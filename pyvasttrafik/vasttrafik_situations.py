"""Enables retrival of disturbances in Västtrafik traffic."""
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


class TrafficSituations:
    def __init__(self, api_client=None):
        self.api_url = "https://ext-api.vasttrafik.se/ts/v1"
        self._api = Vasttrafik()
        self.configuration = self._api.configuration
        self.configuration.host = self.api_url

    def get_traffic_situations(self, **kwargs):  # noqa: E501
        objecttype = '/traffic-situations'

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
            200: "list[TrafficSituationApiModel]",
            400: None,
            500: None,
        }

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise Exception(
                    "Got an unexpected keyword argument '%s'"
                    " to method ts_v1_traffic_situations_get" % key
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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        traffic_situation = self._api.make_request(
            objecttype,
            query_params,
            header_params,
            body_params,
            response_types_map,
            auth_settings,
        )
        return traffic_situation

    def get_traffic_situations_number(self, **kwargs):  # noqa: E501
        objecttype = "/traffic-situations/{situationNumber}"

        local_var_params = locals()

        all_params = [
            'situation_number'
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
            200: "TrafficSituationApiModel",
            400: None,
            404: "str",
            500: None,
        }

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise Exception(
                    "Got an unexpected keyword argument '%s'"
                    " to method ts_v1_traffic_situations_by_situation_number_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}
        if 'situation_number' in local_var_params:
            path_params['situationNumber'] = local_var_params['situation_number']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self._api.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        traffic_situation = self._api.make_request(
            objecttype,
            query_params,
            header_params,
            body_params,
            response_types_map,
            auth_settings,
            path_params,
        )
        return traffic_situation

    def get_traffic_situations_line(self, **kwargs):  # noqa: E501
        objecttype = "/traffic-situations/line/{gid}"

        local_var_params = locals()

        all_params = [
            'gid'
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
            200: "list[TrafficSituationApiModel]",
            400: None,
            500: None,
        }

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise Exception(
                    "Got an unexpected keyword argument '%s'"
                    " to method ts_v1_traffic_situations_line_by_gid_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}
        if 'gid' in local_var_params:
            path_params['gid'] = local_var_params['gid']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self._api.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        traffic_situation_line = self._api.make_request(
            objecttype,
            query_params,
            header_params,
            body_params,
            response_types_map,
            auth_settings,
            path_params,
        )
        return traffic_situation_line

    def get_traffic_situations_stoppoint(self, **kwargs):  # noqa: E501
        objecttype = "/traffic-situations/stoppoint/{gid}"

        local_var_params = locals()

        all_params = [
            'gid'
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
            200: "list[TrafficSituationApiModel]",
            400: None,
            500: None,
        }

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise Exception(
                    "Got an unexpected keyword argument '%s'"
                    " to method ts_v1_traffic_situations_stoppoint_by_gid_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}
        if 'gid' in local_var_params:
            path_params['gid'] = local_var_params['gid']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self._api.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        traffic_situation_stoppoint = self._api.make_request(
            objecttype,
            query_params,
            header_params,
            body_params,
            response_types_map,
            auth_settings,
            path_params,
        )
        return traffic_situation_stoppoint

    def get_traffic_situations_stoparea(self, **kwargs):  # noqa: E501
        objecttype = "/traffic-situations/stoparea/{gid}"

        local_var_params = locals()

        all_params = [
            'gid'
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
            200: "list[TrafficSituationApiModel]",
            400: None,
            500: None,
        }

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise Exception(
                    "Got an unexpected keyword argument '%s'"
                    " to method ts_v1_traffic_situations_stoparea_by_gid_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}
        if 'gid' in local_var_params:
            path_params['gid'] = local_var_params['gid']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self._api.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        traffic_situation_stoparea = self._api.make_request(
            objecttype,
            query_params,
            header_params,
            body_params,
            response_types_map,
            auth_settings,
            path_params,
        )
        return traffic_situation_stoparea

    def get_traffic_situations_journey(self, **kwargs):  # noqa: E501
        objecttype = "/traffic-situations/journey/{gid}"

        local_var_params = locals()

        all_params = [
            'gid'
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
            200: "list[TrafficSituationApiModel]",
            400: None,
            500: None,
        }

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise Exception(
                    "Got an unexpected keyword argument '%s'"
                    " to method ts_v1_traffic_situations_journey_by_gid_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}
        if 'gid' in local_var_params:
            path_params['gid'] = local_var_params['gid']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self._api.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        traffic_situation_journey = self._api.make_request(
            objecttype,
            query_params,
            header_params,
            body_params,
            response_types_map,
            auth_settings,
            path_params,
        )
        return traffic_situation_journey
