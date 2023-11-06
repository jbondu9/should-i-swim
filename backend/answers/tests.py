from django.urls import reverse_lazy
from rest_framework.test import APITestCase

from answers.enums import Reason


class TestAnswer(APITestCase):
    url = reverse_lazy("answer-list")

    def test_list_without_params(self):
        response = self.client.get(self.url)

        data = response.json()

        expected_fields = ["reason_name", "reason_description"]

        self.assertEqual(response.status_code, 200)
        self.assertListEqual(list(data), expected_fields)

    def test_list_with_valid_params(self):
        response = self.client.get(self.url, data={"open": "true", "bound": "72.1"})

        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["reason_name"], Reason.CROWED.value)

    def test_list_with_invalid_params(self):
        response = self.client.get(self.url, data={"open": "foo", "bound": "bar"})

        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["reason_name"], Reason.CLOSED.value)

        response = self.client.get(self.url, data={"open": "true", "bound": "foo"})

        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIn(data["reason_name"], [r.value for r in Reason])
