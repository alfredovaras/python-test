import unittest, requests
import unittest.mock
from src.api_client import get_location
from unittest.mock import patch


class ApiClientTests(unittest.TestCase):

    @patch('src.api_client.requests.get')
    def test_get_location_returns_expected_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'countryName': 'USA',
            'regionName': 'Miami',
            'cityName': 'Florida',
            'countryCode': 'US',
            'language': 'en'
        }
        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"),'USA')
        self.assertEqual(result.get("region"),'Miami')
        self.assertEqual(result.get("city"),'Florida')
        self.assertEqual(result.get("code"),'US')
        self.assertEqual(result.get("language"),'en')

        mock_get.assert_called_once_with('https://freeipapi.com/api/json/8.8.8.8')

    @patch('src.api_client.requests.get')
    def test_get_location_returns_side_effect(self, mock_get):
        mock_get.side_effect = [
            requests.exceptions.RequestException("Service Unavailable"),
            unittest.mock.Mock(
                status_code=200,
                json=lambda: {
                    'countryName': 'USA',
                    'regionName': 'Miami',
                    'cityName': 'Florida',
                    'countryCode': 'US',
                    'language': 'en'
                }
            )
            ]


        with self.assertRaises(requests.exceptions.RequestException):
             get_location("8.8.8.8")

        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"),'USA')
        self.assertEqual(result.get("region"),'Miami')
        self.assertEqual(result.get("city"),'Florida')
        self.assertEqual(result.get("code"),'US')
        self.assertEqual(result.get("language"),'en')

    @patch('src.api_client.requests.get')
    def test_get_location_returns_ip_invalid(self, mock_get):
        mock_get.side_effect = [
            requests.exceptions.HTTPError("Not Found"),
            unittest.mock.Mock(
                status_code=200,
                json=lambda: {
                    'countryName': 'USA',
                    'regionName': 'Miami',
                    'cityName': 'Florida',
                    'countryCode': 'US',
                    'language': 'en'
                }
            )
            ]


        with self.assertRaises(requests.exceptions.HTTPError):
             get_location("8.8.8.8")

        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"),'USA')
        self.assertEqual(result.get("region"),'Miami')
        self.assertEqual(result.get("city"),'Florida')
        self.assertEqual(result.get("code"),'US')
        self.assertEqual(result.get("language"),'en')
