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


class VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel(object):
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
        'departure_access_link': 'VTApiPlaneraResaWebV4ModelsJourneyDetailsDepartureAccessLinkApiModel',
        'trip_legs': 'list[VTApiPlaneraResaWebV4ModelsJourneyDetailsTripLegDetailsApiModel]',
        'connection_links': 'list[VTApiPlaneraResaWebV4ModelsJourneyDetailsConnectionLinkApiModel]',
        'arrival_access_link': 'VTApiPlaneraResaWebV4ModelsJourneyDetailsArrivalAccessLinkApiModel',
        'destination_link': 'VTApiPlaneraResaWebV4ModelsJourneyDetailsDestinationLinkApiModel',
        'ticket_suggestions_result': 'VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketSuggestionsResultApiModel',
        'tariff_zones': 'list[VTApiPlaneraResaWebV4ModelsJourneyDetailsTariffZoneApiModel]',
        'occupancy': 'VTApiPlaneraResaWebV4ModelsOccupancyInformationApiModel'
    }

    attribute_map = {
        'departure_access_link': 'departureAccessLink',
        'trip_legs': 'tripLegs',
        'connection_links': 'connectionLinks',
        'arrival_access_link': 'arrivalAccessLink',
        'destination_link': 'destinationLink',
        'ticket_suggestions_result': 'ticketSuggestionsResult',
        'tariff_zones': 'tariffZones',
        'occupancy': 'occupancy'
    }

    def __init__(self, departure_access_link=None, trip_legs=None, connection_links=None, arrival_access_link=None, destination_link=None, ticket_suggestions_result=None, tariff_zones=None, occupancy=None, local_vars_configuration=None):  # noqa: E501
        """VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._departure_access_link = None
        self._trip_legs = None
        self._connection_links = None
        self._arrival_access_link = None
        self._destination_link = None
        self._ticket_suggestions_result = None
        self._tariff_zones = None
        self._occupancy = None
        self.discriminator = None

        if departure_access_link is not None:
            self.departure_access_link = departure_access_link
        self.trip_legs = trip_legs
        self.connection_links = connection_links
        if arrival_access_link is not None:
            self.arrival_access_link = arrival_access_link
        if destination_link is not None:
            self.destination_link = destination_link
        if ticket_suggestions_result is not None:
            self.ticket_suggestions_result = ticket_suggestions_result
        self.tariff_zones = tariff_zones
        if occupancy is not None:
            self.occupancy = occupancy

    @property
    def departure_access_link(self):
        """Gets the departure_access_link of this VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.  # noqa: E501


        :return: The departure_access_link of this VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.  # noqa: E501
        :rtype: VTApiPlaneraResaWebV4ModelsJourneyDetailsDepartureAccessLinkApiModel
        """
        return self._departure_access_link

    @departure_access_link.setter
    def departure_access_link(self, departure_access_link):
        """Sets the departure_access_link of this VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.


        :param departure_access_link: The departure_access_link of this VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.  # noqa: E501
        :type departure_access_link: VTApiPlaneraResaWebV4ModelsJourneyDetailsDepartureAccessLinkApiModel
        """

        self._departure_access_link = departure_access_link

    @property
    def trip_legs(self):
        """Gets the trip_legs of this VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.  # noqa: E501

        Detailed information, including stops, about the trip legs.  # noqa: E501

        :return: The trip_legs of this VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.  # noqa: E501
        :rtype: list[VTApiPlaneraResaWebV4ModelsJourneyDetailsTripLegDetailsApiModel]
        """
        return self._trip_legs

    @trip_legs.setter
    def trip_legs(self, trip_legs):
        """Sets the trip_legs of this VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.

        Detailed information, including stops, about the trip legs.  # noqa: E501

        :param trip_legs: The trip_legs of this VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.  # noqa: E501
        :type trip_legs: list[VTApiPlaneraResaWebV4ModelsJourneyDetailsTripLegDetailsApiModel]
        """

        self._trip_legs = trip_legs

    @property
    def connection_links(self):
        """Gets the connection_links of this VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.  # noqa: E501

        A list of ConnectionLinks between TripLegs, when applicable. The internal order of TripLegs and ConnectionLinks is defined by Index-property on the objects.  # noqa: E501

        :return: The connection_links of this VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.  # noqa: E501
        :rtype: list[VTApiPlaneraResaWebV4ModelsJourneyDetailsConnectionLinkApiModel]
        """
        return self._connection_links

    @connection_links.setter
    def connection_links(self, connection_links):
        """Sets the connection_links of this VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.

        A list of ConnectionLinks between TripLegs, when applicable. The internal order of TripLegs and ConnectionLinks is defined by Index-property on the objects.  # noqa: E501

        :param connection_links: The connection_links of this VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.  # noqa: E501
        :type connection_links: list[VTApiPlaneraResaWebV4ModelsJourneyDetailsConnectionLinkApiModel]
        """

        self._connection_links = connection_links

    @property
    def arrival_access_link(self):
        """Gets the arrival_access_link of this VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.  # noqa: E501


        :return: The arrival_access_link of this VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.  # noqa: E501
        :rtype: VTApiPlaneraResaWebV4ModelsJourneyDetailsArrivalAccessLinkApiModel
        """
        return self._arrival_access_link

    @arrival_access_link.setter
    def arrival_access_link(self, arrival_access_link):
        """Sets the arrival_access_link of this VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.


        :param arrival_access_link: The arrival_access_link of this VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.  # noqa: E501
        :type arrival_access_link: VTApiPlaneraResaWebV4ModelsJourneyDetailsArrivalAccessLinkApiModel
        """

        self._arrival_access_link = arrival_access_link

    @property
    def destination_link(self):
        """Gets the destination_link of this VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.  # noqa: E501


        :return: The destination_link of this VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.  # noqa: E501
        :rtype: VTApiPlaneraResaWebV4ModelsJourneyDetailsDestinationLinkApiModel
        """
        return self._destination_link

    @destination_link.setter
    def destination_link(self, destination_link):
        """Sets the destination_link of this VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.


        :param destination_link: The destination_link of this VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.  # noqa: E501
        :type destination_link: VTApiPlaneraResaWebV4ModelsJourneyDetailsDestinationLinkApiModel
        """

        self._destination_link = destination_link

    @property
    def ticket_suggestions_result(self):
        """Gets the ticket_suggestions_result of this VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.  # noqa: E501


        :return: The ticket_suggestions_result of this VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.  # noqa: E501
        :rtype: VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketSuggestionsResultApiModel
        """
        return self._ticket_suggestions_result

    @ticket_suggestions_result.setter
    def ticket_suggestions_result(self, ticket_suggestions_result):
        """Sets the ticket_suggestions_result of this VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.


        :param ticket_suggestions_result: The ticket_suggestions_result of this VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.  # noqa: E501
        :type ticket_suggestions_result: VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketSuggestionsResultApiModel
        """

        self._ticket_suggestions_result = ticket_suggestions_result

    @property
    def tariff_zones(self):
        """Gets the tariff_zones of this VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.  # noqa: E501

        The tariff zones that the journey traverses.  # noqa: E501

        :return: The tariff_zones of this VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.  # noqa: E501
        :rtype: list[VTApiPlaneraResaWebV4ModelsJourneyDetailsTariffZoneApiModel]
        """
        return self._tariff_zones

    @tariff_zones.setter
    def tariff_zones(self, tariff_zones):
        """Sets the tariff_zones of this VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.

        The tariff zones that the journey traverses.  # noqa: E501

        :param tariff_zones: The tariff_zones of this VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.  # noqa: E501
        :type tariff_zones: list[VTApiPlaneraResaWebV4ModelsJourneyDetailsTariffZoneApiModel]
        """

        self._tariff_zones = tariff_zones

    @property
    def occupancy(self):
        """Gets the occupancy of this VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.  # noqa: E501


        :return: The occupancy of this VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.  # noqa: E501
        :rtype: VTApiPlaneraResaWebV4ModelsOccupancyInformationApiModel
        """
        return self._occupancy

    @occupancy.setter
    def occupancy(self, occupancy):
        """Sets the occupancy of this VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.


        :param occupancy: The occupancy of this VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel.  # noqa: E501
        :type occupancy: VTApiPlaneraResaWebV4ModelsOccupancyInformationApiModel
        """

        self._occupancy = occupancy

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
        if not isinstance(other, VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel):
            return True

        return self.to_dict() != other.to_dict()
