from datetime import datetime

from django.urls import reverse, reverse_lazy

from rest_framework.test import APITestCase

from unittest.mock import patch

from pools.mocks import (
    CURRENT_CAPACITY,
    FAKE_POOL,
    MAXIMUM_CAPACITY,
    NOW,
    UPDATED_AT,
    mock_get_refreshed_data,
)
from pools.models import Pool


class TestPool(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.pool = Pool.objects.create(
            _id=FAKE_POOL["_id"],
            pool_name=FAKE_POOL["pool_name"],
            swimming_pool_name=FAKE_POOL["swimming_pool_name"],
            maximum_capacity=FAKE_POOL["maximum_capacity"],
            updated_at=FAKE_POOL["updated_at"],
        )

    def get_pool_detail(self, pool: Pool):
        return {
            "_id": pool._id,
            "pool_name": pool.pool_name,
            "swimming_pool_name": pool.swimming_pool_name,
            "is_opened": pool.is_opened,
            "current_capacity": f"{pool.current_capacity:.2f}",
            "maximum_capacity": pool.maximum_capacity,
            "updated_at": datetime.fromisoformat(pool.updated_at).strftime(
                "%Y-%m-%dT%H:%M:%SZ"
            ),
        }

    def test_list(self):
        response = self.client.get(reverse_lazy("pool-list"))

        self.assertEqual(response.status_code, 200)

        expected_fields = ["_id", "pool_name", "swimming_pool_name"]

        for entry in response.json():
            self.assertListEqual(list(entry.keys()), expected_fields)

    def test_create(self):
        pool_count = Pool.objects.count()

        response = self.client.post(
            reverse_lazy("pool-list"),
            data={
                "_id": 300,
                "pool_name": "Exterieur",
                "swimming_pool_name": "Piscine Stehelin",
            },
        )

        self.assertEqual(response.status_code, 405)
        self.assertEqual(Pool.objects.count(), pool_count)

    @patch("pools.models.datetime")
    def test_detail_without_update(self, mock_datetime):
        mock_datetime.now.return_value = datetime.fromisoformat(UPDATED_AT)

        response = self.client.get(reverse("pool-detail", kwargs={"pk": self.pool.pk}))

        self.assertEqual(self.pool._id, self.pool.pk)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.get_pool_detail(self.pool), response.json())

    @patch("pools.models.datetime")
    @patch("pools.models.Pool.get_refreshed_data", mock_get_refreshed_data)
    def test_detail_with_update(self, mock_datetime):
        mock_datetime.now.return_value = datetime.fromisoformat(NOW)
        mock_datetime.fromisoformat = lambda *args, **kw: datetime.fromisoformat(
            *args, **kw
        )

        response = self.client.get(reverse("pool-detail", kwargs={"pk": self.pool.pk}))

        self.pool.is_opened = True
        self.pool.current_capacity = (CURRENT_CAPACITY / MAXIMUM_CAPACITY) * 100
        self.pool.updated_at = NOW

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.get_pool_detail(self.pool), response.json())
