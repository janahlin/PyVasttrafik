# coding: utf-8

"""
    Planera Resa

    Sök och planera resor med Västtrafik  # noqa: E501

    The version of the OpenAPI document: v4
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from pyvasttrafik.api.configuration import Configuration


class VTApiPlaneraResaWebV4ModelsPaginationProperties(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'size': 'int'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'size': 'size'
    }

    def __init__(self, limit=None, offset=None, size=None, local_vars_configuration=None):  # noqa: E501
        """VTApiPlaneraResaWebV4ModelsPaginationProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._limit = None
        self._offset = None
        self._size = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if size is not None:
            self.size = size

    @property
    def limit(self):
        """Gets the limit of this VTApiPlaneraResaWebV4ModelsPaginationProperties.  # noqa: E501

        The requested number of results.  # noqa: E501

        :return: The limit of this VTApiPlaneraResaWebV4ModelsPaginationProperties.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this VTApiPlaneraResaWebV4ModelsPaginationProperties.

        The requested number of results.  # noqa: E501

        :param limit: The limit of this VTApiPlaneraResaWebV4ModelsPaginationProperties.  # noqa: E501
        :type limit: int
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this VTApiPlaneraResaWebV4ModelsPaginationProperties.  # noqa: E501

        The requested offset in the results array.  # noqa: E501

        :return: The offset of this VTApiPlaneraResaWebV4ModelsPaginationProperties.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this VTApiPlaneraResaWebV4ModelsPaginationProperties.

        The requested offset in the results array.  # noqa: E501

        :param offset: The offset of this VTApiPlaneraResaWebV4ModelsPaginationProperties.  # noqa: E501
        :type offset: int
        """

        self._offset = offset

    @property
    def size(self):
        """Gets the size of this VTApiPlaneraResaWebV4ModelsPaginationProperties.  # noqa: E501

        The actual number of returned results.  # noqa: E501

        :return: The size of this VTApiPlaneraResaWebV4ModelsPaginationProperties.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this VTApiPlaneraResaWebV4ModelsPaginationProperties.

        The actual number of returned results.  # noqa: E501

        :param size: The size of this VTApiPlaneraResaWebV4ModelsPaginationProperties.  # noqa: E501
        :type size: int
        """

        self._size = size

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VTApiPlaneraResaWebV4ModelsPaginationProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VTApiPlaneraResaWebV4ModelsPaginationProperties):
            return True

        return self.to_dict() != other.to_dict()