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

                >>> thread = api.locations_by_coordinates_get(latitude, longitude, async_req=True)
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

        >>> thread = api.locations_by_coordinates_get_with_http_info(latitude, longitude, async_req=True)
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

        >>> thread = api.locations_by_text_get(q, async_req=True)
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

        >>> thread = api.locations_by_text_get_with_http_info(q, async_req=True)
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

    def request(self, url):
        header = {"Authorization": self.auth.token}
        response = requests.get(url, headers=header)
        response = self.auth.check_response(response)

        return response.json()


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

# if __name__ == "__main__":
#    with open("credentials.csv", "r") as f:
#        key, secret = f.read().split(",")

#    auth = Auth(key, secret, 0)
#    ts = TrafficSituations(auth)
#    vt = Reseplaneraren(auth)

# s = ts.trafficsituations()[0]
# print(s)
# stop1 = vt.location_name(input="Kungssten").get("LocationList").get("StopLocation")[0].get("id")
# print(ts.stoppoint(9022014001040002))
# stop2 = vt.location_name(input="Kampenhof").get("LocationList").get("StopLocation")[0].get("id")
# print(vt.trip(originId=stop1, destId=stop2, date=20190215, time="15:24"))
