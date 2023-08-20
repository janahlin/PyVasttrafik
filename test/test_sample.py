import unittest
from pyvasttrafik import vasttrafik


class TestAuthMethod(unittest.TestCase):
    def test_planner_auth(self):
        with open("credentials.csv", "r") as f:
            key, secret = f.read().split(",")

        config = vasttrafik.Configuration.get_default_copy()

        rest_client = pyvasttrafik.api.rest.RESTClientObject(config)
        default_headers = {}

        user_agent = 'OpenAPI-Generator/1.0.0/python'
        client_side_validation = config.client_side_validation

        print(rest_client)


if __name__ == '__main__':
    unittest.main()
