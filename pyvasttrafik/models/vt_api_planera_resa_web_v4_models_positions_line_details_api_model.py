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


class VTApiPlaneraResaWebV4ModelsPositionsLineDetailsApiModel(object):
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
        'name': 'str',
        'background_color': 'str',
        'foreground_color': 'str',
        'border_color': 'str',
        'transport_mode': 'VTApiPlaneraResaCoreModelsTransportMode',
        'transport_sub_mode': 'VTApiPlaneraResaCoreModelsTransportSubMode'
    }

    attribute_map = {
        'name': 'name',
        'background_color': 'backgroundColor',
        'foreground_color': 'foregroundColor',
        'border_color': 'borderColor',
        'transport_mode': 'transportMode',
        'transport_sub_mode': 'transportSubMode'
    }

    def __init__(self, name=None, background_color=None, foreground_color=None, border_color=None, transport_mode=None, transport_sub_mode=None, local_vars_configuration=None):  # noqa: E501
        """VTApiPlaneraResaWebV4ModelsPositionsLineDetailsApiModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._background_color = None
        self._foreground_color = None
        self._border_color = None
        self._transport_mode = None
        self._transport_sub_mode = None
        self.discriminator = None

        self.name = name
        self.background_color = background_color
        self.foreground_color = foreground_color
        self.border_color = border_color
        if transport_mode is not None:
            self.transport_mode = transport_mode
        if transport_sub_mode is not None:
            self.transport_sub_mode = transport_sub_mode

    @property
    def name(self):
        """Gets the name of this VTApiPlaneraResaWebV4ModelsPositionsLineDetailsApiModel.  # noqa: E501

        The line name.  # noqa: E501

        :return: The name of this VTApiPlaneraResaWebV4ModelsPositionsLineDetailsApiModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VTApiPlaneraResaWebV4ModelsPositionsLineDetailsApiModel.

        The line name.  # noqa: E501

        :param name: The name of this VTApiPlaneraResaWebV4ModelsPositionsLineDetailsApiModel.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def background_color(self):
        """Gets the background_color of this VTApiPlaneraResaWebV4ModelsPositionsLineDetailsApiModel.  # noqa: E501

        The background color of the line symbol.  # noqa: E501

        :return: The background_color of this VTApiPlaneraResaWebV4ModelsPositionsLineDetailsApiModel.  # noqa: E501
        :rtype: str
        """
        return self._background_color

    @background_color.setter
    def background_color(self, background_color):
        """Sets the background_color of this VTApiPlaneraResaWebV4ModelsPositionsLineDetailsApiModel.

        The background color of the line symbol.  # noqa: E501

        :param background_color: The background_color of this VTApiPlaneraResaWebV4ModelsPositionsLineDetailsApiModel.  # noqa: E501
        :type background_color: str
        """

        self._background_color = background_color

    @property
    def foreground_color(self):
        """Gets the foreground_color of this VTApiPlaneraResaWebV4ModelsPositionsLineDetailsApiModel.  # noqa: E501

        The foreground color of the line symbol.  # noqa: E501

        :return: The foreground_color of this VTApiPlaneraResaWebV4ModelsPositionsLineDetailsApiModel.  # noqa: E501
        :rtype: str
        """
        return self._foreground_color

    @foreground_color.setter
    def foreground_color(self, foreground_color):
        """Sets the foreground_color of this VTApiPlaneraResaWebV4ModelsPositionsLineDetailsApiModel.

        The foreground color of the line symbol.  # noqa: E501

        :param foreground_color: The foreground_color of this VTApiPlaneraResaWebV4ModelsPositionsLineDetailsApiModel.  # noqa: E501
        :type foreground_color: str
        """

        self._foreground_color = foreground_color

    @property
    def border_color(self):
        """Gets the border_color of this VTApiPlaneraResaWebV4ModelsPositionsLineDetailsApiModel.  # noqa: E501

        The border color of the line symbol.  # noqa: E501

        :return: The border_color of this VTApiPlaneraResaWebV4ModelsPositionsLineDetailsApiModel.  # noqa: E501
        :rtype: str
        """
        return self._border_color

    @border_color.setter
    def border_color(self, border_color):
        """Sets the border_color of this VTApiPlaneraResaWebV4ModelsPositionsLineDetailsApiModel.

        The border color of the line symbol.  # noqa: E501

        :param border_color: The border_color of this VTApiPlaneraResaWebV4ModelsPositionsLineDetailsApiModel.  # noqa: E501
        :type border_color: str
        """

        self._border_color = border_color

    @property
    def transport_mode(self):
        """Gets the transport_mode of this VTApiPlaneraResaWebV4ModelsPositionsLineDetailsApiModel.  # noqa: E501


        :return: The transport_mode of this VTApiPlaneraResaWebV4ModelsPositionsLineDetailsApiModel.  # noqa: E501
        :rtype: VTApiPlaneraResaCoreModelsTransportMode
        """
        return self._transport_mode

    @transport_mode.setter
    def transport_mode(self, transport_mode):
        """Sets the transport_mode of this VTApiPlaneraResaWebV4ModelsPositionsLineDetailsApiModel.


        :param transport_mode: The transport_mode of this VTApiPlaneraResaWebV4ModelsPositionsLineDetailsApiModel.  # noqa: E501
        :type transport_mode: VTApiPlaneraResaCoreModelsTransportMode
        """

        self._transport_mode = transport_mode

    @property
    def transport_sub_mode(self):
        """Gets the transport_sub_mode of this VTApiPlaneraResaWebV4ModelsPositionsLineDetailsApiModel.  # noqa: E501


        :return: The transport_sub_mode of this VTApiPlaneraResaWebV4ModelsPositionsLineDetailsApiModel.  # noqa: E501
        :rtype: VTApiPlaneraResaCoreModelsTransportSubMode
        """
        return self._transport_sub_mode

    @transport_sub_mode.setter
    def transport_sub_mode(self, transport_sub_mode):
        """Sets the transport_sub_mode of this VTApiPlaneraResaWebV4ModelsPositionsLineDetailsApiModel.


        :param transport_sub_mode: The transport_sub_mode of this VTApiPlaneraResaWebV4ModelsPositionsLineDetailsApiModel.  # noqa: E501
        :type transport_sub_mode: VTApiPlaneraResaCoreModelsTransportSubMode
        """

        self._transport_sub_mode = transport_sub_mode

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
        if not isinstance(other, VTApiPlaneraResaWebV4ModelsPositionsLineDetailsApiModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VTApiPlaneraResaWebV4ModelsPositionsLineDetailsApiModel):
            return True

        return self.to_dict() != other.to_dict()
