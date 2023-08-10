"""PyVasttrafik Västtrafik Journey Planner API Client"""
# import base64
import json
import time as time_module
import requests
import vasttrafik

TOKEN_URL = "https://ext-api.vasttrafik.se/token"
API_BASE_URL = "https://ext-api.vasttrafik.se/pr/v4"
CONSUMER_KEY = "BQC13xQ6eWZVZGXaHPO9ylOtN9ca"
CONSUMER_SECRET = "xbajICAwyEpIHPoatzOJvqYcs_Qa"
CONSUMER_SCOPE = "1"

auth = vasttrafik.auth(CONSUMER_KEY, CONSUMER_SECRET, CONSUMER_SCOPE)
resepl = vasttrafik.Reseplaneraren(auth)
trafficsit = vasttrafik.TrafficSituations(auth)


def latlon_to_string_representation(latlon):
    """Helper method to convert latlon to string representation
        - latlon: lat or long to convert to string representation
        """
    return str(round(latlon * 1000000)).rstrip('0').rstrip('.')


class Client:
    """Client used to communicate with the API."""

    def __init__(self):
        # self.token = fetch_token(key, secret)
        self.auth = auth
        self.planner = resepl
        self.disturb = trafficsit
        self.response_format = 'json'

    def get_journey_detail(self):
        """/journeyDetail endpoint"""
        raise NotImplementedError

    def get_location_by_coord(self, lat, long, query_params=None):
        """/location.nearbystops endpoint
        - lat:  latitude in long format
        - long: longitude in long format
        """
        kwargs = dict["latitude": lat, "longitude": long]
        data = self.planner.location_by_coord(API_BASE_URL, **kwargs)

        return data['results']

    def get_location_by_text(self, query, query_params=None):
        """/location.name endpoint
        - query: name to search for as string
        """
        data = self.get('/location.name?input=' + query, query_params)
        return data['results']

    def get_nearby_address(self, lat, long, query_params=None):
        """/location.nearbyaddress
        - lat:  latitude in long format
        - long: longitude in long format
        """
        data = self.get('/location.nearbyaddress?originCoordLat=' +
                        str(lat) + '&originCoordLong=' + str(long), query_params)
        return data['LocationList']['CoordLocation']

    # /arrivalBoard endpoint
    def get_arrivals(self, stop_id, direction, date=None, time=None, query_params=None):
        """
        /arrivalBoard endpoint
        - stop_id:      stop_id as long
        - direction:    stop_id as long
        - date:         the date in format YYYY-MM-DD
        - time:         the time in format HH:MM
        """
        if date is not None and time is not None:
            data = self.get('/arrivalBoard?id=' + str(stop_id) +
                            '&date=' + date + '&time=' + time +
                            '&direction=' + str(direction), query_params)
        else:
            data = self.get('/arrivalBoard?id=' + str(stop_id) + '&date=' +
                            time_module.strftime("%Y-%m-%d") +
                            '&time=' + time_module.strftime("%H:%M") +
                            '&direction=' + str(direction), query_params)
        return data['ArrivalBoard']['Arrival']

    # /departureBoard endpoint
    def get_departures(self, stop_id, date=None, time=None, query_params=None):
        """/departureBoard endpoint
        - stop_id:      stop_id as long
        - date:         the date in format YYYY-MM-DD
        - time:         the time in format HH:MM
        """
        if date is not None and time is not None:
            data = self.get('/departureBoard?id=' + str(stop_id) +
                            '&date=' + date + '&time=' + time, query_params)
        else:
            data = self.get('/departureBoard?id=' + str(stop_id) + '&date=' +
                            time_module.strftime("%Y-%m-%d") +
                            '&time=' + time_module.strftime("%H:%M"), query_params)
        return data['DepartureBoard']['Departure']

    # /trip endpoint
    def calculate_trip(self, query_params=None):
        """/trip endpoint"""
        raise NotImplementedError

    # /livemap endpoint
    def get_livemap(self, longitude_max, latitude_max, longitude_min, latitude_min,
                    query_params=None):
        """/livemap endpoint
        - longitude_max:    left border (longitude) of the bounding box in WGS84 * 1000000
        - latitude_max:     right border (longitude) of the bounding box in WGS84 * 1000000
        - longitude_min:    lower border (latitude) of the bounding box in WGS84 * 1000000
        - latitude_min:     upper border (latitude) of the bounding box in WGS84 * 1000000
        """
        if (longitude_max is None or latitude_max is None or longitude_min is None
                or latitude_min is None):
            raise Exception('Error: Missing argument!')
        data = self.get('/livemap?maxx=' + latlon_to_string_representation(longitude_max) +
                        '&maxy=' +
                        latlon_to_string_representation(latitude_max) + '&minx=' +
                        latlon_to_string_representation(longitude_min) + '&miny=' +
                        latlon_to_string_representation(latitude_min), query_params)
        return data['livemap']['vehicles']

    # request builder
    def get(self, endpoint, query_params=None):
        """Helper method to make an HTTP request to the API
        - endpoint: which endpoint to use for the call
        """
        url = API_BASE_URL + endpoint

        if query_params is not None:
            for key in query_params:
                url += '&' + key + '=' + query_params[key]
            url += '&format=' + self.response_format
        elif '?' in url:
            url += '&format=' + self.response_format
        else:
            url += '?format=' + self.response_format

        headers = {
            'Authorization': 'Bearer ' + self.token
        }
        res = requests.get(url, headers=headers)

        if res.status_code == 200:
            return json.loads(res.content.decode('UTF-8'))

        raise Exception(
            'Error: ' + str(res.status_code) + str(res.content))
