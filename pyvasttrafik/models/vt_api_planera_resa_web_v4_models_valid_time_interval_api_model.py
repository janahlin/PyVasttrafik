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


class VTApiPlaneraResaWebV4ModelsValidTimeIntervalApiModel(object):
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
        'valid_from': 'str',
        'valid_until': 'str'
    }

    attribute_map = {
        'valid_from': 'validFrom',
        'valid_until': 'validUntil'
    }

    def __init__(self, valid_from=None, valid_until=None, local_vars_configuration=None):  # noqa: E501
        """VTApiPlaneraResaWebV4ModelsValidTimeIntervalApiModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._valid_from = None
        self._valid_until = None
        self.discriminator = None

        self.valid_from = valid_from
        self.valid_until = valid_until

    @property
    def valid_from(self):
        """Gets the valid_from of this VTApiPlaneraResaWebV4ModelsValidTimeIntervalApiModel.  # noqa: E501

        The start time of the interval when valid journey information is available, specified in RFC 3339 format.  # noqa: E501

        :return: The valid_from of this VTApiPlaneraResaWebV4ModelsValidTimeIntervalApiModel.  # noqa: E501
        :rtype: str
        """
        return self._valid_from

    @valid_from.setter
    def valid_from(self, valid_from):
        """Sets the valid_from of this VTApiPlaneraResaWebV4ModelsValidTimeIntervalApiModel.

        The start time of the interval when valid journey information is available, specified in RFC 3339 format.  # noqa: E501

        :param valid_from: The valid_from of this VTApiPlaneraResaWebV4ModelsValidTimeIntervalApiModel.  # noqa: E501
        :type valid_from: str
        """

        self._valid_from = valid_from

    @property
    def valid_until(self):
        """Gets the valid_until of this VTApiPlaneraResaWebV4ModelsValidTimeIntervalApiModel.  # noqa: E501

        The end time of the interval when valid journey information is available, specified in RFC 3339 format.  # noqa: E501

        :return: The valid_until of this VTApiPlaneraResaWebV4ModelsValidTimeIntervalApiModel.  # noqa: E501
        :rtype: str
        """
        return self._valid_until

    @valid_until.setter
    def valid_until(self, valid_until):
        """Sets the valid_until of this VTApiPlaneraResaWebV4ModelsValidTimeIntervalApiModel.

        The end time of the interval when valid journey information is available, specified in RFC 3339 format.  # noqa: E501

        :param valid_until: The valid_until of this VTApiPlaneraResaWebV4ModelsValidTimeIntervalApiModel.  # noqa: E501
        :type valid_until: str
        """

        self._valid_until = valid_until

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
        if not isinstance(other, VTApiPlaneraResaWebV4ModelsValidTimeIntervalApiModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VTApiPlaneraResaWebV4ModelsValidTimeIntervalApiModel):
            return True

        return self.to_dict() != other.to_dict()