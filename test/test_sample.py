import json
import unittest
from pyvasttrafik import vasttrafik


class TestAuthMethod(unittest.TestCase):
    def test_planner_auth(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        # print(key)
        # print(secret)

        auth = vasttrafik.Auth(key, secret, 1)

        # print(auth.token)

        rp = vasttrafik.Reseplaneraren()

        rp.api_client.configuration.access_token = auth.token

        # print(rp.locations_by_text_get("Åstol"))

    def test_locations(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        # print(key)
        # print(secret)

        auth = vasttrafik.Auth(key, secret, 1)

        # print(auth.token)

        rp = vasttrafik.Reseplaneraren()

        rp.api_client.configuration.access_token = auth.token

        data = rp.locations_by_text_get("Åstol")
        res = data.results[0]

        print(res.gid)

    def test_positions(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        lowleftlat = 57.72172
        lowleftlong = 12.011882
        upprightlat = 57.737549
        upprightlong = 12.039268
        # limit = 100

        auth = vasttrafik.Auth(key, secret, 1)

        # print(auth.token)

        rp = vasttrafik.Reseplaneraren()

        rp.api_client.configuration.access_token = auth.token

        # print(rp.positions_get(lowleftlat, lowleftlong, upprightlat, upprightlong))


if __name__ == '__main__':
    unittest.main()
