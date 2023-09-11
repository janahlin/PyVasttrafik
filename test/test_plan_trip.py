import unittest
import aiohttp
import asyncio
import async_timeout
from datetime import datetime


from pyvasttrafik.vasttrafik_main import Auth, Vasttrafik
from pyvasttrafik.vasttrafik_plan import VasttrafikPlanTrip


class TestAuth(unittest.TestCase):
    def test__auth(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")
        auth = Auth(key, secret, 1)

        # vt = Vasttrafik()

        # print(auth.token)

        # print(rp.locations_by_text_get("Åstol"))


class TestPlanTrips(unittest.TestCase):
    def test_init(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = Auth(key, secret, 1)

        rp = VasttrafikPlanTrip()
        rp.configuration.access_token = auth.token
        url = rp.api_url

        # print(url)

    def test_get_location_by_text(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = Auth(key, secret, 1)

        rp = VasttrafikPlanTrip()
        rp.configuration.access_token = auth.token
        stations = rp.get_location_by_text("Åstol", types="stoparea", limit=1)
        res = stations[0].results
        pag = stations[0].pagination
        links = stations[0].links
        # print(links)

    def test_get_location_by_coordinates(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = Auth(key, secret, 1)

        rp = VasttrafikPlanTrip()
        rp.configuration.access_token = auth.token
        latitude = 57.924079
        longitude = 11.589001
        data = rp.get_location_by_coordinates(latitude, longitude)
        res = data[0].results

        # print(res)

    def test_get_journey(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = Auth(key, secret, 1)

        rp = VasttrafikPlanTrip()
        rp.configuration.access_token = auth.token

        origin = rp.get_location_by_text("Åstol", types="stoparea", limit=1)
        destination = rp.get_location_by_text("Rönnäng", types="stoparea", limit=1)

        # data = rp.get_journeys()
        origin_gid = origin[0].results[0].gid
        destination_gid = destination[0].results[0].gid

        journey = rp.get_journeys(origin_gid=origin_gid, destination_gid=destination_gid)

        # print(journey)

    def test_journey_reconstruct(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = Auth(key, secret, 1)

        rp = VasttrafikPlanTrip()
        rp.configuration.access_token = auth.token

        origin = rp.get_location_by_text("Åstol", types="stoparea", limit=1)
        destination = rp.get_location_by_text("Rönnäng", types="stoparea", limit=1)

        # data = rp.get_journeys()
        origin_gid = origin[0].results[0].gid
        destination_gid = destination[0].results[0].gid

        journey = rp.get_journeys(origin_gid=origin_gid, destination_gid=destination_gid, limit=1)
        journey_ref = journey[0].results
        reconstruct = rp.journeys_reconstruct(ref=journey_ref[0].reconstruction_reference)

        # print(reconstruct)

    def test_journey_get_details(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = Auth(key, secret, 1)

        rp = VasttrafikPlanTrip()
        rp.configuration.access_token = auth.token

        origin = rp.get_location_by_text("Åstol", types="stoparea", limit=1)
        destination = rp.get_location_by_text("Rönnäng", types="stoparea", limit=1)

        # data = rp.get_journeys()
        origin_gid = origin[0].results[0].gid
        destination_gid = destination[0].results[0].gid

        journey = rp.get_journeys(origin_gid=origin_gid, destination_gid=destination_gid, limit=1)
        journey_ref = journey[0].results
        journey_detail = rp.get_journeys_details(details_reference=journey_ref[0].details_reference)

        # print(journey_detail)

    def test_journey_get_valid_time_interval(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = Auth(key, secret, 1)

        rp = VasttrafikPlanTrip()
        rp.configuration.access_token = auth.token

        time_interval = rp.get_journeys_valid_time_interval()

        # print(time_interval)

    def test_positions(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        lowleftlat = 57.72172
        lowleftlong = 12.011882
        upprightlat = 57.737549
        upprightlong = 12.039268
        # limit = 100

        auth = Auth(key, secret, 1)

        rp = VasttrafikPlanTrip()
        rp.configuration.access_token = auth.token

        pos = rp.get_positions(lowleftlat, lowleftlong, upprightlat, upprightlong)

        # print(pos)

    def test_get_departure_area(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = Auth(key, secret, 1)

        rp = VasttrafikPlanTrip()
        rp.configuration.access_token = auth.token

        origin = rp.get_location_by_text("Åstol", types="stoparea", limit=1)

        origin_gid = origin[0].results[0].gid

        departure_area = rp.get_stop_areas_departures_by_gid(origin_gid)

        # print(departure_area)

    def test_get_arrival_area(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = Auth(key, secret, 1)

        rp = VasttrafikPlanTrip()
        rp.configuration.access_token = auth.token

        origin = rp.get_location_by_text("Rönnäng", types="stoparea", limit=1)

        origin_gid = origin[0].results[0].gid

        arrival_area = rp.get_stop_areas_arrivals_by_gid(origin_gid)

        # print(arrival_area)

    def test_get_departure_area_detail(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = Auth(key, secret, 1)

        rp = VasttrafikPlanTrip()
        rp.configuration.access_token = auth.token

        origin = rp.get_location_by_text("Stigberget", types="stoparea", limit=1)

        origin_gid = origin[0].results[0].gid

        departure_area = rp.get_stop_areas_departures_by_gid(origin_gid)

        detail_ref = departure_area[0].results[0].details_reference

        details = rp.get_stop_areas_departures_by_gid_details(details_reference=detail_ref, stop_area_gid=origin_gid)

        # print(details)

    def test_get_departure_stop_point(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = Auth(key, secret, 1)

        rp = VasttrafikPlanTrip()
        rp.configuration.access_token = auth.token

        origin = rp.get_location_by_text("Rönnäng", limit=1)

        origin_gid = origin[0].results[0].gid

        departure_area = rp.get_stop_areas_departures_by_gid(origin_gid)

        first_area = departure_area[0].results[0].stop_point.gid

        departure_point = rp.get_stop_points_departures(first_area)

        # print(departure_point)

    def test_get_arrival_stop_point(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = Auth(key, secret, 1)

        rp = VasttrafikPlanTrip()
        rp.configuration.access_token = auth.token

        origin = rp.get_location_by_text("Rönnäng", limit=1)

        origin_gid = origin[0].results[0].gid

        departure_area = rp.get_stop_areas_departures_by_gid(origin_gid)

        first_area = departure_area[0].results[0].stop_point.gid

        arrival_point = rp.get_stop_points_arrivals(first_area)

        # print(arrival_point)

    def test_get_departure_stop_point_detail(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = Auth(key, secret, 1)

        rp = VasttrafikPlanTrip()
        rp.configuration.access_token = auth.token

        origin = rp.get_location_by_text("Rönnäng", limit=1)

        origin_gid = origin[0].results[0].gid

        departure_area = rp.get_stop_areas_departures_by_gid(origin_gid)

        first_area = departure_area[0].results[0].stop_point.gid

        departure_point = rp.get_stop_points_departures(first_area)

        departure_point_ref = departure_point[0].results[0].details_reference

        departure_point_detail = rp.get_stop_point_departures_by_gid_details(departure_point_ref, departure_point)

        # print(departure_point_detail)

    def test_get_arrival_stop_point_detail(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = Auth(key, secret, 1)

        rp = VasttrafikPlanTrip()
        rp.configuration.access_token = auth.token

        origin = rp.get_location_by_text("Rönnäng", limit=1)

        origin_gid = origin[0].results[0].gid

        departure_area = rp.get_stop_areas_departures_by_gid(origin_gid)

        first_area = departure_area[0].results[0].stop_point.gid

        arrival_point = rp.get_stop_points_arrivals(first_area)

        arrival_point_ref = arrival_point[0].results[0].details_reference

        arrival_point_detail = rp.get_stop_point_departures_by_gid_details(arrival_point_ref, arrival_point)

        # print(arrival_point_detail)
