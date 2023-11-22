from django.urls import reverse_lazy
from rest_framework.test import APITestCase

from answers.enums import Reason
from answers.tests import factories


class AnswerViewsetTestCase(APITestCase):
    url = reverse_lazy("answer-list")

    def setUp(self):
        factories.AnswerFactory(status=Reason.CROWED.name)
        factories.AnswerFactory(status=Reason.CLOSED.name)

    def test_list_without_params(self):
        response = self.client.get(self.url)

        data = response.json()

        expected_fields = ["status", "description"]

        self.assertEqual(response.status_code, 200)
        self.assertListEqual(list(data), expected_fields)

    def test_list_with_valid_params(self):
        response = self.client.get(self.url, data={"open": "true", "bound": "72.1"})

        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["status"], Reason.CROWED.value)

    def test_list_with_invalid_params(self):
        response = self.client.get(self.url, data={"open": "foo", "bound": "bar"})

        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["status"], Reason.CLOSED.value)

        response = self.client.get(self.url, data={"open": "true", "bound": "foo"})

        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIn(data["status"], [r.value for r in Reason])
