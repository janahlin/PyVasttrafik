# coding: utf-8
import base64
import requests
import six

from pyvasttrafik.api.api_client import ApiClient
from pyvasttrafik.api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


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


class Reseplaneraren:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        # if type(auth) != Auth:
        #    raise TypeError("Expected Auth object")
        # self.auth = auth
        # self.url = "https://ext-api.vasttrafik.se/pr/v4"

    def locations_by_coordinates_get(self, latitude, longitude, **kwargs):
        """Returns the locations nearest the specified coordinates. Currently only stop areas, stop points and meta-stations are supported.  # noqa: E501

                Sample request:        GET /locations/by-coordinates?latitude=57.708734&longitude=11.974764&radiusInMeters=500&limit=10&offset=0  # noqa: E501
                This method makes a synchronous HTTP request by default. To make an
                asynchronous HTTP request, please pass async_req=True

                >>> thread = Reseplaneraren.locations_by_coordinates_get(latitude, longitude, async_req=True)
                >>> result = thread.get()

                :param kwargs:
                :return:
                :param latitude: The latitude. (required)
                :type latitude: float
                :param longitude: The longitude. (required)
                :type longitude: float
                :param radius_in_meters: The search radius from the coordinates specified in meters. Must be a positive integer > 0.
                :type radius_in_meters: int
                :param types: The location types to include in the response, if none specified all locations types are included.
                :type types: list[VTApiPlaneraResaWebV4ModelsLocationByCoordinatesType]
                :param limit: The number of results to return.
                :type limit: int
                :param offset: The zero-based start offset of the pagination.
                :type offset: int
                :param async_req: Whether to execute the request asynchronously.
                :type async_req: bool, optional
                :param _preload_content: if False, the urllib3.HTTPResponse object will
                                         be returned without reading/decoding response
                                         data. Default is True.
                :type _preload_content: bool, optional
                :param _request_timeout: timeout setting for this request. If one
                                         number provided, it will be total request
                                         timeout. It can also be a pair (tuple) of
                                         (connection, read) timeouts.
                :return: Returns the result object.
                         If the method is called asynchronously,
                         returns the request thread.
                :rtype: VTApiPlaneraResaWebV4ModelsLocationsGetLocationsResponse
                """
        kwargs['_return_http_data_only'] = True

        return self.locations_by_coordinates_get_with_http_info(latitude, longitude, **kwargs)  # noqa: E501

    def locations_by_coordinates_get_with_http_info(self, latitude, longitude, **kwargs):  # noqa: E501
        """Returns the locations nearest the specified coordinates. Currently only stop areas, stop points and meta-stations are supported.  # noqa: E501

        Sample request:        GET /locations/by-coordinates?latitude=57.708734&longitude=11.974764&radiusInMeters=500&limit=10&offset=0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = Reseplaneraren.locations_by_coordinates_get_with_http_info(latitude, longitude, async_req=True)
        >>> result = thread.get()

        :param latitude: The latitude. (required)
        :type latitude: float
        :param longitude: The longitude. (required)
        :type longitude: float
        :param radius_in_meters: The search radius from the coordinates specified in meters. Must be a positive integer > 0.
        :type radius_in_meters: int
        :param types: The location types to include in the response, if none specified all locations types are included.
        :type types: list[VTApiPlaneraResaWebV4ModelsLocationByCoordinatesType]
        :param limit: The number of results to return.
        :type limit: int
        :param offset: The zero-based start offset of the pagination.
        :type offset: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(VTApiPlaneraResaWebV4ModelsLocationsGetLocationsResponse, status_code(int), headers(HTTPHeaderDict))
        """

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

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method locations_by_coordinates_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'latitude' is set
        if self.api_client.client_side_validation and local_var_params.get('latitude') is None:  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `latitude` when calling `locations_by_coordinates_get`")  # noqa: E501
        # verify the required parameter 'longitude' is set
        if self.api_client.client_side_validation and local_var_params.get('longitude') is None:  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `longitude` when calling `locations_by_coordinates_get`")  # noqa: E501

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
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        response_types_map = {
            200: "VTApiPlaneraResaWebV4ModelsLocationsGetLocationsResponse",
            400: "VTApiPlaneraResaWebV4ModelsApiError",
            500: None,
            503: None,
        }

        return self.api_client.call_api(
            '/locations/by-coordinates', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def locations_by_text_get(self, q, **kwargs):
        """Returns locations matching the specified text. Currently only stop areas, addresses, points of interest and meta-stations are supported.  # noqa: E501

        Sample request:        GET /locations/by-text?q=brunnsparken&limit=10&offset=0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = Reseplaneraren.locations_by_text_get(q, async_req=True)
        >>> result = thread.get()

        :param q: The search text (e.g. 'brunn', 'cent' or 'Kungsgatan'). The maximum length allowed is 256 characters. (required)
        :type q: str
        :param types: The location types to include in the response, if none specified all locations types are included.
        :type types: list[VTApiPlaneraResaWebV4ModelsLocationByTextType]
        :param limit: The number of results to return.
        :type limit: int
        :param offset: The zero-based start offset of the pagination.
        :type offset: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: VTApiPlaneraResaWebV4ModelsLocationsGetLocationsResponse
        """

        kwargs['_return_http_data_only'] = True
        return self.locations_by_text_get_with_http_info(q, **kwargs)  # noqa: E501

    def locations_by_text_get_with_http_info(self, q, **kwargs):  # noqa: E501
        """Returns locations matching the specified text. Currently only stop areas, addresses, points of interest and meta-stations are supported.  # noqa: E501

        Sample request:        GET /locations/by-text?q=brunnsparken&limit=10&offset=0  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = Reseplaneraren.locations_by_text_get_with_http_info(q, async_req=True)
        >>> result = thread.get()

        :param q: The search text (e.g. 'brunn', 'cent' or 'Kungsgatan'). The maximum length allowed is 256 characters. (required)
        :type q: str
        :param types: The location types to include in the response, if none specified all locations types are included.
        :type types: list[VTApiPlaneraResaWebV4ModelsLocationByTextType]
        :param limit: The number of results to return.
        :type limit: int
        :param offset: The zero-based start offset of the pagination.
        :type offset: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(VTApiPlaneraResaWebV4ModelsLocationsGetLocationsResponse, status_code(int), headers(HTTPHeaderDict))
        """
        local_var_params = locals()

        all_params = [
            'q',
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

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method locations_by_text_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'q' is set
        if self.api_client.client_side_validation and local_var_params.get('q') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `q` when calling `locations_by_text_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if local_var_params.get('q') is not None:  # noqa: E501
            query_params.append(('q', local_var_params['q']))  # noqa: E501
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
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        response_types_map = {
            200: "VTApiPlaneraResaWebV4ModelsLocationsGetLocationsResponse",
            400: "VTApiPlaneraResaWebV4ModelsApiError",
            500: None,
            503: None,
        }

        return self.api_client.call_api(
            '/locations/by-text', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def positions_get(self, lower_left_lat, lower_left_long, upper_right_lat, upper_right_long, **kwargs):  # noqa: E501
        """Returns journey positions within a bounding box  # noqa: E501

        Sample request:        GET /positions?lowerLeftLat=57.721723&lowerLeftLong=12.011882&upperRightLat=57.737549&upperRightLong=12.039268&limit=100  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = Reseplaneraren.positions_get(lower_left_lat, lower_left_long, upper_right_lat, upper_right_long, async_req=True)
        >>> result = thread.get()

        :param lower_left_lat: Lower left latitude of bounding box. (required)
        :type lower_left_lat: float
        :param lower_left_long: Lower left longitude of bounding box. (required)
        :type lower_left_long: float
        :param upper_right_lat: Upper right latitude of bounding box. (required)
        :type upper_right_lat: float
        :param upper_right_long: Upper right longitude of bounding box. (required)
        :type upper_right_long: float
        :param transport_modes: The transport modes to include when searching for journeys, if none specified all transport modes are included.
        :type transport_modes: list[VTApiPlaneraResaCoreModelsPositionTransportMode]
        :param details_references: Filter journeys by one or more journey details reference.
        :type details_references: list[str]
        :param line_designations: Only journeys running the given lineDesignations (case sensitive) are part of the result.
        :type line_designations: list[str]
        :param limit: Maximum number of journeys in response. Range from 1 to 200. Defaults to 100
        :type limit: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: list[VTApiPlaneraResaWebV4ModelsPositionsJourneyPositionApiModel]
        """
        kwargs['_return_http_data_only'] = True
        return self.positions_get_with_http_info(lower_left_lat, lower_left_long, upper_right_lat, upper_right_long,
                                                 **kwargs)  # noqa: E501

    def positions_get_with_http_info(self, lower_left_lat, lower_left_long, upper_right_lat, upper_right_long,
                                     **kwargs):  # noqa: E501
        """Returns journey positions within a bounding box  # noqa: E501

        Sample request:        GET /positions?lowerLeftLat=57.721723&lowerLeftLong=12.011882&upperRightLat=57.737549&upperRightLong=12.039268&limit=100  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = Reseplaneraren.positions_get_with_http_info(lower_left_lat, lower_left_long, upper_right_lat, upper_right_long, async_req=True)
        >>> result = thread.get()

        :param lower_left_lat: Lower left latitude of bounding box. (required)
        :type lower_left_lat: float
        :param lower_left_long: Lower left longitude of bounding box. (required)
        :type lower_left_long: float
        :param upper_right_lat: Upper right latitude of bounding box. (required)
        :type upper_right_lat: float
        :param upper_right_long: Upper right longitude of bounding box. (required)
        :type upper_right_long: float
        :param transport_modes: The transport modes to include when searching for journeys, if none specified all transport modes are included.
        :type transport_modes: list[VTApiPlaneraResaCoreModelsPositionTransportMode]
        :param details_references: Filter journeys by one or more journey details reference.
        :type details_references: list[str]
        :param line_designations: Only journeys running the given lineDesignations (case sensitive) are part of the result.
        :type line_designations: list[str]
        :param limit: Maximum number of journeys in response. Range from 1 to 200. Defaults to 100
        :type limit: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(list[VTApiPlaneraResaWebV4ModelsPositionsJourneyPositionApiModel], status_code(int), headers(HTTPHeaderDict))
        """

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

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method positions_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'lower_left_lat' is set
        if self.api_client.client_side_validation and local_var_params.get('lower_left_lat') is None:  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `lower_left_lat` when calling `positions_get`")  # noqa: E501
        # verify the required parameter 'lower_left_long' is set
        if self.api_client.client_side_validation and local_var_params.get('lower_left_long') is None:  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `lower_left_long` when calling `positions_get`")  # noqa: E501
        # verify the required parameter 'upper_right_lat' is set
        if self.api_client.client_side_validation and local_var_params.get('upper_right_lat') is None:  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `upper_right_lat` when calling `positions_get`")  # noqa: E501
        # verify the required parameter 'upper_right_long' is set
        if self.api_client.client_side_validation and local_var_params.get('upper_right_long') is None:  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `upper_right_long` when calling `positions_get`")  # noqa: E501

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
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        response_types_map = {
            200: "list[VTApiPlaneraResaWebV4ModelsPositionsJourneyPositionApiModel]",
            400: "VTApiPlaneraResaWebV4ModelsApiError",
            500: None,
            503: None,
        }

        return self.api_client.call_api(
            '/positions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def stop_areas_stop_area_gid_arrivals_details_reference_details_get(self, details_reference, stop_area_gid,
                                                                        **kwargs):  # noqa: E501
        """Returns details about an arrival.  # noqa: E501

        Sample request:        GET /stop-areas/9021014001760000/arrivals/{detailsReference}/details?includes=servicejourneycalls  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = Reseplaneraren.stop_areas_stop_area_gid_arrivals_details_reference_details_get(details_reference, stop_area_gid, async_req=True)
        >>> result = thread.get()

        :param details_reference: The reference to the service journey, received from the arrivals call. A detailsReference is only valid during the same day as it was generated. (required)
        :type details_reference: str
        :param stop_area_gid: (required)
        :type stop_area_gid: str
        :param includes: The additional information to include in the response.
        :type includes: list[VTApiPlaneraResaWebV4ModelsArrivalDetailsIncludeType]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsArrivalDetailsApiModel
        """
        kwargs['_return_http_data_only'] = True
        return self.stop_areas_stop_area_gid_arrivals_details_reference_details_get_with_http_info(details_reference,
                                                                                                   stop_area_gid,
                                                                                                   **kwargs)  # noqa: E501

    def stop_areas_stop_area_gid_arrivals_details_reference_details_get_with_http_info(self, details_reference,
                                                                                       stop_area_gid,
                                                                                       **kwargs):  # noqa: E501
        """Returns details about an arrival.  # noqa: E501

        Sample request:        GET /stop-areas/9021014001760000/arrivals/{detailsReference}/details?includes=servicejourneycalls  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = Reseplaneraren.stop_areas_stop_area_gid_arrivals_details_reference_details_get_with_http_info(details_reference, stop_area_gid, async_req=True)
        >>> result = thread.get()

        :param details_reference: The reference to the service journey, received from the arrivals call. A detailsReference is only valid during the same day as it was generated. (required)
        :type details_reference: str
        :param stop_area_gid: (required)
        :type stop_area_gid: str
        :param includes: The additional information to include in the response.
        :type includes: list[VTApiPlaneraResaWebV4ModelsArrivalDetailsIncludeType]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsArrivalDetailsApiModel, status_code(int), headers(HTTPHeaderDict))
        """

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

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stop_areas_stop_area_gid_arrivals_details_reference_details_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'details_reference' is set
        if self.api_client.client_side_validation and local_var_params.get('details_reference') is None:  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `details_reference` when calling `stop_areas_stop_area_gid_arrivals_details_reference_details_get`")  # noqa: E501
        # verify the required parameter 'stop_area_gid' is set
        if self.api_client.client_side_validation and local_var_params.get('stop_area_gid') is None:  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `stop_area_gid` when calling `stop_areas_stop_area_gid_arrivals_details_reference_details_get`")  # noqa: E501

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
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        response_types_map = {
            200: "VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsArrivalDetailsApiModel",
            400: "VTApiPlaneraResaWebV4ModelsApiError",
            404: "MicrosoftAspNetCoreMvcProblemDetails",
            500: None,
            503: None,
        }

        return self.api_client.call_api(
            '/stop-areas/{stopAreaGid}/arrivals/{detailsReference}/details', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def stop_areas_stop_area_gid_arrivals_get(self, stop_area_gid, **kwargs):  # noqa: E501
        """Returns arrivals to the specified stop area at the specified time.  # noqa: E501

        Sample request:        GET /stop-areas/9021014003980000/arrivals  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = Reseplaneraren.stop_areas_stop_area_gid_arrivals_get(stop_area_gid, async_req=True)
        >>> result = thread.get()

        :param stop_area_gid: The 16-digit Västtrafik gid of the stop area. (required)
        :type stop_area_gid: str
        :param start_date_time: The start of the time interval for which to get upcoming arrivals. Must be specified in RFC 3339 format or be null which means that the current time on the server is used.
        :type start_date_time: datetime
        :param platforms: Filter results by platform. Multiple platforms are separated by comma. Case sensitive.
        :type platforms: str
        :param time_span_in_minutes: The number of minutes from the start time for which to get upcoming arrivals. Allowed values are between 0 and 1440.
        :type time_span_in_minutes: int
        :param max_arrivals_per_line_and_direction: The maximum number of arrivals for a single line in a specific direction.
        :type max_arrivals_per_line_and_direction: int
        :param limit: The number of results to return.
        :type limit: int
        :param offset: The zero-based start offset of the pagination.
        :type offset: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsGetArrivalsResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.stop_areas_stop_area_gid_arrivals_get_with_http_info(stop_area_gid, **kwargs)  # noqa: E501

    def stop_areas_stop_area_gid_arrivals_get_with_http_info(self, stop_area_gid, **kwargs):  # noqa: E501
        """Returns arrivals to the specified stop area at the specified time.  # noqa: E501

        Sample request:        GET /stop-areas/9021014003980000/arrivals  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = Reseplaneraren.stop_areas_stop_area_gid_arrivals_get_with_http_info(stop_area_gid, async_req=True)
        >>> result = thread.get()

        :param stop_area_gid: The 16-digit Västtrafik gid of the stop area. (required)
        :type stop_area_gid: str
        :param start_date_time: The start of the time interval for which to get upcoming arrivals. Must be specified in RFC 3339 format or be null which means that the current time on the server is used.
        :type start_date_time: datetime
        :param platforms: Filter results by platform. Multiple platforms are separated by comma. Case sensitive.
        :type platforms: str
        :param time_span_in_minutes: The number of minutes from the start time for which to get upcoming arrivals. Allowed values are between 0 and 1440.
        :type time_span_in_minutes: int
        :param max_arrivals_per_line_and_direction: The maximum number of arrivals for a single line in a specific direction.
        :type max_arrivals_per_line_and_direction: int
        :param limit: The number of results to return.
        :type limit: int
        :param offset: The zero-based start offset of the pagination.
        :type offset: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsGetArrivalsResponse, status_code(int), headers(HTTPHeaderDict))
        """

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

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stop_areas_stop_area_gid_arrivals_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'stop_area_gid' is set
        if self.api_client.client_side_validation and local_var_params.get('stop_area_gid') is None:  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `stop_area_gid` when calling `stop_areas_stop_area_gid_arrivals_get`")  # noqa: E501

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
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        response_types_map = {
            200: "VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsGetArrivalsResponse",
            400: "VTApiPlaneraResaWebV4ModelsApiError",
            404: "MicrosoftAspNetCoreMvcProblemDetails",
            500: None,
            503: None,
        }

        return self.api_client.call_api(
            '/stop-areas/{stopAreaGid}/arrivals', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def stop_areas_stop_area_gid_departures_details_reference_details_get(self, details_reference, stop_area_gid,
                                                                          **kwargs):  # noqa: E501
        """Returns details about a departure.  # noqa: E501

        Sample request:        GET /stop-areas/9021014001760000/departures/{detailsReference}/details?includes=servicejourneycalls  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = Reseplaneraren.stop_areas_stop_area_gid_departures_details_reference_details_get(details_reference, stop_area_gid, async_req=True)
        >>> result = thread.get()

        :param details_reference: The reference to the service journey, received from the departures call. A detailsReference is only valid during the same day as it was generated. (required)
        :type details_reference: str
        :param stop_area_gid: (required)
        :type stop_area_gid: str
        :param includes: The additional information to include in the response.
        :type includes: list[VTApiPlaneraResaWebV4ModelsDepartureDetailsIncludeType]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsDepartureDetailsApiModel
        """
        kwargs['_return_http_data_only'] = True
        return self.stop_areas_stop_area_gid_departures_details_reference_details_get_with_http_info(details_reference,
                                                                                                     stop_area_gid,
                                                                                                     **kwargs)  # noqa: E501

    def stop_areas_stop_area_gid_departures_details_reference_details_get_with_http_info(self, details_reference,
                                                                                         stop_area_gid,
                                                                                         **kwargs):  # noqa: E501
        """Returns details about a departure.  # noqa: E501

        Sample request:        GET /stop-areas/9021014001760000/departures/{detailsReference}/details?includes=servicejourneycalls  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = Reseplaneraren.stop_areas_stop_area_gid_departures_details_reference_details_get_with_http_info(details_reference, stop_area_gid, async_req=True)
        >>> result = thread.get()

        :param details_reference: The reference to the service journey, received from the departures call. A detailsReference is only valid during the same day as it was generated. (required)
        :type details_reference: str
        :param stop_area_gid: (required)
        :type stop_area_gid: str
        :param includes: The additional information to include in the response.
        :type includes: list[VTApiPlaneraResaWebV4ModelsDepartureDetailsIncludeType]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsDepartureDetailsApiModel, status_code(int), headers(HTTPHeaderDict))
        """

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

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stop_areas_stop_area_gid_departures_details_reference_details_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'details_reference' is set
        if self.api_client.client_side_validation and local_var_params.get('details_reference') is None:  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `details_reference` when calling `stop_areas_stop_area_gid_departures_details_reference_details_get`")  # noqa: E501
        # verify the required parameter 'stop_area_gid' is set
        if self.api_client.client_side_validation and local_var_params.get('stop_area_gid') is None:  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `stop_area_gid` when calling `stop_areas_stop_area_gid_departures_details_reference_details_get`")  # noqa: E501

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
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        response_types_map = {
            200: "VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsDepartureDetailsApiModel",
            400: "VTApiPlaneraResaWebV4ModelsApiError",
            404: "MicrosoftAspNetCoreMvcProblemDetails",
            500: None,
            503: None,
        }

        return self.api_client.call_api(
            '/stop-areas/{stopAreaGid}/departures/{detailsReference}/details', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def stop_areas_stop_area_gid_departures_get(self, stop_area_gid, **kwargs):  # noqa: E501
        """Returns departures from the specified stop area at the specified time.  # noqa: E501

        Sample request:        GET /stop-areas/9021014003980000/departures  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = Reseplaneraren.stop_areas_stop_area_gid_departures_get(stop_area_gid, async_req=True)
        >>> result = thread.get()

        :param stop_area_gid: The 16-digit Västtrafik gid of the stop area. (required)
        :type stop_area_gid: str
        :param start_date_time: The start of the time interval for which to get upcoming departures. Must be specified in RFC 3339 format or be null which means that the current time on the server is used.
        :type start_date_time: datetime
        :param platforms: Filter results by platform. Multiple platforms are separated by comma. Case sensitive.
        :type platforms: str
        :param time_span_in_minutes: The number of minutes from the start time for which to get upcoming departures. Allowed values are between 0 and 1440.
        :type time_span_in_minutes: int
        :param max_departures_per_line_and_direction: The maximum number of departures for a single line in a specific direction.
        :type max_departures_per_line_and_direction: int
        :param limit: The number of results to return.
        :type limit: int
        :param offset: The zero-based start offset of the pagination.
        :type offset: int
        :param include_occupancy: Includes occupancy in departure.
        :type include_occupancy: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsGetDeparturesResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.stop_areas_stop_area_gid_departures_get_with_http_info(stop_area_gid, **kwargs)  # noqa: E501

    def stop_areas_stop_area_gid_departures_get_with_http_info(self, stop_area_gid, **kwargs):  # noqa: E501
        """Returns departures from the specified stop area at the specified time.  # noqa: E501

        Sample request:        GET /stop-areas/9021014003980000/departures  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = Reseplaneraren.stop_areas_stop_area_gid_departures_get_with_http_info(stop_area_gid, async_req=True)
        >>> result = thread.get()

        :param stop_area_gid: The 16-digit Västtrafik gid of the stop area. (required)
        :type stop_area_gid: str
        :param start_date_time: The start of the time interval for which to get upcoming departures. Must be specified in RFC 3339 format or be null which means that the current time on the server is used.
        :type start_date_time: datetime
        :param platforms: Filter results by platform. Multiple platforms are separated by comma. Case sensitive.
        :type platforms: str
        :param time_span_in_minutes: The number of minutes from the start time for which to get upcoming departures. Allowed values are between 0 and 1440.
        :type time_span_in_minutes: int
        :param max_departures_per_line_and_direction: The maximum number of departures for a single line in a specific direction.
        :type max_departures_per_line_and_direction: int
        :param limit: The number of results to return.
        :type limit: int
        :param offset: The zero-based start offset of the pagination.
        :type offset: int
        :param include_occupancy: Includes occupancy in departure.
        :type include_occupancy: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsGetDeparturesResponse, status_code(int), headers(HTTPHeaderDict))
        """

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

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stop_areas_stop_area_gid_departures_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'stop_area_gid' is set
        if self.api_client.client_side_validation and local_var_params.get('stop_area_gid') is None:  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `stop_area_gid` when calling `stop_areas_stop_area_gid_departures_get`")  # noqa: E501

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
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        response_types_map = {
            200: "VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsGetDeparturesResponse",
            400: "VTApiPlaneraResaWebV4ModelsApiError",
            404: "MicrosoftAspNetCoreMvcProblemDetails",
            500: None,
            503: None,
        }

        return self.api_client.call_api(
            '/stop-areas/{stopAreaGid}/departures', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def stop_points_stop_point_gid_arrivals_details_reference_details_get(self, details_reference, stop_point_gid,
                                                                          **kwargs):  # noqa: E501
        """Returns details about an arrival.  # noqa: E501

        Sample request:        GET /stop-points/9022014001760003/arrivals/{detailsReference}/details?includes=servicejourneycalls  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = Reseplaneraren.stop_points_stop_point_gid_arrivals_details_reference_details_get(details_reference, stop_point_gid, async_req=True)
        >>> result = thread.get()

        :param details_reference: The reference to the service journey, received from the arrivals call. A detailsReference is only valid during the same day as it was generated. (required)
        :type details_reference: str
        :param stop_point_gid: (required)
        :type stop_point_gid: str
        :param includes: The additional information to include in the response.
        :type includes: list[VTApiPlaneraResaWebV4ModelsArrivalDetailsIncludeType]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsArrivalDetailsApiModel
        """
        kwargs['_return_http_data_only'] = True
        return self.stop_points_stop_point_gid_arrivals_details_reference_details_get_with_http_info(details_reference,
                                                                                                     stop_point_gid,
                                                                                                     **kwargs)  # noqa: E501

    def stop_points_stop_point_gid_arrivals_details_reference_details_get_with_http_info(self, details_reference,
                                                                                         stop_point_gid,
                                                                                         **kwargs):  # noqa: E501
        """Returns details about an arrival.  # noqa: E501

        Sample request:        GET /stop-points/9022014001760003/arrivals/{detailsReference}/details?includes=servicejourneycalls  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = Reseplaneraren.stop_points_stop_point_gid_arrivals_details_reference_details_get_with_http_info(details_reference, stop_point_gid, async_req=True)
        >>> result = thread.get()

        :param details_reference: The reference to the service journey, received from the arrivals call. A detailsReference is only valid during the same day as it was generated. (required)
        :type details_reference: str
        :param stop_point_gid: (required)
        :type stop_point_gid: str
        :param includes: The additional information to include in the response.
        :type includes: list[VTApiPlaneraResaWebV4ModelsArrivalDetailsIncludeType]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsArrivalDetailsApiModel, status_code(int), headers(HTTPHeaderDict))
        """

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

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stop_points_stop_point_gid_arrivals_details_reference_details_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'details_reference' is set
        if self.api_client.client_side_validation and local_var_params.get('details_reference') is None:  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `details_reference` when calling `stop_points_stop_point_gid_arrivals_details_reference_details_get`")  # noqa: E501
        # verify the required parameter 'stop_point_gid' is set
        if self.api_client.client_side_validation and local_var_params.get('stop_point_gid') is None:  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `stop_point_gid` when calling `stop_points_stop_point_gid_arrivals_details_reference_details_get`")  # noqa: E501

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
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        response_types_map = {
            200: "VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsArrivalDetailsApiModel",
            400: "VTApiPlaneraResaWebV4ModelsApiError",
            404: "MicrosoftAspNetCoreMvcProblemDetails",
            500: None,
            503: None,
        }

        return self.api_client.call_api(
            '/stop-points/{stopPointGid}/arrivals/{detailsReference}/details', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def stop_points_stop_point_gid_arrivals_get(self, stop_point_gid, **kwargs):  # noqa: E501
        """Returns arrivals to the specified stop point at the specified time.  # noqa: E501

        Sample request:        GET /stop-points/9022014001760003/arrivals  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = Reseplaneraren.stop_points_stop_point_gid_arrivals_get(stop_point_gid, async_req=True)
        >>> result = thread.get()

        :param stop_point_gid: The 16-digit Västtrafik gid of the stop point. (required)
        :type stop_point_gid: str
        :param start_date_time: The start of the time interval for which to get upcoming arrivals. Must be specified in RFC 3339 format or be null which means that the current time on the server is used.
        :type start_date_time: str
        :param time_span_in_minutes: The number of minutes from the start time for which to get upcoming arrivals. Allowed values are between 0 and 1440.
        :type time_span_in_minutes: int
        :param max_arrivals_per_line_and_direction: The maximum number of arrivals for a single line in a specific direction.
        :type max_arrivals_per_line_and_direction: int
        :param limit: The number of results to return.
        :type limit: int
        :param offset: The zero-based start offset of the pagination.
        :type offset: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsGetArrivalsResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.stop_points_stop_point_gid_arrivals_get_with_http_info(stop_point_gid, **kwargs)  # noqa: E501

    def stop_points_stop_point_gid_arrivals_get_with_http_info(self, stop_point_gid, **kwargs):  # noqa: E501
        """Returns arrivals to the specified stop point at the specified time.  # noqa: E501

        Sample request:        GET /stop-points/9022014001760003/arrivals  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = Reseplaneraren.stop_points_stop_point_gid_arrivals_get_with_http_info(stop_point_gid, async_req=True)
        >>> result = thread.get()

        :param stop_point_gid: The 16-digit Västtrafik gid of the stop point. (required)
        :type stop_point_gid: str
        :param start_date_time: The start of the time interval for which to get upcoming arrivals. Must be specified in RFC 3339 format or be null which means that the current time on the server is used.
        :type start_date_time: str
        :param time_span_in_minutes: The number of minutes from the start time for which to get upcoming arrivals. Allowed values are between 0 and 1440.
        :type time_span_in_minutes: int
        :param max_arrivals_per_line_and_direction: The maximum number of arrivals for a single line in a specific direction.
        :type max_arrivals_per_line_and_direction: int
        :param limit: The number of results to return.
        :type limit: int
        :param offset: The zero-based start offset of the pagination.
        :type offset: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsGetArrivalsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'stop_point_gid',
            'start_date_time',
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

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stop_points_stop_point_gid_arrivals_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'stop_point_gid' is set
        if self.api_client.client_side_validation and local_var_params.get('stop_point_gid') is None:  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `stop_point_gid` when calling `stop_points_stop_point_gid_arrivals_get`")  # noqa: E501

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
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        response_types_map = {
            200: "VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsGetArrivalsResponse",
            400: "VTApiPlaneraResaWebV4ModelsApiError",
            404: "MicrosoftAspNetCoreMvcProblemDetails",
            500: None,
            503: None,
        }

        return self.api_client.call_api(
            '/stop-points/{stopPointGid}/arrivals', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def stop_points_stop_point_gid_departures_details_reference_details_get(self, details_reference, stop_point_gid,
                                                                            **kwargs):  # noqa: E501
        """Returns details about a departure.  # noqa: E501

        Sample request:        GET /stop-points/9022014001760003/departures/{detailsReference}/details?includes=servicejourneycalls  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = Reseplaneraren.stop_points_stop_point_gid_departures_details_reference_details_get(details_reference, stop_point_gid, async_req=True)
        >>> result = thread.get()

        :param details_reference: The reference to the service journey, received from the departures call. A detailsReference is only valid during the same day as it was generated. (required)
        :type details_reference: str
        :param stop_point_gid: (required)
        :type stop_point_gid: str
        :param includes: The additional information to include in the response.
        :type includes: list[VTApiPlaneraResaWebV4ModelsDepartureDetailsIncludeType]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsDepartureDetailsApiModel
        """
        kwargs['_return_http_data_only'] = True
        return self.stop_points_stop_point_gid_departures_details_reference_details_get_with_http_info(
            details_reference, stop_point_gid, **kwargs)  # noqa: E501

    def stop_points_stop_point_gid_departures_details_reference_details_get_with_http_info(self, details_reference,
                                                                                           stop_point_gid,
                                                                                           **kwargs):  # noqa: E501
        """Returns details about a departure.  # noqa: E501

        Sample request:        GET /stop-points/9022014001760003/departures/{detailsReference}/details?includes=servicejourneycalls  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = Reseplaneraren.stop_points_stop_point_gid_departures_details_reference_details_get_with_http_info(details_reference, stop_point_gid, async_req=True)
        >>> result = thread.get()

        :param details_reference: The reference to the service journey, received from the departures call. A detailsReference is only valid during the same day as it was generated. (required)
        :type details_reference: str
        :param stop_point_gid: (required)
        :type stop_point_gid: str
        :param includes: The additional information to include in the response.
        :type includes: list[VTApiPlaneraResaWebV4ModelsDepartureDetailsIncludeType]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsDepartureDetailsApiModel, status_code(int), headers(HTTPHeaderDict))
        """

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

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stop_points_stop_point_gid_departures_details_reference_details_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'details_reference' is set
        if self.api_client.client_side_validation and local_var_params.get('details_reference') is None:  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `details_reference` when calling `stop_points_stop_point_gid_departures_details_reference_details_get`")  # noqa: E501
        # verify the required parameter 'stop_point_gid' is set
        if self.api_client.client_side_validation and local_var_params.get('stop_point_gid') is None:  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `stop_point_gid` when calling `stop_points_stop_point_gid_departures_details_reference_details_get`")  # noqa: E501

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
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        response_types_map = {
            200: "VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsDepartureDetailsApiModel",
            400: "VTApiPlaneraResaWebV4ModelsApiError",
            404: "MicrosoftAspNetCoreMvcProblemDetails",
            500: None,
            503: None,
        }

        return self.api_client.call_api(
            '/stop-points/{stopPointGid}/departures/{detailsReference}/details', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def stop_points_stop_point_gid_departures_get(self, stop_point_gid, **kwargs):  # noqa: E501
        """Returns departures from the specified stop point at the specified time.  # noqa: E501

        Sample request:        GET /stop-points/9022014001760003/departures  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = Reseplaneraren.stop_points_stop_point_gid_departures_get(stop_point_gid, async_req=True)
        >>> result = thread.get()

        :param stop_point_gid: The 16-digit Västtrafik gid of the stop point. (required)
        :type stop_point_gid: str
        :param start_date_time: The start of the time interval for which to get upcoming departures. Must be specified in RFC 3339 format or be null which means that the current time on the server is used.
        :type start_date_time: str
        :param time_span_in_minutes: The number of minutes from the start time for which to get upcoming departures. Allowed values are between 0 and 1440.
        :type time_span_in_minutes: int
        :param max_departures_per_line_and_direction: The maximum number of departures for a single line in a specific direction.
        :type max_departures_per_line_and_direction: int
        :param limit: The number of results to return.
        :type limit: int
        :param offset: The zero-based start offset of the pagination.
        :type offset: int
        :param include_occupancy: Includes occupancy in departure.
        :type include_occupancy: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsGetDeparturesResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.stop_points_stop_point_gid_departures_get_with_http_info(stop_point_gid, **kwargs)  # noqa: E501

    def stop_points_stop_point_gid_departures_get_with_http_info(self, stop_point_gid, **kwargs):  # noqa: E501
        """Returns departures from the specified stop point at the specified time.  # noqa: E501

        Sample request:        GET /stop-points/9022014001760003/departures  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = Reseplaneraren.stop_points_stop_point_gid_departures_get_with_http_info(stop_point_gid, async_req=True)
        >>> result = thread.get()

        :param stop_point_gid: The 16-digit Västtrafik gid of the stop point. (required)
        :type stop_point_gid: str
        :param start_date_time: The start of the time interval for which to get upcoming departures. Must be specified in RFC 3339 format or be null which means that the current time on the server is used.
        :type start_date_time: str
        :param time_span_in_minutes: The number of minutes from the start time for which to get upcoming departures. Allowed values are between 0 and 1440.
        :type time_span_in_minutes: int
        :param max_departures_per_line_and_direction: The maximum number of departures for a single line in a specific direction.
        :type max_departures_per_line_and_direction: int
        :param limit: The number of results to return.
        :type limit: int
        :param offset: The zero-based start offset of the pagination.
        :type offset: int
        :param include_occupancy: Includes occupancy in departure.
        :type include_occupancy: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsGetDeparturesResponse, status_code(int), headers(HTTPHeaderDict))
        """

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

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stop_points_stop_point_gid_departures_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'stop_point_gid' is set
        if self.api_client.client_side_validation and local_var_params.get('stop_point_gid') is None:  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `stop_point_gid` when calling `stop_points_stop_point_gid_departures_get`")  # noqa: E501

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
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        response_types_map = {
            200: "VTApiPlaneraResaWebV4ModelsDeparturesAndArrivalsGetDeparturesResponse",
            400: "VTApiPlaneraResaWebV4ModelsApiError",
            404: "MicrosoftAspNetCoreMvcProblemDetails",
            500: None,
            503: None,
        }

        return self.api_client.call_api(
            '/stop-points/{stopPointGid}/departures', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def journeys_details_reference_details_get(self, details_reference, **kwargs):  # noqa: E501
        """Returns details about a journey.  # noqa: E501

        Sample request:        GET /journeys/{detailsReference}/details?includes=ticketsuggestions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = Reseplaneraren.journeys_details_reference_details_get(details_reference, async_req=True)
        >>> result = thread.get()

        :param details_reference: The reference to the journey, received from the search journeys query. A detailsReference is only valid during the same day as it was generated. (required)
        :type details_reference: str
        :param includes: The additional information to include in the response.
        :type includes: list[VTApiPlaneraResaWebV4ModelsJourneyDetailsIncludeType]
        :param channel_ids: List of channel ids to include if 'ticketsuggestions' is set in the 'includes' parameter. Optional parameter.
        :type channel_ids: list[int]
        :param product_types: List of product type ids to include if 'ticketsuggestions' is set in the 'includes' parameter. Optional parameter.
        :type product_types: list[int]
        :param traveller_categories: List of traveller category ids to include if 'ticketsuggestions' is set in the 'includes' parameter. Optional parameter.
        :type traveller_categories: list[VTApiPlaneraResaCoreModelsTravellerCategory]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel
        """
        kwargs['_return_http_data_only'] = True
        return self.journeys_details_reference_details_get_with_http_info(details_reference, **kwargs)  # noqa: E501

    def journeys_details_reference_details_get_with_http_info(self, details_reference, **kwargs):  # noqa: E501
        """Returns details about a journey.  # noqa: E501

        Sample request:        GET /journeys/{detailsReference}/details?includes=ticketsuggestions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = Reseplaneraren.journeys_details_reference_details_get_with_http_info(details_reference, async_req=True)
        >>> result = thread.get()

        :param details_reference: The reference to the journey, received from the search journeys query. A detailsReference is only valid during the same day as it was generated. (required)
        :type details_reference: str
        :param includes: The additional information to include in the response.
        :type includes: list[VTApiPlaneraResaWebV4ModelsJourneyDetailsIncludeType]
        :param channel_ids: List of channel ids to include if 'ticketsuggestions' is set in the 'includes' parameter. Optional parameter.
        :type channel_ids: list[int]
        :param product_types: List of product type ids to include if 'ticketsuggestions' is set in the 'includes' parameter. Optional parameter.
        :type product_types: list[int]
        :param traveller_categories: List of traveller category ids to include if 'ticketsuggestions' is set in the 'includes' parameter. Optional parameter.
        :type traveller_categories: list[VTApiPlaneraResaCoreModelsTravellerCategory]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel, status_code(int), headers(HTTPHeaderDict))
        """

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

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method journeys_details_reference_details_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'details_reference' is set
        if self.api_client.client_side_validation and local_var_params.get('details_reference') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `details_reference` when calling `journeys_details_reference_details_get`")  # noqa: E501

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
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        response_types_map = {
            200: "VTApiPlaneraResaWebV4ModelsJourneyDetailsJourneyDetailsApiModel",
            400: "VTApiPlaneraResaWebV4ModelsApiError",
            404: "MicrosoftAspNetCoreMvcProblemDetails",
            500: None,
            503: None,
        }

        return self.api_client.call_api(
            '/journeys/{detailsReference}/details', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def journeys_get(self, **kwargs):  # noqa: E501
        """Returns journeys matching the specified search parameters.  # noqa: E501

        For an origin or destination to be valid, either a gid or a combination of latitude and longitude must be specified. OriginName and destinationName are optional in combination with latitude and longitude.    Sample request:        GET /journeys?originGid=9021014001760000&destinationGid=9021014003980000    or        GET /journeys?originName=Sadelsten,+V%C3%A5rg%C3%A5rda&originLongitude=12.63308&originLatitude=58.028237&destinationLongitude=11.930897&destinationLatitude=57.586085&destinationName=%C3%85sdammsstigen,+427+36+Billdal  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = Reseplaneraren.journeys_get(async_req=True)
        >>> result = thread.get()

        :param origin_gid: The 16-digit Västtrafik gid of the origin location (which could be either a stop area (e.g. '9021014001760000'), a stop point (e.g. '9022014001760004') or meta-station (e.g. '0000000800000022')).
        :type origin_gid: str
        :param origin_name: The name of the origin location. The maximum length allowed is 256 characters.
        :type origin_name: str
        :param origin_latitude: The latitude of the origin location.
        :type origin_latitude: float
        :param origin_longitude: The longitude of the origin location.
        :type origin_longitude: float
        :param destination_gid: The 16-digit Västtrafik gid of the destination location (which could be either a stop area, stop point or meta-station).
        :type destination_gid: str
        :param destination_name: The name of the destination location. The maximum length allowed is 256 characters.
        :type destination_name: str
        :param destination_latitude: The latitude of the destination location.
        :type destination_latitude: float
        :param destination_longitude: The longitude of the destination location.
        :type destination_longitude: float
        :param date_time: The datetime for which to search journeys. Must be specified in RFC 3339 format or be null which means that the current time on the server is used. The related dateTimeRelatesTo parameter specifies if the time is related to the arrival or departure.
        :type date_time: datetime
        :param date_time_relates_to: Specifies if the datetime is related to the departure or arrival of the journey.
        :type date_time_relates_to: VTApiPlaneraResaCoreModelsDateTimeRelatesToType
        :param pagination_reference: Pagination reference from a previous search.
        :type pagination_reference: str
        :param limit: The number of results to return. Not guaranteed to return the specified number of results and usually not more than 7 results.
        :type limit: int
        :param transport_modes: The transport modes to include when searching for journeys, if none specified all transport modes are included.
        :type transport_modes: list[VTApiPlaneraResaWebV4ModelsJourneyTransportMode]
        :param transport_sub_modes: The transport sub modes to include when searching for journeys, if none specified all transport sub modes are included. Only supported in combination with transportMode 'train'.
        :type transport_sub_modes: list[VTApiPlaneraResaWebV4ModelsJourneyTransportSubMode]
        :param only_direct_connections: Only include direct connections, e.g. journeys with one trip leg.
        :type only_direct_connections: bool
        :param include_nearby_stop_areas: Includes nearby stop areas when searching for a journey to or from a stop area or stop point. This means that the search algorithm will take additional stop points of other stop areas nearby the given start and destination stop area into account. These additional stop points are reachable by walk. E.g when true a journey suggestion may include a departure access link (initial walking leg) to a stop point of a stop area close by the specified origin stop area.
        :type include_nearby_stop_areas: bool
        :param via_gid: The 16-digit Västtrafik gid of the via location (which must be a stop area).
        :type via_gid: int
        :param origin_walk: Enables/disables using footpaths in the beginning of a trip when searching from an address. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable walk with a minimum distance of 0 meters and a maximum distance of 3 kilometers, set the parameter originWalk=1,0,3000. If default distances should be used, skip the values, e.g 1,,. This will enable walk with the default minimum (0 meters) and the default maximum (2000 meters).
        :type origin_walk: str
        :param dest_walk: Enables/disables using footpaths at the end of a trip when searching to an address. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable walk with a minimum distance of 0 meters and a maximum distance of 3 kilometers, set the parameter destWalk=1,0,3000. If default distances should be used, skip the values, e.g 1,,. This will enable walk with the default minimum (0 meters) and the default maximum (2000 meters).
        :type dest_walk: str
        :param origin_bike: Enables/disables using bike paths in the beginning of a trip when searching from an address. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable bike with a minimum distance of 1000 meters and a maximum distance of 5 kilometers, set the parameter originBike=1,1000,5000. If default distances should be used, skip the values, e.g 1,,. This will enable bike with the default minimum (0 meters) and the default maximum (3000 meters).
        :type origin_bike: str
        :param dest_bike: Enables/disables using bike paths at the end of a trip when searching to an address. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable bike with a minimum distance of 1000 meters and a maximum distance of 5 kilometers, set the parameter destBike=1,1000,5000. If default distances should be used, skip the values, e.g 1,,. This will enable bike with the default minimum (0 meters) and the default maximum (3000 meters).
        :type dest_bike: str
        :param total_bike: Enables/disables using bike routes for the whole trip. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable bike with a minimum distance of 0 meters and a maximum distance of 20 kilometers, set the parameter totalBike=1,0,20000. If default distances should be used, skip the values, e.g 1,,. This will enable bike with the default minimum (0 meters) and the default maximum (25000 meters).
        :type total_bike: str
        :param origin_car: Enables/disables using car in the beginning of a trip when searching from an address. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable car with a minimum distance of 2000 meters and a maximum distance of 7 kilometers, set the parameter origincar=1,2000,7000. If default distances should be used, skip the values, e.g 1,,. This will enable car with the default minimum (0 meters) and the default maximum (5000 meters).
        :type origin_car: str
        :param dest_car: Enables/disables using car at the end of a trip when searching to an address. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable car with a minimum distance of 2000 meters and a maximum distance of 7 kilometers, set the parameter destCar=1,2000,7000. If default distances should be used, skip the values, e.g 1,,. This will enable car with the default minimum (0 meters) and the default maximum (5000 meters).
        :type dest_car: str
        :param origin_park: Enables/disables using Park and Ride in the beginning of a trip when searching from an address. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable Park and Ride with a minimum distance of 3000 meters and a maximum distance of 70 kilometers, set the parameter originPark=1,3000,70000. If default distances should be used, skip the values, e.g 1,,. This will enable Park and Ride with the default minimum (2000 meters) and the default maximum (50000 meters).
        :type origin_park: str
        :param dest_park: Enables/disables using Park and Ride at the end of a trip when searching to an address. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable Park and Ride with a minimum distance of 3000 meters and a maximum distance of 70 kilometers, set the parameter destPark=1,3000,70000. If default distances should be used, skip the values, e.g 1,,. This will enable Park and Ride with the default minimum (2000 meters) and the default maximum (50000 meters).
        :type dest_park: str
        :param interchange_duration_in_minutes: The minimum number of minutes between arrival and departure for a connection to be valid and the trip included in the search results, ignoring the default value.
        :type interchange_duration_in_minutes: int
        :param include_occupancy: Includes occupancy in journey.
        :type include_occupancy: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: VTApiPlaneraResaWebV4ModelsJourneysGetJourneysResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.journeys_get_with_http_info(**kwargs)  # noqa: E501

    def journeys_get_with_http_info(self, **kwargs):  # noqa: E501
        """Returns journeys matching the specified search parameters.  # noqa: E501

        For an origin or destination to be valid, either a gid or a combination of latitude and longitude must be specified. OriginName and destinationName are optional in combination with latitude and longitude.    Sample request:        GET /journeys?originGid=9021014001760000&destinationGid=9021014003980000    or        GET /journeys?originName=Sadelsten,+V%C3%A5rg%C3%A5rda&originLongitude=12.63308&originLatitude=58.028237&destinationLongitude=11.930897&destinationLatitude=57.586085&destinationName=%C3%85sdammsstigen,+427+36+Billdal  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = Reseplaneraren.journeys_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param origin_gid: The 16-digit Västtrafik gid of the origin location (which could be either a stop area (e.g. '9021014001760000'), a stop point (e.g. '9022014001760004') or meta-station (e.g. '0000000800000022')).
        :type origin_gid: str
        :param origin_name: The name of the origin location. The maximum length allowed is 256 characters.
        :type origin_name: str
        :param origin_latitude: The latitude of the origin location.
        :type origin_latitude: float
        :param origin_longitude: The longitude of the origin location.
        :type origin_longitude: float
        :param destination_gid: The 16-digit Västtrafik gid of the destination location (which could be either a stop area, stop point or meta-station).
        :type destination_gid: str
        :param destination_name: The name of the destination location. The maximum length allowed is 256 characters.
        :type destination_name: str
        :param destination_latitude: The latitude of the destination location.
        :type destination_latitude: float
        :param destination_longitude: The longitude of the destination location.
        :type destination_longitude: float
        :param date_time: The datetime for which to search journeys. Must be specified in RFC 3339 format or be null which means that the current time on the server is used. The related dateTimeRelatesTo parameter specifies if the time is related to the arrival or departure.
        :type date_time: datetime
        :param date_time_relates_to: Specifies if the datetime is related to the departure or arrival of the journey.
        :type date_time_relates_to: VTApiPlaneraResaCoreModelsDateTimeRelatesToType
        :param pagination_reference: Pagination reference from a previous search.
        :type pagination_reference: str
        :param limit: The number of results to return. Not guaranteed to return the specified number of results and usually not more than 7 results.
        :type limit: int
        :param transport_modes: The transport modes to include when searching for journeys, if none specified all transport modes are included.
        :type transport_modes: list[VTApiPlaneraResaWebV4ModelsJourneyTransportMode]
        :param transport_sub_modes: The transport sub modes to include when searching for journeys, if none specified all transport sub modes are included. Only supported in combination with transportMode 'train'.
        :type transport_sub_modes: list[VTApiPlaneraResaWebV4ModelsJourneyTransportSubMode]
        :param only_direct_connections: Only include direct connections, e.g. journeys with one trip leg.
        :type only_direct_connections: bool
        :param include_nearby_stop_areas: Includes nearby stop areas when searching for a journey to or from a stop area or stop point. This means that the search algorithm will take additional stop points of other stop areas nearby the given start and destination stop area into account. These additional stop points are reachable by walk. E.g when true a journey suggestion may include a departure access link (initial walking leg) to a stop point of a stop area close by the specified origin stop area.
        :type include_nearby_stop_areas: bool
        :param via_gid: The 16-digit Västtrafik gid of the via location (which must be a stop area).
        :type via_gid: int
        :param origin_walk: Enables/disables using footpaths in the beginning of a trip when searching from an address. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable walk with a minimum distance of 0 meters and a maximum distance of 3 kilometers, set the parameter originWalk=1,0,3000. If default distances should be used, skip the values, e.g 1,,. This will enable walk with the default minimum (0 meters) and the default maximum (2000 meters).
        :type origin_walk: str
        :param dest_walk: Enables/disables using footpaths at the end of a trip when searching to an address. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable walk with a minimum distance of 0 meters and a maximum distance of 3 kilometers, set the parameter destWalk=1,0,3000. If default distances should be used, skip the values, e.g 1,,. This will enable walk with the default minimum (0 meters) and the default maximum (2000 meters).
        :type dest_walk: str
        :param origin_bike: Enables/disables using bike paths in the beginning of a trip when searching from an address. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable bike with a minimum distance of 1000 meters and a maximum distance of 5 kilometers, set the parameter originBike=1,1000,5000. If default distances should be used, skip the values, e.g 1,,. This will enable bike with the default minimum (0 meters) and the default maximum (3000 meters).
        :type origin_bike: str
        :param dest_bike: Enables/disables using bike paths at the end of a trip when searching to an address. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable bike with a minimum distance of 1000 meters and a maximum distance of 5 kilometers, set the parameter destBike=1,1000,5000. If default distances should be used, skip the values, e.g 1,,. This will enable bike with the default minimum (0 meters) and the default maximum (3000 meters).
        :type dest_bike: str
        :param total_bike: Enables/disables using bike routes for the whole trip. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable bike with a minimum distance of 0 meters and a maximum distance of 20 kilometers, set the parameter totalBike=1,0,20000. If default distances should be used, skip the values, e.g 1,,. This will enable bike with the default minimum (0 meters) and the default maximum (25000 meters).
        :type total_bike: str
        :param origin_car: Enables/disables using car in the beginning of a trip when searching from an address. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable car with a minimum distance of 2000 meters and a maximum distance of 7 kilometers, set the parameter origincar=1,2000,7000. If default distances should be used, skip the values, e.g 1,,. This will enable car with the default minimum (0 meters) and the default maximum (5000 meters).
        :type origin_car: str
        :param dest_car: Enables/disables using car at the end of a trip when searching to an address. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable car with a minimum distance of 2000 meters and a maximum distance of 7 kilometers, set the parameter destCar=1,2000,7000. If default distances should be used, skip the values, e.g 1,,. This will enable car with the default minimum (0 meters) and the default maximum (5000 meters).
        :type dest_car: str
        :param origin_park: Enables/disables using Park and Ride in the beginning of a trip when searching from an address. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable Park and Ride with a minimum distance of 3000 meters and a maximum distance of 70 kilometers, set the parameter originPark=1,3000,70000. If default distances should be used, skip the values, e.g 1,,. This will enable Park and Ride with the default minimum (2000 meters) and the default maximum (50000 meters).
        :type origin_park: str
        :param dest_park: Enables/disables using Park and Ride at the end of a trip when searching to an address. To fine-tune the minimum and/or maximum distance to the next public transport station, provide these values separated by comma. The values are expressed in meters. To enable Park and Ride with a minimum distance of 3000 meters and a maximum distance of 70 kilometers, set the parameter destPark=1,3000,70000. If default distances should be used, skip the values, e.g 1,,. This will enable Park and Ride with the default minimum (2000 meters) and the default maximum (50000 meters).
        :type dest_park: str
        :param interchange_duration_in_minutes: The minimum number of minutes between arrival and departure for a connection to be valid and the trip included in the search results, ignoring the default value.
        :type interchange_duration_in_minutes: int
        :param include_occupancy: Includes occupancy in journey.
        :type include_occupancy: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(VTApiPlaneraResaWebV4ModelsJourneysGetJourneysResponse, status_code(int), headers(HTTPHeaderDict))
        """

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

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
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
            query_params.append(('interchangeDurationInMinutes', local_var_params['interchange_duration_in_minutes']))  # noqa: E501
        if local_var_params.get('include_occupancy') is not None:  # noqa: E501
            query_params.append(('includeOccupancy', local_var_params['include_occupancy']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        response_types_map = {
            200: "VTApiPlaneraResaWebV4ModelsJourneysGetJourneysResponse",
            400: "VTApiPlaneraResaWebV4ModelsApiError",
            500: None,
            503: None,
        }

        return self.api_client.call_api(
            '/journeys', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def journeys_reconstruct_get(self, ref, **kwargs):  # noqa: E501
        """Reconstructs a journey based on the given reconstruction reference, received from the search journeys query.  # noqa: E501

        Sample request:        GET /journeys/reconstruct?ref=¶HKI¶T$A=1@O=Brunnsparken, Göteborg@L=1760003@a=128@$A=1@O=Korsvägen, Göteborg@L=3980004@a=128@$202206131358$202206131406$Spå    4$$1$$$$$$¶KRCC¶#VE#1#  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = Reseplaneraren.journeys_reconstruct_get(ref, async_req=True)
        >>> result = thread.get()

        :param ref: The reconstruction reference. A reconstructionReference is valid as long as the original journey search is valid. (required)
        :type ref: str
        :param include_occupancy: Includes occupancy in journey.
        :type include_occupancy: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: VTApiPlaneraResaWebV4ModelsJourneysJourneyApiModel
        """
        kwargs['_return_http_data_only'] = True
        return self.journeys_reconstruct_get_with_http_info(ref, **kwargs)  # noqa: E501

    def journeys_reconstruct_get_with_http_info(self, ref, **kwargs):  # noqa: E501
        """Reconstructs a journey based on the given reconstruction reference, received from the search journeys query.  # noqa: E501

        Sample request:        GET /journeys/reconstruct?ref=¶HKI¶T$A=1@O=Brunnsparken, Göteborg@L=1760003@a=128@$A=1@O=Korsvägen, Göteborg@L=3980004@a=128@$202206131358$202206131406$Spå    4$$1$$$$$$¶KRCC¶#VE#1#  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = Reseplaneraren.journeys_reconstruct_get_with_http_info(ref, async_req=True)
        >>> result = thread.get()

        :param ref: The reconstruction reference. A reconstructionReference is valid as long as the original journey search is valid. (required)
        :type ref: str
        :param include_occupancy: Includes occupancy in journey.
        :type include_occupancy: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(VTApiPlaneraResaWebV4ModelsJourneysJourneyApiModel, status_code(int), headers(HTTPHeaderDict))
        """

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

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method journeys_reconstruct_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'ref' is set
        if self.api_client.client_side_validation and local_var_params.get('ref') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `ref` when calling `journeys_reconstruct_get`")  # noqa: E501

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
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        response_types_map = {
            200: "VTApiPlaneraResaWebV4ModelsJourneysJourneyApiModel",
            400: "VTApiPlaneraResaWebV4ModelsApiError",
            500: None,
            503: None,
            404: None,
        }

        return self.api_client.call_api(
            '/journeys/reconstruct', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def journeys_valid_time_interval_get(self, **kwargs):  # noqa: E501
        """Returns a time interval for when journey data is available.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = Reseplaneraren.journeys_valid_time_interval_get(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: VTApiPlaneraResaWebV4ModelsValidTimeIntervalApiModel
        """
        kwargs['_return_http_data_only'] = True
        return self.journeys_valid_time_interval_get_with_http_info(**kwargs)  # noqa: E501

    def journeys_valid_time_interval_get_with_http_info(self, **kwargs):  # noqa: E501
        """Returns a time interval for when journey data is available.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = Reseplaneraren.journeys_valid_time_interval_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(VTApiPlaneraResaWebV4ModelsValidTimeIntervalApiModel, status_code(int), headers(HTTPHeaderDict))
        """

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

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
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
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        response_types_map = {
            200: "VTApiPlaneraResaWebV4ModelsValidTimeIntervalApiModel",
            404: "MicrosoftAspNetCoreMvcProblemDetails",
            500: None,
            503: None,
        }

        return self.api_client.call_api(
            '/journeys/valid-time-interval', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    # def request(self, url):
    #     header = {"Authorization": self.auth.token}
    #     response = requests.get(url, headers=header)
    #     response = self.auth.check_response(response)
    #
    #     return response.json()


class TrafficSituations:
    def __init__(self, auth):
        if type(auth) != Auth:
            raise TypeError("Expected Auth object")
        self.auth = auth
        self.url = "https://api.vasttrafik.se/ts/v1/traffic-situations"

    def __get(self, url):
        header = {"Authorization": self.auth.token}
        response = requests.get(url, headers=header)
        response = self.auth.check_response(response)

        return response.json()

    def trafficsituations(self):
        url = self.url
        return self.__get(url)

    def stoppoint(self, gid):
        url = self.url + f'/stoppoint/{gid}'
        return self.__get(url)

    def situation(self, gid):
        url = self.url + f'/{gid}'
        return self.__get(url)

    def line(self, gid):
        url = self.url + f'/line/{gid}'
        return self.__get(url)

    def journey(self, gid):
        url = self.url + f'/journey/{gid}'
        return self.__get(url)

    def stoparea(self, gid):
        url = self.url + f'/stoparea/{gid}'
        return self.__get(url)
