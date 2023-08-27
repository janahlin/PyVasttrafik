import base64
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

        print(rp.locations_by_text_get("Åstol"))




if __name__ == '__main__':
    unittest.main()
