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

    def test_locations_by_text(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = vasttrafik.Auth(key, secret, 1)

        rp = vasttrafik.Reseplaneraren()

        rp.api_client.configuration.access_token = auth.token

        data = rp.locations_by_text_get("Åstol")
        res = data.results[0]

        # print(res.gid)

    def test_locations_by_coordinates(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = vasttrafik.Auth(key, secret, 1)

        rp = vasttrafik.Reseplaneraren()

        rp.api_client.configuration.access_token = auth.token

        data = rp.locations_by_coordinates_get(57.924079, 11.589001)
        # res = data.results[0]

        # print(data)

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

    def test_departure_area_detail(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = vasttrafik.Auth(key, secret, 1)

        rp = vasttrafik.Reseplaneraren()

        rp.api_client.configuration.access_token = auth.token

        data = rp.locations_by_text_get("Åstol")
        res = data.results[0]
        # result = rp.stop_areas_stop_area_gid_departures_get(res.gid)
        result = rp.stop_points_stop_point_gid_departures_get('9022014015535001').results[0]

        detail = rp.stop_areas_stop_area_gid_departures_details_reference_details_get(result.details_reference,
                                                                                      '9022014015535001')

        # print(detail)

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

    def test_arrival_area_detail(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = vasttrafik.Auth(key, secret, 1)

        rp = vasttrafik.Reseplaneraren()

        rp.api_client.configuration.access_token = auth.token

        data = rp.locations_by_text_get("Åstol")
        res = data.results[0]
        # result = rp.stop_areas_stop_area_gid_departures_get(res.gid)
        result = rp.stop_points_stop_point_gid_arrivals_get('9022014015535001').results[0]

        detail = rp.stop_areas_stop_area_gid_arrivals_details_reference_details_get(result.details_reference,
                                                                                    'V3eyJUIjpbeyJSIjoiMXw2NDM1fDB8ODB8MzA5MjAyMyIsIkkiOjB9XX0')

        # print(detail)

    def test_departure_point(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = vasttrafik.Auth(key, secret, 1)

        rp = vasttrafik.Reseplaneraren()

        rp.api_client.configuration.access_token = auth.token

        result = rp.stop_points_stop_point_gid_departures_get('9022014015535001').results
        # stop = rp.stop_points_stop_point_gid_departures_get('9022014015535001').pagination

        # print(result)

    def test_departure_point_details(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = vasttrafik.Auth(key, secret, 1)

        rp = vasttrafik.Reseplaneraren()

        rp.api_client.configuration.access_token = auth.token

        result = rp.stop_points_stop_point_gid_departures_get('9022014015535001').results

        ref = result[0].details_reference
        stop = result[0].stop_point.gid

        details = rp.stop_points_stop_point_gid_departures_details_reference_details_get(ref, stop)

        # print(details)

    def test_arrival_point(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = vasttrafik.Auth(key, secret, 1)

        rp = vasttrafik.Reseplaneraren()

        rp.api_client.configuration.access_token = auth.token

        result = rp.stop_points_stop_point_gid_arrivals_get('9022014015535001').results

        # test = result.planned_time

        # print(test)

    def test_arrival_point_details(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = vasttrafik.Auth(key, secret, 1)

        rp = vasttrafik.Reseplaneraren()

        rp.api_client.configuration.access_token = auth.token

        result = rp.stop_points_stop_point_gid_arrivals_get('9022014015535001').results

        ref = result[0].details_reference
        stop = result[0].stop_point.gid

        details = rp.stop_points_stop_point_gid_arrivals_details_reference_details_get(ref, stop)

        # print(details)

    def test_journeys_get(self):
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

        # print(journey)

    def test_journeys_reconstruct(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = vasttrafik.Auth(key, secret, 1)

        rp = vasttrafik.Reseplaneraren()

        rp.api_client.configuration.access_token = auth.token

        data = rp.locations_by_text_get("Åstol")
        data2 = rp.locations_by_text_get("Rönnäng")
        res = data.results[0]
        res2 = data2.results[0]

        journey = rp.journeys_get(origin_gid=res.gid, destination_gid=res2.gid, limit=1).results[0]

        reconstruct = rp.journeys_reconstruct_get(journey.reconstruction_reference)

        # print(reconstruct)

    def test_journeys_details(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = vasttrafik.Auth(key, secret, 1)

        rp = vasttrafik.Reseplaneraren()

        rp.api_client.configuration.access_token = auth.token

        data = rp.locations_by_text_get("Åstol")
        data2 = rp.locations_by_text_get("Rönnäng")
        res = data.results[0]
        res2 = data2.results[0]

        journey = rp.journeys_get(origin_gid=res.gid, destination_gid=res2.gid, limit=1).results[0]

        details = rp.journeys_details_reference_details_get(journey.details_reference)

        # print(details)

    def test_journeys_valid_time_interval(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = vasttrafik.Auth(key, secret, 1)

        rp = vasttrafik.Reseplaneraren()

        rp.api_client.configuration.access_token = auth.token

        data = rp.locations_by_text_get("Åstol")
        data2 = rp.locations_by_text_get("Rönnäng")
        res = data.results[0]
        res2 = data2.results[0]

        interval = rp.journeys_valid_time_interval_get()

        # print(interval)

    def test_traffic_situations_auth(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = vasttrafik.Auth(key, secret, 1)

        ts = vasttrafik.TrafficSituations()

        ts.api_client.configuration.access_token = auth.token

        # print(ts.api_client.configuration.access_token)

    def test_traffic_situations_get(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = vasttrafik.Auth(key, secret, 1)

        ts = vasttrafik.TrafficSituations()

        ts.api_client.configuration.access_token = auth.token

        situation = ts.ts_v1_traffic_situations_get()

        # sn1 = situation[0].situation_number

        # print(situation)

    def test_traffic_situations_number(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = vasttrafik.Auth(key, secret, 1)

        ts = vasttrafik.TrafficSituations()

        ts.api_client.configuration.access_token = auth.token

        situation = ts.ts_v1_traffic_situations_get()

        sn1 = situation[0].situation_number

        sit_detail = ts.ts_v1_traffic_situations_by_situation_number_get(sn1)

        # print(sit_detail)

    def test_traffic_situations_journey_by_gid(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = vasttrafik.Auth(key, secret, 1)

        ts = vasttrafik.TrafficSituations()

        ts.api_client.configuration.access_token = auth.token

        situation = ts.ts_v1_traffic_situations_get()

        no_journeys = len(situation[0].affected_journeys)

        if no_journeys > 0:
            gid = situation[0].affected_journeys[0].gid
        else:
            gid = "No journey affected"

        # print(gid)

    def test_traffic_situations_stop_area_by_gid(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = vasttrafik.Auth(key, secret, 1)

        ts = vasttrafik.TrafficSituations()

        ts.api_client.configuration.access_token = auth.token

        situation = ts.ts_v1_traffic_situations_get()

        # no_journeys = len(situation[0].affected_journeys)
        stop_area_gid = situation[0].affected_stop_points[0].stop_area_gid

        affected_stop_area = ts.ts_v1_traffic_situations_stoparea_by_gid_get(stop_area_gid)

        # print(affected_stop_area)

    def test_traffic_situations_stop_point_by_gid(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = vasttrafik.Auth(key, secret, 1)

        ts = vasttrafik.TrafficSituations()

        ts.api_client.configuration.access_token = auth.token

        situation = ts.ts_v1_traffic_situations_get()

        # no_journeys = len(situation[0].affected_journeys)
        stop_point_gid = situation[0].affected_stop_points[0].gid

        affected_stop_point = ts.ts_v1_traffic_situations_stoppoint_by_gid_get(stop_point_gid)

        # print(affected_stop_point)

    def test_traffic_situations_stop_point_by_line(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = vasttrafik.Auth(key, secret, 1)

        ts = vasttrafik.TrafficSituations()

        ts.api_client.configuration.access_token = auth.token

        situation = ts.ts_v1_traffic_situations_get()

        # no_journeys = len(situation[0].affected_journeys)
        line_gid = situation[0].affected_lines[0].gid

        affected_line = ts.ts_v1_traffic_situations_line_by_gid_get(line_gid)

        print(affected_line)


if __name__ == '__main__':
    unittest.main()
