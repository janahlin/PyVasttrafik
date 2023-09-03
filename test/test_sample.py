import json
import unittest
from pyvasttrafik import vasttrafik


class TestAuthMethod(unittest.TestCase):
    def test_planner_auth(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = vasttrafik.Auth(key, secret, 1)

        rp = vasttrafik.Reseplaneraren()

        rp.api_client.configuration.access_token = auth.token

        # print(rp.locations_by_text_get("Åstol"))

    def test_locations(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = vasttrafik.Auth(key, secret, 1)

        rp = vasttrafik.Reseplaneraren()

        rp.api_client.configuration.access_token = auth.token

        data = rp.locations_by_text_get("Åstol")
        res = data.results[0]

        # print(res.gid)

    def test_positions(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        lowleftlat = 57.72172
        lowleftlong = 12.011882
        upprightlat = 57.737549
        upprightlong = 12.039268
        # limit = 100

        auth = vasttrafik.Auth(key, secret, 1)

        rp = vasttrafik.Reseplaneraren()

        rp.api_client.configuration.access_token = auth.token

        # print(rp.positions_get(lowleftlat, lowleftlong, upprightlat, upprightlong))

    def test_departure_area(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = vasttrafik.Auth(key, secret, 1)

        rp = vasttrafik.Reseplaneraren()

        rp.api_client.configuration.access_token = auth.token

        data = rp.locations_by_text_get("Åstol")
        res = data.results[0]

        result = rp.stop_areas_stop_area_gid_departures_get(res.gid)

        # print(result)

    def test_arrival_area(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = vasttrafik.Auth(key, secret, 1)

        rp = vasttrafik.Reseplaneraren()

        rp.api_client.configuration.access_token = auth.token

        data = rp.locations_by_text_get("Åstol")
        res = data.results[0]

        result = rp.stop_areas_stop_area_gid_arrivals_get(res.gid)

        # print(result)

    def test_departure_point(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = vasttrafik.Auth(key, secret, 1)

        rp = vasttrafik.Reseplaneraren()

        rp.api_client.configuration.access_token = auth.token

        result = rp.stop_points_stop_point_gid_departures_get('9022014015535001').results

        # test = result.planned_time

        # print(test)

    def test_arrival_point(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = vasttrafik.Auth(key, secret, 1)

        rp = vasttrafik.Reseplaneraren()

        rp.api_client.configuration.access_token = auth.token

        result = rp.stop_points_stop_point_gid_arrivals_get('9022014015535001').results

        # test = result.planned_time

        # print(test)

    def test_journeys(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = vasttrafik.Auth(key, secret, 1)

        rp = vasttrafik.Reseplaneraren()

        rp.api_client.configuration.access_token = auth.token

        data = rp.locations_by_text_get("Åstol")
        data2 = rp.locations_by_text_get("Rönnäng")
        res = data.results[0]
        res2 = data2.results[0]

        journey = rp.journeys_get(origin_gid=res.gid, destination_gid=res2.gid, limit=1)

        print(journey)


if __name__ == '__main__':
    unittest.main()
