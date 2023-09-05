# coding: utf-8

"""
    Störning

    Störningsinformation för realtid och planerad trafik  # noqa: E501

    The version of the OpenAPI document: v1
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


class StopPointApiModel(object):
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
        'gid': 'str',
        'name': 'str',
        'short_name': 'str',
        'stop_area_gid': 'str',
        'stop_area_name': 'str',
        'stop_area_short_name': 'str',
        'municipality_name': 'str',
        'municipality_number': 'int'
    }

    attribute_map = {
        'gid': 'gid',
        'name': 'name',
        'short_name': 'shortName',
        'stop_area_gid': 'stopAreaGid',
        'stop_area_name': 'stopAreaName',
        'stop_area_short_name': 'stopAreaShortName',
        'municipality_name': 'municipalityName',
        'municipality_number': 'municipalityNumber'
    }

    def __init__(self, gid=None, name=None, short_name=None, stop_area_gid=None, stop_area_name=None, stop_area_short_name=None, municipality_name=None, municipality_number=None, local_vars_configuration=None):  # noqa: E501
        """StopPointApiModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._gid = None
        self._name = None
        self._short_name = None
        self._stop_area_gid = None
        self._stop_area_name = None
        self._stop_area_short_name = None
        self._municipality_name = None
        self._municipality_number = None
        self.discriminator = None

        self.gid = gid
        if name is not None:
            self.name = name
        if short_name is not None:
            self.short_name = short_name
        if stop_area_gid is not None:
            self.stop_area_gid = stop_area_gid
        if stop_area_name is not None:
            self.stop_area_name = stop_area_name
        if stop_area_short_name is not None:
            self.stop_area_short_name = stop_area_short_name
        if municipality_name is not None:
            self.municipality_name = municipality_name
        if municipality_number is not None:
            self.municipality_number = municipality_number

    @property
    def gid(self):
        """Gets the gid of this StopPointApiModel.  # noqa: E501

        Example data: 9022014003310004  # noqa: E501

        :return: The gid of this StopPointApiModel.  # noqa: E501
        :rtype: str
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this StopPointApiModel.

        Example data: 9022014003310004  # noqa: E501

        :param gid: The gid of this StopPointApiModel.  # noqa: E501
        :type gid: str
        """
        if self.local_vars_configuration.client_side_validation and gid is None:  # noqa: E501
            raise ValueError("Invalid value for `gid`, must not be `None`")  # noqa: E501

        self._gid = gid

    @property
    def name(self):
        """Gets the name of this StopPointApiModel.  # noqa: E501

        Full name of stop point.  Example data: \"Ã–xnered station (tÃ¥g)\"  # noqa: E501

        :return: The name of this StopPointApiModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StopPointApiModel.

        Full name of stop point.  Example data: \"Ã–xnered station (tÃ¥g)\"  # noqa: E501

        :param name: The name of this StopPointApiModel.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def short_name(self):
        """Gets the short_name of this StopPointApiModel.  # noqa: E501

        Short name of stop point.  Example data: \"Ã–xnered stn\"  # noqa: E501

        :return: The short_name of this StopPointApiModel.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this StopPointApiModel.

        Short name of stop point.  Example data: \"Ã–xnered stn\"  # noqa: E501

        :param short_name: The short_name of this StopPointApiModel.  # noqa: E501
        :type short_name: str
        """

        self._short_name = short_name

    @property
    def stop_area_gid(self):
        """Gets the stop_area_gid of this StopPointApiModel.  # noqa: E501

        Example data: 9021014080800000  # noqa: E501

        :return: The stop_area_gid of this StopPointApiModel.  # noqa: E501
        :rtype: str
        """
        return self._stop_area_gid

    @stop_area_gid.setter
    def stop_area_gid(self, stop_area_gid):
        """Sets the stop_area_gid of this StopPointApiModel.

        Example data: 9021014080800000  # noqa: E501

        :param stop_area_gid: The stop_area_gid of this StopPointApiModel.  # noqa: E501
        :type stop_area_gid: str
        """

        self._stop_area_gid = stop_area_gid

    @property
    def stop_area_name(self):
        """Gets the stop_area_name of this StopPointApiModel.  # noqa: E501

        Full name of stop area.  Example data: \"Ã–xnered station (tÃ¥g)\"  # noqa: E501

        :return: The stop_area_name of this StopPointApiModel.  # noqa: E501
        :rtype: str
        """
        return self._stop_area_name

    @stop_area_name.setter
    def stop_area_name(self, stop_area_name):
        """Sets the stop_area_name of this StopPointApiModel.

        Full name of stop area.  Example data: \"Ã–xnered station (tÃ¥g)\"  # noqa: E501

        :param stop_area_name: The stop_area_name of this StopPointApiModel.  # noqa: E501
        :type stop_area_name: str
        """

        self._stop_area_name = stop_area_name

    @property
    def stop_area_short_name(self):
        """Gets the stop_area_short_name of this StopPointApiModel.  # noqa: E501

        Short name of stop point.  Example data: \"Ã–xnered stn\"  # noqa: E501

        :return: The stop_area_short_name of this StopPointApiModel.  # noqa: E501
        :rtype: str
        """
        return self._stop_area_short_name

    @stop_area_short_name.setter
    def stop_area_short_name(self, stop_area_short_name):
        """Sets the stop_area_short_name of this StopPointApiModel.

        Short name of stop point.  Example data: \"Ã–xnered stn\"  # noqa: E501

        :param stop_area_short_name: The stop_area_short_name of this StopPointApiModel.  # noqa: E501
        :type stop_area_short_name: str
        """

        self._stop_area_short_name = stop_area_short_name

    @property
    def municipality_name(self):
        """Gets the municipality_name of this StopPointApiModel.  # noqa: E501

        Example data: \"Partille\"  # noqa: E501

        :return: The municipality_name of this StopPointApiModel.  # noqa: E501
        :rtype: str
        """
        return self._municipality_name

    @municipality_name.setter
    def municipality_name(self, municipality_name):
        """Sets the municipality_name of this StopPointApiModel.

        Example data: \"Partille\"  # noqa: E501

        :param municipality_name: The municipality_name of this StopPointApiModel.  # noqa: E501
        :type municipality_name: str
        """

        self._municipality_name = municipality_name

    @property
    def municipality_number(self):
        """Gets the municipality_number of this StopPointApiModel.  # noqa: E501

        Example data : 1402  # noqa: E501

        :return: The municipality_number of this StopPointApiModel.  # noqa: E501
        :rtype: int
        """
        return self._municipality_number

    @municipality_number.setter
    def municipality_number(self, municipality_number):
        """Sets the municipality_number of this StopPointApiModel.

        Example data : 1402  # noqa: E501

        :param municipality_number: The municipality_number of this StopPointApiModel.  # noqa: E501
        :type municipality_number: int
        """

        self._municipality_number = municipality_number

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
        if not isinstance(other, StopPointApiModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StopPointApiModel):
            return True

        return self.to_dict() != other.to_dict()
