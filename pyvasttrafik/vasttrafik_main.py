"""pyvasttrafik module"""
from __future__ import annotations

from typing import Any, cast
from abc import ABCMeta, abstractmethod
from enum import Enum

import base64
import datetime
import requests
import re
import six
from six.moves.urllib.parse import quote
import json
from dateutil.parser import parse
import urllib3
import aiohttp
from lxml import etree

from pyvasttrafik.config import Configuration
from pyvasttrafik import rest
from pyvasttrafik import api_models

from .exceptions import InvalidAuthentication, UnknownError


class FilterOperation(Enum):
    """Contains all field filter operations."""

    EQUAL = "EQ"
    EXISTS = "EXISTS"
    GREATER_THAN = "GT"
    GREATER_THAN_EQUAL = "GTE"
    LESS_THAN = "LT"
    LESS_THAN_EQUAL = "LTE"
    NOT_EQUAL = "NE"
    LIKE = "LIKE"
    NOT_LIKE = "NOTLIKE"
    #    IN = "IN"
    NOT_IN = "NOTIN"
    WITH_IN = "WITHIN"


class SortOrder(Enum):
    """Specifies how rows of data are sorted."""

    ASCENDING = "asc"
    DECENDING = "desc"


class FieldSort:
    """What field and how to sort on it."""

    def __init__(self, field: str, sort_order: SortOrder) -> None:
        """Initialize the class."""
        self._field = field
        self._sort_order = sort_order

    def to_string(self) -> str:
        """Sort_order as string."""
        return self._field + " " + self._sort_order.value


