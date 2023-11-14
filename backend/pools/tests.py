from datetime import datetime

from django.urls import reverse, reverse_lazy
from rest_framework.test import APITestCase

from pools.models import Pool


class TestPool(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.pool = Pool.objects.create(
            _id=2,
            swimming_pool="Piscine Stehelin",
            basin="Exterieur",
            is_opened=False,
            current_capacity=0.0,
            maximum_capacity=200,
            updated_at="2023-11-14T16:26:31+00:00",
        )

    @staticmethod
    def get_pool_detail(pool: Pool):
        return {
            "_id": pool._id,
            "swimming_pool": pool.swimming_pool,
            "basin": pool.basin,
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

        expected_fields = ["_id", "swimming_pool", "basin"]

        for entry in response.json():
            self.assertListEqual(list(entry.keys()), expected_fields)

    def test_create(self):
        pool_count = Pool.objects.count()

        response = self.client.post(
            reverse_lazy("pool-list"),
            data={
                "_id": 3,
                "swimming_pool": "Piscine Stehelin",
                "basin": "Exterieur",
            },
        )

        self.assertEqual(response.status_code, 405)
        self.assertEqual(Pool.objects.count(), pool_count)

    def test_detail(self):
        response = self.client.get(reverse("pool-detail", kwargs={"pk": self.pool.pk}))

        self.assertEqual(self.pool._id, self.pool.pk)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.get_pool_detail(self.pool), response.json())
