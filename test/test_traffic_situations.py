import unittest
import aiohttp
import asyncio
import async_timeout
from datetime import datetime

from pyvasttrafik.vasttrafik_main import Auth, Vasttrafik
from pyvasttrafik.vasttrafik_situations import TrafficSituations


class TestAuth(unittest.TestCase):
    def test__auth(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")
        auth = Auth(key, secret, 1)

        # print(auth.token)


class TestTrafficSituations(unittest.TestCase):
    def test_init(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = Auth(key, secret, 1)

        ts = TrafficSituations()
        ts.configuration.access_token = auth.token
        url = ts.api_url

        # print(url)

    def test_get_traffic_situations(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = Auth(key, secret, 1)

        ts = TrafficSituations()
        ts.configuration.access_token = auth.token

        situations = ts.get_traffic_situations()

        # print(situations)

    def test_traffic_situations_number(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = Auth(key, secret, 1)

        ts = TrafficSituations()
        ts.configuration.access_token = auth.token

        situations = ts.get_traffic_situations()

        sn1 = situations[0][0].situation_number

        gid = situations[0][0].affected_lines[0].gid

        affected_line = ts.get_traffic_situations_line(gid=gid)

        # print(affected_line)

    def test_traffic_situations_stoppoint(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = Auth(key, secret, 1)

        ts = TrafficSituations()
        ts.configuration.access_token = auth.token

        situations = ts.get_traffic_situations()

        sn1 = situations[0][0].situation_number

        gid = situations[0][0].affected_lines[0].affected_stop_point_gids[0]

        affected_stoppoint = ts.get_traffic_situations_stoppoint(gid=gid)

        # print(affected_stoppoint)

    def test_traffic_situations_stoparea(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = Auth(key, secret, 1)

        ts = TrafficSituations()
        ts.configuration.access_token = auth.token

        situations = ts.get_traffic_situations()

        sn1 = situations[0][0].situation_number

        gid = situations[0][0].affected_stop_points[0].stop_area_gid

        affected_stoparea = ts.get_traffic_situations_stoparea(gid=gid)

        # print(affected_stoparea)

    def test_traffic_situations_journey(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        auth = Auth(key, secret, 1)

        ts = TrafficSituations()
        ts.configuration.access_token = auth.token

        situations = ts.get_traffic_situations()

        sn1 = situations
        y = 0
        # for x in sn1:
        #    gid = situations[y][0].affected_journeys
        #    print(gid)
        #    y = y + 1
        # affected_stoparea = ts.get_traffic_situations_stoparea(gid=gid)

        print(sn1)