class Filter:
    """Base class for all filters."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def generate_node(self, parent_node: Any) -> Any:
        """Generate node."""


class FieldFilter(Filter):
    """Used to filter on one field."""

    def __init__(self, operation: FilterOperation, name: str, value: Any) -> None:
        """Initialize the class."""
        self.operation = operation
        self.name = name
        self.value = value

    def generate_node(self, parent_node: Any) -> Any:
        """Return element node for field filter."""
        filter_node = etree.SubElement(parent_node, self.operation.value)
        filter_node.attrib["name"] = self.name
        filter_node.attrib["value"] = self.value
        return filter_node


class OrFilter(Filter):
    """Used to create a Or filter."""

    def __init__(self, filters: list[Filter]) -> None:
        """Initialize the class."""
        self.filters = filters

    def generate_node(self, parent_node: Any) -> Any:
        """Return element node for filter."""
        or_node = etree.SubElement(parent_node, "OR")
        for sub_filter in self.filters:
            sub_filter.generate_node(or_node)
        return or_node


class AndFilter(Filter):
    """Used to create a And filter."""

    def __init__(self, filters: list[Filter]) -> None:
        """Initialize the class."""
        self.filters = filters

    def generate_node(self, parent_node: Any) -> Any:
        """Return element node for filter."""
        or_node = etree.SubElement(parent_node, "AND")
        for sub_filter in self.filters:
            sub_filter.generate_node(or_node)
        return or_node


class Auth:
    def __init__(self, key, secret, scope):
        if key is None or secret is None or scope is None:
            raise TypeError("Usage: Auth(<key>, <secret>, <scope>)")

        if type(key) != str:
            raise TypeError("Expected str [key]")
        if type(secret) != str:
            raise TypeError("Expected str [secret]")
        if type(scope) != int:
            raise TypeError("Expected int [scope]")

        self.__credentials = base64.b64encode(str.encode(f'{key}:{secret}')).decode("utf-8")
        self.scope = scope

        self.__renew_token()

    def __renew_token(self):
        header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Basic " + self.__credentials
        }
        url = f'https://ext-api.vasttrafik.se/token?grant_type=client_credentials&scope=device_{self.scope}'
        response = requests.post(url, headers=header)
        response_dict = response.json()

        if response.status_code != 200:
            raise requests.exceptions.HTTPError(f'{response.status_code} {response_dict.get("error_description")}')

        # self.token = "Bearer " + response_dict.get("access_token")
        self.token = response_dict.get("access_token")

    def check_response(self, response):
        if response.status_code == 401:
            self.__renew_token()

            header = {"Authorization": self.token}
            response = requests.get(response.url, headers=header)

        response_dict = response.json()
        if response.status_code != 200:
            raise requests.exceptions.HTTPError(f'{response.status_code} {response_dict.get("error_description")}')

        return response


class Vasttrafik:
    """Class used to communicate with västtrafik api."""
    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,  # noqa: F821
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }

    date_time_format = "%Y-%m-%dT%H:%M:%S.%f%z"
    date_time_format_for_modified = "%Y-%m-%dT%H:%M:%S.%fZ"

    def __init__(self, configuration=None):
        """Initialize main Västtrafik object."""
        if configuration is None:
            configuration = Configuration.get_default_copy()
        self.configuration = configuration
        self.configuration = configuration

        self.rest_client = rest.RESTClientObject(configuration)
        self.default_headers = {}
        # if header_name is not None:
        #    self.default_headers[header_name] = header_value
        # Set default User-Agent.
        self.user_agent = 'OpenAPI-Generator/1.0.0/python'
        # self.client_side_validation = configuration.client_side_validation

    @property
    def user_agent(self):
        """User agent for this API client"""
        return self.default_headers['User-Agent']

    @user_agent.setter
    def user_agent(self, value):
        self.default_headers['User-Agent'] = value

    def make_request(
            self,
            objecttype: str,
            query_params=None,
            header_params=None,
            body=None,
            response_types_map=None,
            auth_settings=None,
            path_params=None,
            _return_http_data_only=None,
            _request_auth=None,
            _preload_content=True,
            _host=None,
    ):

        # header parameters
        header_params = header_params or {}
        header_params.update(self.default_headers)

        if query_params:
            query_params = query_params

        # path parameters
        if path_params:
            for k, v in path_params.items():
                # specified safe chars, encode everything
                objecttype = objecttype.replace(
                    '{%s}' % k,
                    quote(str(v), safe=self.configuration.safe_chars_for_path_param)
                )

        self.update_params_for_auth(
            header_params, query_params, auth_settings,
            request_auth=_request_auth)

        if _host is None:
            url = self.configuration.host + objecttype
        else:
            # use server/host defined in path or operation instead
            url = _host + objecttype
        try:
            response_data = self.request(url, query_params=query_params, headers=header_params)
        except Exception as e:
            e.body = e.body
            raise e

        # self.last_response = response_data

        return_data = response_data

        if not _preload_content:
            return return_data

        response_type = response_types_map.get(response_data.status, None)

        if six.PY3 and response_type not in ["file", "bytes"]:
            match = None
            content_type = response_data.getheader('content-type')
            if content_type is not None:
                match = re.search(r"charset=([a-zA-Z\-\d]+)[\s\;]?", content_type)
            encoding = match.group(1) if match else "utf-8"
            response_data.data = response_data.data.decode(encoding)

        if response_type:
            return_data = self.deserialize(response_data, response_type)
        else:
            return_data = None

        if _return_http_data_only:
            return return_data
        else:
            return (return_data, response_data.status,
                    response_data.getheaders())

    def select_header_accept(self, accepts):
        """Returns `Accept` based on an array of accepts provided.

        :param accepts: List of headers.
        :return: Accept (e.g. application/json).
        """
        if not accepts:
            return

        accepts = [x.lower() for x in accepts]

        if 'application/json' in accepts:
            return 'application/json'
        else:
            return ', '.join(accepts)

    def update_params_for_auth(self, headers, queries, auth_settings,
                               request_auth=None):

        if not auth_settings:
            return

        if request_auth:
            self._apply_auth_params(headers, queries, request_auth)
            return

        for auth in auth_settings:
            auth_setting = self.configuration.auth_settings().get(auth)
            if auth_setting:
                self._apply_auth_params(headers, queries, auth_setting)

    def _apply_auth_params(self, headers, queries, auth_setting):

        if auth_setting['in'] == 'cookie':
            headers['Cookie'] = auth_setting['value']
        elif auth_setting['in'] == 'header':
            headers[auth_setting['key']] = auth_setting['value']
        elif auth_setting['in'] == 'query':
            queries.append((auth_setting['key'], auth_setting['value']))
        else:
            raise Exception(
                'Authentication token must be in `query` or `header`'
            )

    def request(self, url, query_params=None, headers=None,
                post_params=None, body=None, _preload_content=True,
                _request_timeout=None):
        """Makes the HTTP request using RESTClient."""
        return self.rest_client.GET(url,
                                    query_params=query_params,
                                    _preload_content=_preload_content,
                                    _request_timeout=_request_timeout,
                                    headers=headers)

    def deserialize(self, response, response_type):
        """Deserializes response into an object.

        :param response: RESTResponse object to be deserialized.
        :param response_type: class literal for
            deserialized object, or string of class name.

        :return: deserialized object.
        """

        # handle file downloading
        # save response body into a tmp file and return the instance
        if response_type == "file":
            # return self.__deserialize_file(response)
            return "fil"
        # fetch data from response object
        try:
            data = json.loads(response.data)
        except ValueError:
            data = response.data

        return self.__deserialize(data, response_type)

    def __deserialize(self, data, klass):
        """Deserializes dict, list, str into an object.

        :param data: dict, list or str.
        :param klass: class literal, or string of class name.

        :return: object.
        """
        if data is None:
            return None

        if type(klass) == str:
            if klass.startswith('list['):
                sub_kls = re.match(r'list\[(.*)]', klass).group(1)
                return [self.__deserialize(sub_data, sub_kls)
                        for sub_data in data]

            if klass.startswith('dict['):
                sub_kls = re.match(r'dict\[([^,]*), (.*)]', klass).group(2)
                return {k: self.__deserialize(v, sub_kls)
                        for k, v in six.iteritems(data)}

            # convert str to class
            if klass in self.NATIVE_TYPES_MAPPING:
                klass = self.NATIVE_TYPES_MAPPING[klass]
            else:
                klass = getattr(api_models, klass)

        if klass in self.PRIMITIVE_TYPES:
            return self.__deserialize_primitive(data, klass)
        elif klass == object:
            return self.__deserialize_object(data)
        elif klass == datetime.date:
            return self.__deserialize_date(data)
        elif klass == datetime.datetime:
            return self.__deserialize_datetime(data)
        else:
            return self.__deserialize_model(data, klass)

    def __deserialize_primitive(self, data, klass):
        """Deserializes string to primitive type.

        :param data: str.
        :param klass: class literal.

        :return: int, long, float, str, bool.
        """
        try:
            return klass(data)
        except UnicodeEncodeError:
            return six.text_type(data)
        except TypeError:
            return data

    def __deserialize_object(self, value):
        """Return an original value.

        :return: object.
        """
        # print("Object")
        # print(value)
        return value

    def __deserialize_date(self, string):
        """Deserializes string to date.

        :param string: str.
        :return: date.
        """
        # print("Date")
        # print(string)
        try:
            return parse(string).date()
        except ImportError:
            return string
        except ValueError:
            raise rest.ApiException(
                status=0,
                reason="Failed to parse `{0}` as date object".format(string)
            )

    def __deserialize_datetime(self, string):
        """Deserializes string to datetime.

        The string should be in iso8601 datetime format.

        :param string: str.
        :return: datetime.
        """
        # print("DateTime")
        # print(string)
        try:
            return parse(string)
        except ImportError:
            return string
        except ValueError:
            raise rest.ApiException(
                status=0,
                reason=(
                    "Failed to parse `{0}` as datetime object"
                    .format(string)
                )
            )

    def __deserialize_model(self, data, klass):
        """Deserializes list or dict to model.

        :param data: dict, list.
        :param klass: class literal.
        :return: model object.
        """

        has_discriminator = False
        if (hasattr(klass, 'get_real_child_model')
                and klass.discriminator_value_class_map):
            has_discriminator = True

        if not klass.api_types and has_discriminator is False:
            return data

        kwargs = {}
        if (data is not None and
                klass.api_types is not None and
                isinstance(data, (list, dict))):
            for attr, attr_type in six.iteritems(klass.api_types):
                if klass.attribute_map[attr] in data:
                    value = data[klass.attribute_map[attr]]
                    kwargs[attr] = self.__deserialize(value, attr_type)

        kwargs["local_vars_configuration"] = self.configuration
        instance = klass(**kwargs)

        if has_discriminator:
            klass_name = instance.get_real_child_model(data)
            if klass_name:
                instance = self.__deserialize(data, klass_name)
        return instance
