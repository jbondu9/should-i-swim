from datetime import datetime, timezone

from rest_framework.viewsets import ReadOnlyModelViewSet

from pools.models import Pool
from pools.serializers import PoolSerializer

import requests

ONE_DAY = 1
FIFTEEN_MIN_IN_SECONDS = 15 * 60


class PoolViewset(ReadOnlyModelViewSet):
    serializer_class = PoolSerializer

    def fetch(self):
        response = requests.get(
            "https://opendata.bordeaux-metropole.fr/api/explore/v2.1/catalog/datasets/bor_frequentation_piscine_tr/records"
        )
        response.raise_for_status()
        return response.json()

    def is_opened(self, updated_at: datetime, entries: int) -> bool:
        # if the last update is greater than 1 day or if there is no entry during the day, we consider the swimming pool as closed
        if (
            datetime.now(timezone.utc) - updated_at.replace(tzinfo=timezone.utc)
        ).days >= ONE_DAY or entries == 0:
            return False
        return True

    def get_queryset(self):
        pools = Pool.objects.all().order_by("-updated_at")

        # if there no swimming pool in the database or the last update is greater than 15 minutes, we fetch the data
        if len(pools) == 0 or (
            len(pools) > 0
            and (
                datetime.now(timezone.utc)
                - pools[0].updated_at.replace(tzinfo=timezone.utc)
            ).seconds
            > FIFTEEN_MIN_IN_SECONDS
        ):
            data = self.fetch()

            for entry in data["results"]:
                updated_at = datetime.fromisoformat(entry["datemiseajour"])

                Pool.objects.update_or_create(
                    _id=entry["fmizonnum"],
                    defaults={
                        "_id": entry["fmizonnum"],
                        "pool_name": entry["fmizonlib"],
                        "swimming_pool_name": entry["etablissement_etalib"],
                        "current_capacity": entry["fmicourante"],
                        "maximum_capacity": entry["fmizonmax"],
                        "updated_at": updated_at,
                        "open": self.is_opened(updated_at, entry["entree"]),
                    },
                )

        return Pool.objects.all().order_by("swimming_pool_name")
