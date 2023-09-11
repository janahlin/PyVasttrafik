"""Enables retrival of information for plan trips in Västtrafik traffic."""
from __future__ import annotations

from typing import Any

from datetime import datetime, timedelta
from enum import Enum

import aiohttp
import six

import pyvasttrafik.vasttrafik_main
import pyvasttrafik.api_models
from pyvasttrafik.vasttrafik_main import (
    FieldFilter,
    FieldSort,
    FilterOperation,
    OrFilter,
    SortOrder,
    Vasttrafik,
)

LOCATION_INFO_REQUIRED_FIELDS = ["q"]


class VasttrafikPlanTrip:
    """Class used to communicate with Västtrafik's plan api."""

    def __init__(self):
        """Initialize Vasttrafik object"""

        self.api_url = "https://ext-api.vasttrafik.se/pr/v4"
        self._api = Vasttrafik()
        self.configuration = self._api.configuration
        self.configuration.host = self.api_url

    def get_location_by_text(self, q, **kwargs):
        objecttype = '/locations/by-text'
        local_var_params = locals()
        all_params = [
            'q',
            'types',
            'limit',
            'offset'
        ]

        response_types_map = {
            200: "LocationsGetLocationsResponse",
            400: "Error",
            500: None,
            503: None,
        }

        collection_formats = {}
        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise Exception(
                    "Got an unexpected keyword argument '%s'"
                    " to method locations_by_text_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        query_params = []
        if local_var_params.get('q') is not None:  # noqa: E501
            query_params.append(('q', local_var_params['q']))  # noqa: E501
        if local_var_params.get('types') is not None:  # noqa: E501            )
            query_params.append(('types', local_var_params['types']))  # noqa: E501
            collection_formats['types'] = 'multi'  # noqa: E501
        if local_var_params.get('limit') is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if local_var_params.get('offset') is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501

        body_params = None
        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`

        header_params['Accept'] = self._api.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # print(header_params)
        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        location = self._api.make_request(
            objecttype,
            query_params,
            header_params,
            body_params,
            response_types_map,
            auth_settings,
        )
        return location

    def get_location_by_coordinates(self, latitude, longitude, **kwargs):
        objecttype = '/locations/by-coordinates'
        local_var_params = locals()

        all_params = [
            'latitude',
            'longitude',
            'radius_in_meters',
            'types',
            'limit',
            'offset'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        response_types_map = {
            200: "LocationsGetLocationsResponse",
            400: "Error",
            500: None,
            503: None,
        }

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise Exception(
                    "Got an unexpected keyword argument '%s'"
                    " to method locations_by_coordinates_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        if local_var_params.get('latitude') is not None:  # noqa: E501
            query_params.append(('latitude', local_var_params['latitude']))  # noqa: E501
        if local_var_params.get('longitude') is not None:  # noqa: E501
            query_params.append(('longitude', local_var_params['longitude']))  # noqa: E501
        if local_var_params.get('radius_in_meters') is not None:  # noqa: E501
            query_params.append(('radiusInMeters', local_var_params['radius_in_meters']))  # noqa: E501
        if local_var_params.get('types') is not None:  # noqa: E501
            query_params.append(('types', local_var_params['types']))  # noqa: E501
            collection_formats['types'] = 'multi'  # noqa: E501
        if local_var_params.get('limit') is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if local_var_params.get('offset') is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self._api.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        location = self._api.make_request(
            objecttype,
            query_params,
            header_params,
            body_params,
            response_types_map,
            auth_settings,
        )
        return location

    def get_journeys(self, **kwargs):
        objecttype = '/journeys'
        local_var_params = locals()

        all_params = [
            'origin_gid',
            'origin_name',
            'origin_latitude',
            'origin_longitude',
            'destination_gid',
            'destination_name',
            'destination_latitude',
            'destination_longitude',
            'date_time',
            'date_time_relates_to',
            'pagination_reference',
            'limit',
            'transport_modes',
            'transport_sub_modes',
            'only_direct_connections',
            'include_nearby_stop_areas',
            'via_gid',
            'origin_walk',
            'dest_walk',
            'origin_bike',
            'dest_bike',
            'total_bike',
            'origin_car',
            'dest_car',
            'origin_park',
            'dest_park',
            'interchange_duration_in_minutes',
            'include_occupancy'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        response_types_map = {
            200: "JourneysGetJourneysResponse",
            400: "Error",
            500: None,
            503: None,
        }

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise Exception(
                    "Got an unexpected keyword argument '%s'"
                    " to method journeys_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if local_var_params.get('origin_gid') is not None:  # noqa: E501
            query_params.append(('originGid', local_var_params['origin_gid']))  # noqa: E501
        if local_var_params.get('origin_name') is not None:  # noqa: E501
            query_params.append(('originName', local_var_params['origin_name']))  # noqa: E501
        if local_var_params.get('origin_latitude') is not None:  # noqa: E501
            query_params.append(('originLatitude', local_var_params['origin_latitude']))  # noqa: E501
        if local_var_params.get('origin_longitude') is not None:  # noqa: E501
            query_params.append(('originLongitude', local_var_params['origin_longitude']))  # noqa: E501
        if local_var_params.get('destination_gid') is not None:  # noqa: E501
            query_params.append(('destinationGid', local_var_params['destination_gid']))  # noqa: E501
        if local_var_params.get('destination_name') is not None:  # noqa: E501
            query_params.append(('destinationName', local_var_params['destination_name']))  # noqa: E501
        if local_var_params.get('destination_latitude') is not None:  # noqa: E501
            query_params.append(('destinationLatitude', local_var_params['destination_latitude']))  # noqa: E501
        if local_var_params.get('destination_longitude') is not None:  # noqa: E501
            query_params.append(('destinationLongitude', local_var_params['destination_longitude']))  # noqa: E501
        if local_var_params.get('date_time') is not None:  # noqa: E501
            query_params.append(('dateTime', local_var_params['date_time']))  # noqa: E501
        if local_var_params.get('date_time_relates_to') is not None:  # noqa: E501
            query_params.append(('dateTimeRelatesTo', local_var_params['date_time_relates_to']))  # noqa: E501
        if local_var_params.get('pagination_reference') is not None:  # noqa: E501
            query_params.append(('paginationReference', local_var_params['pagination_reference']))  # noqa: E501
        if local_var_params.get('limit') is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if local_var_params.get('transport_modes') is not None:  # noqa: E501
            query_params.append(('transportModes', local_var_params['transport_modes']))  # noqa: E501
            collection_formats['transportModes'] = 'multi'  # noqa: E501
        if local_var_params.get('transport_sub_modes') is not None:  # noqa: E501
            query_params.append(('transportSubModes', local_var_params['transport_sub_modes']))  # noqa: E501
            collection_formats['transportSubModes'] = 'multi'  # noqa: E501
        if local_var_params.get('only_direct_connections') is not None:  # noqa: E501
            query_params.append(('onlyDirectConnections', local_var_params['only_direct_connections']))  # noqa: E501
        if local_var_params.get('include_nearby_stop_areas') is not None:  # noqa: E501
            query_params.append(('includeNearbyStopAreas', local_var_params['include_nearby_stop_areas']))  # noqa: E501
        if local_var_params.get('via_gid') is not None:  # noqa: E501
            query_params.append(('viaGid', local_var_params['via_gid']))  # noqa: E501
        if local_var_params.get('origin_walk') is not None:  # noqa: E501
            query_params.append(('originWalk', local_var_params['origin_walk']))  # noqa: E501
        if local_var_params.get('dest_walk') is not None:  # noqa: E501
            query_params.append(('destWalk', local_var_params['dest_walk']))  # noqa: E501
        if local_var_params.get('origin_bike') is not None:  # noqa: E501
            query_params.append(('originBike', local_var_params['origin_bike']))  # noqa: E501
        if local_var_params.get('dest_bike') is not None:  # noqa: E501
            query_params.append(('destBike', local_var_params['dest_bike']))  # noqa: E501
        if local_var_params.get('total_bike') is not None:  # noqa: E501
            query_params.append(('totalBike', local_var_params['total_bike']))  # noqa: E501
        if local_var_params.get('origin_car') is not None:  # noqa: E501
            query_params.append(('originCar', local_var_params['origin_car']))  # noqa: E501
        if local_var_params.get('dest_car') is not None:  # noqa: E501
            query_params.append(('destCar', local_var_params['dest_car']))  # noqa: E501
        if local_var_params.get('origin_park') is not None:  # noqa: E501
            query_params.append(('originPark', local_var_params['origin_park']))  # noqa: E501
        if local_var_params.get('dest_park') is not None:  # noqa: E501
            query_params.append(('destPark', local_var_params['dest_park']))  # noqa: E501
        if local_var_params.get('interchange_duration_in_minutes') is not None:  # noqa: E501
            query_params.append(
                ('interchangeDurationInMinutes', local_var_params['interchange_duration_in_minutes']))  # noqa: E501
        if local_var_params.get('include_occupancy') is not None:  # noqa: E501
            query_params.append(('includeOccupancy', local_var_params['include_occupancy']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self._api.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        journey = self._api.make_request(
            objecttype,
            query_params,
            header_params,
            body_params,
            response_types_map,
            auth_settings,
        )
        return journey

    def journeys_reconstruct(self, **kwargs):
        objecttype = '/journeys/reconstruct'
        local_var_params = locals()

        all_params = [
            'ref',
            'include_occupancy'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        response_types_map = {
            200: "JourneysJourneyApiModel",
            400: "Error",
            500: None,
            503: None,
            404: None,
        }

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise Exception(
                    "Got an unexpected keyword argument '%s'"
                    " to method journeys_reconstruct_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if local_var_params.get('ref') is not None:  # noqa: E501
            query_params.append(('ref', local_var_params['ref']))  # noqa: E501
        if local_var_params.get('include_occupancy') is not None:  # noqa: E501
            query_params.append(('includeOccupancy', local_var_params['include_occupancy']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self._api.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        journey = self._api.make_request(
            objecttype,
            query_params,
            header_params,
            body_params,
            response_types_map,
            auth_settings,
        )
        return journey

    def get_journeys_details(self, details_reference, **kwargs):
        objecttype = "/journeys/{detailsReference}/details"

        local_var_params = locals()

        all_params = [
            'details_reference',
            'includes',
            'channel_ids',
            'product_types',
            'traveller_categories'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        response_types_map = {
            200: "JourneyDetailsJourneyDetailsApiModel",
            400: "Error",
            404: "MicrosoftAspNetCoreMvcProblemDetails",
            500: None,
            503: None,
        }

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise Exception(
                    "Got an unexpected keyword argument '%s'"
                    " to method journeys_details_reference_details_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'details_reference' is set
        # if self.api_client.client_side_validation and local_var_params.get('details_reference') is None:  # noqa: E501
        #    raise ApiValueError("Missing the required parameter `details_reference` when calling `journeys_details_reference_details_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'details_reference' in local_var_params:
            path_params['detailsReference'] = local_var_params['details_reference']  # noqa: E501

        query_params = []
        if local_var_params.get('includes') is not None:  # noqa: E501
            query_params.append(('includes', local_var_params['includes']))  # noqa: E501
            collection_formats['includes'] = 'multi'  # noqa: E501
        if local_var_params.get('channel_ids') is not None:  # noqa: E501
            query_params.append(('channelIds', local_var_params['channel_ids']))  # noqa: E501
            collection_formats['channelIds'] = 'multi'  # noqa: E501
        if local_var_params.get('product_types') is not None:  # noqa: E501
            query_params.append(('productTypes', local_var_params['product_types']))  # noqa: E501
            collection_formats['productTypes'] = 'multi'  # noqa: E501
        if local_var_params.get('traveller_categories') is not None:  # noqa: E501
            query_params.append(('travellerCategories', local_var_params['traveller_categories']))  # noqa: E501
            collection_formats['travellerCategories'] = 'multi'  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self._api.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        journey_details = self._api.make_request(
            objecttype,
            query_params,
            header_params,
            body_params,
            response_types_map,
            auth_settings,
            path_params,
        )
        return journey_details

    def get_journeys_valid_time_interval(self, **kwargs):
        objecttype = "/journeys/valid-time-interval"

        local_var_params = locals()

        all_params = [
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        response_types_map = {
            200: "ValidTimeIntervalApiModel",
            404: "MicrosoftAspNetCoreMvcProblemDetails",
            500: None,
            503: None,
        }

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise Exception(
                    "Got an unexpected keyword argument '%s'"
                    " to method journeys_valid_time_interval_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self._api.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        valid_time_interval = self._api.make_request(
            objecttype,
            query_params,
            header_params,
            body_params,
            response_types_map,
            auth_settings,
            path_params,
        )
        return valid_time_interval

    def get_positions(self, lower_left_lat, lower_left_long, upper_right_lat, upper_right_long, **kwargs):
        objecttype = "/positions"

        local_var_params = locals()

        all_params = [
            'lower_left_lat',
            'lower_left_long',
            'upper_right_lat',
            'upper_right_long',
            'transport_modes',
            'details_references',
            'line_designations',
            'limit'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        response_types_map = {
            200: "list[PositionsJourneyPositionApiModel]",
            400: "Error",
            500: None,
            503: None,
        }

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise Exception(
                    "Got an unexpected keyword argument '%s'"
                    " to method positions_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if local_var_params.get('lower_left_lat') is not None:  # noqa: E501
            query_params.append(('lowerLeftLat', local_var_params['lower_left_lat']))  # noqa: E501
        if local_var_params.get('lower_left_long') is not None:  # noqa: E501
            query_params.append(('lowerLeftLong', local_var_params['lower_left_long']))  # noqa: E501
        if local_var_params.get('upper_right_lat') is not None:  # noqa: E501
            query_params.append(('upperRightLat', local_var_params['upper_right_lat']))  # noqa: E501
        if local_var_params.get('upper_right_long') is not None:  # noqa: E501
            query_params.append(('upperRightLong', local_var_params['upper_right_long']))  # noqa: E501
        if local_var_params.get('transport_modes') is not None:  # noqa: E501
            query_params.append(('transportModes', local_var_params['transport_modes']))  # noqa: E501
            collection_formats['transportModes'] = 'multi'  # noqa: E501
        if local_var_params.get('details_references') is not None:  # noqa: E501
            query_params.append(('detailsReferences', local_var_params['details_references']))  # noqa: E501
            collection_formats['detailsReferences'] = 'multi'  # noqa: E501
        if local_var_params.get('line_designations') is not None:  # noqa: E501
            query_params.append(('lineDesignations', local_var_params['line_designations']))  # noqa: E501
            collection_formats['lineDesignations'] = 'multi'  # noqa: E501
        if local_var_params.get('limit') is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self._api.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        positions = self._api.make_request(
            objecttype,
            query_params,
            header_params,
            body_params,
            response_types_map,
            auth_settings,
            path_params,
        )
        return positions

    def get_stop_areas_departures_by_gid(self, stop_area_gid, **kwargs):
        objecttype = "/stop-areas/{stopAreaGid}/departures"

        local_var_params = locals()

        all_params = [
            'stop_area_gid',
            'start_date_time',
            'platforms',
            'time_span_in_minutes',
            'max_departures_per_line_and_direction',
            'limit',
            'offset',
            'include_occupancy'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        response_types_map = {
            200: "DeparturesAndArrivalsGetDeparturesResponse",
            400: "Error",
            404: "MicrosoftAspNetCoreMvcProblemDetails",
            500: None,
            503: None,
        }

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise Exception(
                    "Got an unexpected keyword argument '%s'"
                    " to method stop_areas_stop_area_gid_departures_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}
        if 'stop_area_gid' in local_var_params:
            path_params['stopAreaGid'] = local_var_params['stop_area_gid']  # noqa: E501

        query_params = []
        if local_var_params.get('start_date_time') is not None:  # noqa: E501
            query_params.append(('startDateTime', local_var_params['start_date_time']))  # noqa: E501
        if local_var_params.get('platforms') is not None:  # noqa: E501
            query_params.append(('platforms', local_var_params['platforms']))  # noqa: E501
        if local_var_params.get('time_span_in_minutes') is not None:  # noqa: E501
            query_params.append(('timeSpanInMinutes', local_var_params['time_span_in_minutes']))  # noqa: E501
        if local_var_params.get('max_departures_per_line_and_direction') is not None:  # noqa: E501
            query_params.append(('maxDeparturesPerLineAndDirection',
                                 local_var_params['max_departures_per_line_and_direction']))  # noqa: E501
        if local_var_params.get('limit') is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if local_var_params.get('offset') is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if local_var_params.get('include_occupancy') is not None:  # noqa: E501
            query_params.append(('includeOccupancy', local_var_params['include_occupancy']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self._api.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        departure_area = self._api.make_request(
            objecttype,
            query_params,
            header_params,
            body_params,
            response_types_map,
            auth_settings,
            path_params,
        )
        return departure_area

    def get_stop_areas_arrivals_by_gid(self, stop_area_gid, **kwargs):
        objecttype = "/stop-areas/{stopAreaGid}/arrivals"

        local_var_params = locals()

        all_params = [
            'stop_area_gid',
            'start_date_time',
            'platforms',
            'time_span_in_minutes',
            'max_arrivals_per_line_and_direction',
            'limit',
            'offset'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        response_types_map = {
            200: "DeparturesAndArrivalsGetArrivalsResponse",
            400: "Error",
            404: "MicrosoftAspNetCoreMvcProblemDetails",
            500: None,
            503: None,
        }

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise Exception(
                    "Got an unexpected keyword argument '%s'"
                    " to method stop_areas_stop_area_gid_arrivals_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}
        if 'stop_area_gid' in local_var_params:
            path_params['stopAreaGid'] = local_var_params['stop_area_gid']  # noqa: E501

        query_params = []
        if local_var_params.get('start_date_time') is not None:  # noqa: E501
            query_params.append(('startDateTime', local_var_params['start_date_time']))  # noqa: E501
        if local_var_params.get('platforms') is not None:  # noqa: E501
            query_params.append(('platforms', local_var_params['platforms']))  # noqa: E501
        if local_var_params.get('time_span_in_minutes') is not None:  # noqa: E501
            query_params.append(('timeSpanInMinutes', local_var_params['time_span_in_minutes']))  # noqa: E501
        if local_var_params.get('max_arrivals_per_line_and_direction') is not None:  # noqa: E501
            query_params.append(('maxArrivalsPerLineAndDirection',
                                 local_var_params['max_arrivals_per_line_and_direction']))  # noqa: E501
        if local_var_params.get('limit') is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if local_var_params.get('offset') is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self._api.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        arrival_area = self._api.make_request(
            objecttype,
            query_params,
            header_params,
            body_params,
            response_types_map,
            auth_settings,
            path_params,
        )
        return arrival_area

    def get_stop_areas_departures_by_gid_details(self, details_reference, stop_area_gid, **kwargs):
        objecttype = "/stop-areas/{stopAreaGid}/departures/{detailsReference}/details"

        local_var_params = locals()

        all_params = [
            'details_reference',
            'stop_area_gid',
            'includes'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        response_types_map = {
            200: "DeparturesAndArrivalsDepartureDetailsApiModel",
            400: "Error",
            404: "MicrosoftAspNetCoreMvcProblemDetails",
            500: None,
            503: None,
        }

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise Exception(
                    "Got an unexpected keyword argument '%s'"
                    " to method stop_areas_stop_area_gid_departures_details_reference_details_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}
        if 'details_reference' in local_var_params:
            path_params['detailsReference'] = local_var_params['details_reference']  # noqa: E501
        if 'stop_area_gid' in local_var_params:
            path_params['stopAreaGid'] = local_var_params['stop_area_gid']  # noqa: E501

        query_params = []
        if local_var_params.get('includes') is not None:  # noqa: E501
            query_params.append(('includes', local_var_params['includes']))  # noqa: E501
            collection_formats['includes'] = 'multi'  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self._api.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        departure_area_detail = self._api.make_request(
            objecttype,
            query_params,
            header_params,
            body_params,
            response_types_map,
            auth_settings,
            path_params,
        )
        return departure_area_detail

    def get_stop_areas_arrivals_by_gid_details(self, details_reference, stop_area_gid, **kwargs):
        objecttype = "/stop-areas/{stopAreaGid}/arrivals/{detailsReference}/details"

        local_var_params = locals()

        all_params = [
            'details_reference',
            'stop_area_gid',
            'includes'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        response_types_map = {
            200: "DeparturesAndArrivalsArrivalsDetailsApiModel",
            400: "Error",
            404: "MicrosoftAspNetCoreMvcProblemDetails",
            500: None,
            503: None,
        }

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise Exception(
                    "Got an unexpected keyword argument '%s'"
                    " to method stop_areas_stop_area_gid_departures_details_reference_details_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}
        if 'details_reference' in local_var_params:
            path_params['detailsReference'] = local_var_params['details_reference']  # noqa: E501
        if 'stop_area_gid' in local_var_params:
            path_params['stopAreaGid'] = local_var_params['stop_area_gid']  # noqa: E501

        query_params = []
        if local_var_params.get('includes') is not None:  # noqa: E501
            query_params.append(('includes', local_var_params['includes']))  # noqa: E501
            collection_formats['includes'] = 'multi'  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self._api.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        arrivals_area_detail = self._api.make_request(
            objecttype,
            query_params,
            header_params,
            body_params,
            response_types_map,
            auth_settings,
            path_params,
        )
        return arrivals_area_detail

    def get_stop_points_departures(self, stop_point_gid, **kwargs):
        objecttype = "/stop-points/{stopPointGid}/departures"

        local_var_params = locals()

        all_params = [
            'stop_point_gid',
            'start_date_time',
            'time_span_in_minutes',
            'max_departures_per_line_and_direction',
            'limit',
            'offset',
            'include_occupancy'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        response_types_map = {
            200: "DeparturesAndArrivalsGetDeparturesResponse",
            400: "Error",
            404: "MicrosoftAspNetCoreMvcProblemDetails",
            500: None,
            503: None,
        }

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise Exception(
                    "Got an unexpected keyword argument '%s'"
                    " to method stop_points_stop_point_gid_departures_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}
        if 'stop_point_gid' in local_var_params:
            path_params['stopPointGid'] = local_var_params['stop_point_gid']  # noqa: E501

        query_params = []
        if local_var_params.get('start_date_time') is not None:  # noqa: E501
            query_params.append(('startDateTime', local_var_params['start_date_time']))  # noqa: E501
        if local_var_params.get('time_span_in_minutes') is not None:  # noqa: E501
            query_params.append(('timeSpanInMinutes', local_var_params['time_span_in_minutes']))  # noqa: E501
        if local_var_params.get('max_departures_per_line_and_direction') is not None:  # noqa: E501
            query_params.append(('maxDeparturesPerLineAndDirection',
                                 local_var_params['max_departures_per_line_and_direction']))  # noqa: E501
        if local_var_params.get('limit') is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if local_var_params.get('offset') is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if local_var_params.get('include_occupancy') is not None:  # noqa: E501
            query_params.append(('includeOccupancy', local_var_params['include_occupancy']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self._api.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        departure_stop_point = self._api.make_request(
            objecttype,
            query_params,
            header_params,
            body_params,
            response_types_map,
            auth_settings,
            path_params,
        )
        return departure_stop_point

    def get_stop_points_arrivals(self, stop_point_gid, **kwargs):
        objecttype = "/stop-points/{stopPointGid}/arrivals"

        local_var_params = locals()

        all_params = [
            'stop_point_gid',
            'start_date_time',
            'time_span_in_minutes',
            'max_departures_per_line_and_direction',
            'limit',
            'offset',
            'include_occupancy'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        response_types_map = {
            200: "DeparturesAndArrivalsGetArrivalsResponse",
            400: "Error",
            404: "MicrosoftAspNetCoreMvcProblemDetails",
            500: None,
            503: None,
        }

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise Exception(
                    "Got an unexpected keyword argument '%s'"
                    " to method stop_points_stop_point_gid_arrivals_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}
        if 'stop_point_gid' in local_var_params:
            path_params['stopPointGid'] = local_var_params['stop_point_gid']  # noqa: E501

        query_params = []
        if local_var_params.get('start_date_time') is not None:  # noqa: E501
            query_params.append(('startDateTime', local_var_params['start_date_time']))  # noqa: E501
        if local_var_params.get('time_span_in_minutes') is not None:  # noqa: E501
            query_params.append(('timeSpanInMinutes', local_var_params['time_span_in_minutes']))  # noqa: E501
        if local_var_params.get('max_arrivals_per_line_and_direction') is not None:  # noqa: E501
            query_params.append(('maxArrivalsPerLineAndDirection',
                                 local_var_params['max_arrivals_per_line_and_direction']))  # noqa: E501
        if local_var_params.get('limit') is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if local_var_params.get('offset') is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self._api.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        arrival_stop_point = self._api.make_request(
            objecttype,
            query_params,
            header_params,
            body_params,
            response_types_map,
            auth_settings,
            path_params,
        )
        return arrival_stop_point

    def get_stop_point_departures_by_gid_details(self, details_reference, stop_point_gid, **kwargs):
        objecttype = "/stop-points/{stopPointGid}/departures/{detailsReference}/details"

        local_var_params = locals()

        all_params = [
            'details_reference',
            'stop_point_gid',
            'includes'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        response_types_map = {
            200: "DeparturesAndArrivalsDepartureDetailsApiModel",
            400: "ApiError",
            404: "MicrosoftAspNetCoreMvcProblemDetails",
            500: None,
            503: None,
        }

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise Exception(
                    "Got an unexpected keyword argument '%s'"
                    " to method stop_points_stop_point_gid_departures_details_reference_details_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}
        if 'details_reference' in local_var_params:
            path_params['detailsReference'] = local_var_params['details_reference']  # noqa: E501
        if 'stop_point_gid' in local_var_params:
            path_params['stopPointGid'] = local_var_params['stop_point_gid']  # noqa: E501

        query_params = []
        if local_var_params.get('includes') is not None:  # noqa: E501
            query_params.append(('includes', local_var_params['includes']))  # noqa: E501
            collection_formats['includes'] = 'multi'  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self._api.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        departure_point_detail = self._api.make_request(
            objecttype,
            query_params,
            header_params,
            body_params,
            response_types_map,
            auth_settings,
            path_params,
        )
        return departure_point_detail

    def get_stop_point_arrivals_by_gid_details(self, details_reference, stop_point_gid, **kwargs):
        objecttype = "/stop-points/{stopPointGid}/arrivals/{detailsReference}/details"

        local_var_params = locals()

        all_params = [
            'details_reference',
            'stop_point_gid',
            'includes'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        response_types_map = {
            200: "DeparturesAndArrivalsArrivalDetailsApiModel",
            400: "Error",
            404: "MicrosoftAspNetCoreMvcProblemDetails",
            500: None,
            503: None,
        }

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise Exception(
                    "Got an unexpected keyword argument '%s'"
                    " to method stop_points_stop_point_gid_arrivals_details_reference_details_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}
        if 'details_reference' in local_var_params:
            path_params['detailsReference'] = local_var_params['details_reference']  # noqa: E501
        if 'stop_point_gid' in local_var_params:
            path_params['stopPointGid'] = local_var_params['stop_point_gid']  # noqa: E501

        query_params = []
        if local_var_params.get('includes') is not None:  # noqa: E501
            query_params.append(('includes', local_var_params['includes']))  # noqa: E501
            collection_formats['includes'] = 'multi'  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self._api.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        arrival_point_detail = self._api.make_request(
            objecttype,
            query_params,
            header_params,
            body_params,
            response_types_map,
            auth_settings,
            path_params,
        )
        return arrival_point_detail
