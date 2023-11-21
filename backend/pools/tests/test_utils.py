from datetime import datetime
from unittest.mock import patch

from django.test import TestCase

from pools.utils import time_difference_from_now

FAKE_NOW = datetime.fromisoformat("2023-10-31T17:14:12+00:00")
FAKE_ONE_DAY_BEFORE = datetime.fromisoformat("2023-10-30T12:23:53+00:00")


class UtilTestCase(TestCase):
    @patch("pools.utils.datetime")
    def test_time_difference_from_now(self, mock_datetime):
        mock_datetime.now.return_value = FAKE_NOW
        result = time_difference_from_now(FAKE_ONE_DAY_BEFORE)
        self.assertEqual(result.days, 1)
