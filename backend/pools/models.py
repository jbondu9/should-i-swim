from datetime import datetime, timezone

import requests

from django.db import models

FIFTEEN_MIN_IN_SECONDS = 15 * 60
ONE_DAY = 1


class Pool(models.Model):
    _id = models.IntegerField(primary_key=True)

    photo = models.ImageField()
    pool_name = models.CharField(max_length=255)
    swimming_pool_name = models.CharField(max_length=255)

    is_opened = models.BooleanField(default=False)
    current_capacity = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    maximum_capacity = models.IntegerField(default=0)

    updated_at = models.DateTimeField()

    def get_refreshed_data(self):
        response = requests.get(
            f"https://opendata.bordeaux-metropole.fr/api/explore/v2.1/catalog/datasets/bor_frequentation_piscine_tr/records?select=fmizonnum%2C%20fmicourante%2C%20entree%2C%20datemiseajour&where=fmizonnum%20%3D%20{self._id}&limit=1"
        )
        response.raise_for_status()
        return response.json()

    def set_refreshed_data(self):
        data = self.get_refreshed_data()

        for entry in data["results"]:
            self.is_opened = (
                datetime.now(timezone.utc)
                - self.updated_at.replace(tzinfo=timezone.utc)
            ).days < ONE_DAY and entry["entree"] > 0

            self.current_capacity = (
                (entry["fmicourante"] / self.maximum_capacity) * 100
                if self.maximum_capacity > 0 and entry["fmicourante"] > 0
                else 0
            )

            self.updated_at = datetime.fromisoformat(entry["datemiseajour"])

            self.save()

    def has_to_be_refreshed(self):
        return (
            datetime.now(timezone.utc) - self.updated_at.replace(tzinfo=timezone.utc)
        ).seconds > FIFTEEN_MIN_IN_SECONDS
