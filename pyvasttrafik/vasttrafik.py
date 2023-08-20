# coding: utf-8
import base64
import requests
import six

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

        self.token = "Bearer " + response_dict.get("access_token")

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
    def __init__(self, auth):
        if type(auth) != Auth:
            raise TypeError("Expected Auth object")
        self.auth = auth
        self.url = "https://ext-api.vasttrafik.se/pr/v4"

    def journeys(self, **kwargs):
        header = {"Authorization": self.auth.token}
        url = self.url + "/journeys"
        kwargs["format"] = "json"

        response = requests.get(url, headers=header, params=kwargs)
        response = self.auth.check_response(response)

        return response.json()

    def location_by_coord(self, **kwargs):
        header = {"Authorization": self.auth.token}
        url = self.url + "/locations/by-coordinates"
        kwargs["format"] = "json"

        response = requests.get(url, headers=header, params=kwargs)
        response = self.auth.check_response(response)

        return response.json()

    def locations_by_text(self, **kwargs):
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

        header = {"Authorization": self.auth.token}
        url = self.url + "locations/by-text"

        response = requests.get(url, headers=header, params=kwargs)
        response = self.auth.check_response(response)

        return response.json()

    def livemap(self, baseurl, **kwargs):
        header = {"Authorization": self.auth.token}
        url = baseurl + "/positions"
        kwargs["format"] = "json"

        response = requests.get(url, headers=header, params=kwargs)
        response = self.auth.check_response(response)

        return response.json()

    def journeyDetail(self, baseurl, ref):
        header = {"Authorization": self.auth.token}
        url = baseurl + "/" + ref + "/details"

        # response = requests.get(url, headers=header, params={"ref": ref})
        response = requests.get(url, headers=header)
        response = self.auth.check_response(response)

        return response.json()

    def departureBoard(self, baseurl, gid, **kwargs):
        header = {"Authorization": self.auth.token}
        url = baseurl + "/" + gid + "/departures"
        kwargs["format"] = "json"

        response = requests.get(url, headers=header, params=kwargs)
        response = self.auth.check_response(response)

        return response.json()

    def arrivalBoard(self, baseurl, gid, **kwargs):
        header = {"Authorization": self.auth.token}
        url = baseurl + "/" + gid + "/arrivals"
        kwargs["format"] = "json"

        response = requests.get(url, headers=header, params=kwargs)
        response = self.auth.check_response(response)

        return response.json()

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
