# coding: utf-8

# flake8: noqa

"""
    Planera Resa

    Sök och planera resor med Västtrafik  # noqa: E501

    The version of the OpenAPI document: v4
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
# from pyvasttrafik.vasttrafik import Reseplaneraren

# import ApiClient
# from pyvasttrafik.api.api_client import ApiClient
from pyvasttrafik.api.configuration import Configuration
from pyvasttrafik.api.exceptions import OpenApiException
from pyvasttrafik.api.exceptions import ApiTypeError
from pyvasttrafik.api.exceptions import ApiValueError
from pyvasttrafik.api.exceptions import ApiKeyError
from pyvasttrafik.api.exceptions import ApiAttributeError
from pyvasttrafik.api.exceptions import ApiException
# import models into sdk package

from pyvasttrafik.models.microsoft_asp_net_core_mvc_problem_details import MicrosoftAspNetCoreMvcProblemDetails
from pyvasttrafik.models.vt_api_planera_resa_core_models_date_time_relates_to_type import VTApiPlaneraResaCoreModelsDateTimeRelatesToType
from pyvasttrafik.models.vt_api_planera_resa_core_models_location_type import VTApiPlaneraResaCoreModelsLocationType
from pyvasttrafik.models.vt_api_planera_resa_core_models_note import VTApiPlaneraResaCoreModelsNote
from pyvasttrafik.models.vt_api_planera_resa_core_models_position_transport_mode import VTApiPlaneraResaCoreModelsPositionTransportMode
from pyvasttrafik.models.vt_api_planera_resa_core_models_severity import VTApiPlaneraResaCoreModelsSeverity
from pyvasttrafik.models.vt_api_planera_resa_core_models_time_limitation import VTApiPlaneraResaCoreModelsTimeLimitation
from pyvasttrafik.models.vt_api_planera_resa_core_models_time_validity_type import VTApiPlaneraResaCoreModelsTimeValidityType
from pyvasttrafik.models.vt_api_planera_resa_core_models_time_validity_unit import VTApiPlaneraResaCoreModelsTimeValidityUnit
from pyvasttrafik.models.vt_api_planera_resa_core_models_transport_mode import VTApiPlaneraResaCoreModelsTransportMode
from pyvasttrafik.models.vt_api_planera_resa_core_models_transport_sub_mode import VTApiPlaneraResaCoreModelsTransportSubMode
from pyvasttrafik.models.vt_api_planera_resa_core_models_traveller_category import VTApiPlaneraResaCoreModelsTravellerCategory
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_api_error import VTApiPlaneraResaWebV4ModelsApiError
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_arrival_details_include_type import VTApiPlaneraResaWebV4ModelsArrivalDetailsIncludeType
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_coordinate_api_model import VTApiPlaneraResaWebV4ModelsCoordinateApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_departure_details_include_type import VTApiPlaneraResaWebV4ModelsDepartureDetailsIncludeType
# from .vt_api_planera_resa_web_v4_models_departures_and_arrivals_arrival_api_model import \
#   VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsArrivalApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_departures_and_arrivals_arrival_details_api_model import VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsArrivalDetailsApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_departures_and_arrivals_call_details_api_model import VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsCallDetailsApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_departures_and_arrivals_coordinate_api_model import VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsCoordinateApiModel
from .vt_api_planera_resa_web_v4_models_departures_and_arrivals_departure_api_model import \
    VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsDepartureApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_departures_and_arrivals_departure_details_api_model import VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsDepartureDetailsApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_departures_and_arrivals_get_arrivals_response import VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsGetArrivalsResponse
from .vt_api_planera_resa_web_v4_models_departures_and_arrivals_get_departures_response import \
    VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsGetDeparturesResponse
from .vt_api_planera_resa_web_v4_models_departures_and_arrivals_line_api_model import \
    VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsLineApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_departures_and_arrivals_line_details_api_model import VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsLineDetailsApiModel
from .vt_api_planera_resa_web_v4_models_departures_and_arrivals_service_journey_api_model import \
    VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsServiceJourneyApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_departures_and_arrivals_service_journey_details_api_model import VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsServiceJourneyDetailsApiModel
from .vt_api_planera_resa_web_v4_models_departures_and_arrivals_stop_point_api_model import \
    VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsStopPointApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journey_details_arrival_access_link_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsArrivalAccessLinkApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journey_details_call_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsCallApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journey_details_call_details_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsCallDetailsApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journey_details_channel_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsChannelApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journey_details_connection_link_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsConnectionLinkApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journey_details_departure_access_link_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsDepartureAccessLinkApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journey_details_destination_link_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsDestinationLinkApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journey_details_existing_ticket_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsExistingTicketApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journey_details_include_type import VTApiPlaneraResaWebV4ModelsJourneyDetailsIncludeType
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journey_details_journey_details_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journey_details_line_details_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsLineDetailsApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journey_details_link_endpoint_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsLinkEndpointApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journey_details_link_segment_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsLinkSegmentApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journey_details_punch_configuration_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsPunchConfigurationApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journey_details_punch_configuration_duration_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsPunchConfigurationDurationApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journey_details_service_journey_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsServiceJourneyApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journey_details_stop_area_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsStopAreaApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journey_details_stop_point_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsStopPointApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journey_details_tariff_zone_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsTariffZoneApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journey_details_ticket_suggestion_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketSuggestionApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journey_details_ticket_suggestions_result_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketSuggestionsResultApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journey_details_ticket_validity_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsTicketValidityApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journey_details_time_validity_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsTimeValidityApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journey_details_trip_leg_details_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsTripLegDetailsApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journey_details_zone_api_model import VTApiPlaneraResaWebV4ModelsJourneyDetailsZoneApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journey_transport_mode import VTApiPlaneraResaWebV4ModelsJourneyTransportMode
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journey_transport_sub_mode import VTApiPlaneraResaWebV4ModelsJourneyTransportSubMode
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journeys_arrival_access_link_api_model import VTApiPlaneraResaWebV4ModelsJourneysArrivalAccessLinkApiModel
from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journeys_call_api_model import VTApiPlaneraResaWebV4ModelsJourneysCallApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journeys_connection_link_api_model import VTApiPlaneraResaWebV4ModelsJourneysConnectionLinkApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journeys_departure_access_link_api_model import VTApiPlaneraResaWebV4ModelsJourneysDepartureAccessLinkApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journeys_destination_link_api_model import VTApiPlaneraResaWebV4ModelsJourneysDestinationLinkApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journeys_get_journeys_response import VTApiPlaneraResaWebV4ModelsJourneysGetJourneysResponse
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journeys_journey_api_model import VTApiPlaneraResaWebV4ModelsJourneysJourneyApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journeys_line_api_model import VTApiPlaneraResaWebV4ModelsJourneysLineApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journeys_link_endpoint_api_model import VTApiPlaneraResaWebV4ModelsJourneysLinkEndpointApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journeys_link_segment_api_model import VTApiPlaneraResaWebV4ModelsJourneysLinkSegmentApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journeys_service_journey_api_model import VTApiPlaneraResaWebV4ModelsJourneysServiceJourneyApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journeys_stop_area_api_model import VTApiPlaneraResaWebV4ModelsJourneysStopAreaApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journeys_stop_point_api_model import VTApiPlaneraResaWebV4ModelsJourneysStopPointApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journeys_tariff_zone_api_model import VTApiPlaneraResaWebV4ModelsJourneysTariffZoneApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_journeys_trip_leg_api_model import VTApiPlaneraResaWebV4ModelsJourneysTripLegApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_link_segment_maneuver import VTApiPlaneraResaWebV4ModelsLinkSegmentManeuver
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_link_segment_orientation import VTApiPlaneraResaWebV4ModelsLinkSegmentOrientation
from .vt_api_planera_resa_web_v4_models_location_by_coordinates_type import \
    VTApiPlaneraResaWebV4ModelsLocationByCoordinatesType
from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_location_by_text_type import \
    VTApiPlaneraResaWebV4ModelsLocationByTextType
from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_locations_get_locations_response import \
    VTApiPlaneraResaWebV4ModelsLocationsGetLocationsResponse
from .vt_api_planera_resa_web_v4_models_locations_location_api_model import \
    VTApiPlaneraResaWebV4ModelsLocationsLocationApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_occupancy_information_api_model import VTApiPlaneraResaWebV4ModelsOccupancyInformationApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_occupancy_information_source import VTApiPlaneraResaWebV4ModelsOccupancyInformationSource
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_occupancy_level import VTApiPlaneraResaWebV4ModelsOccupancyLevel
from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_pagination_links import \
    VTApiPlaneraResaWebV4ModelsPaginationLinks
from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_pagination_properties import \
    VTApiPlaneraResaWebV4ModelsPaginationProperties
from .vt_api_planera_resa_web_v4_models_positions_journey_position_api_model import \
    VTApiPlaneraResaWebV4ModelsPositionsJourneyPositionApiModel
from .vt_api_planera_resa_web_v4_models_positions_line_details_api_model import \
    VTApiPlaneraResaWebV4ModelsPositionsLineDetailsApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_product_instance_type_api_model import VTApiPlaneraResaWebV4ModelsProductInstanceTypeApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_punch_configuration_duration_unit_api_model import VTApiPlaneraResaWebV4ModelsPunchConfigurationDurationUnitApiModel
# from pyvasttrafik.models.vt_api_planera_resa_web_v4_models_valid_time_interval_api_model import VTApiPlaneraResaWebV4ModelsValidTimeIntervalApiModel

