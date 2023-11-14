from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any

import requests

from pools.utils import time_difference_from_now

ONE_DAY = 1
OPEN_DATA_BORDEAUX_URL = "https://opendata.bordeaux-metropole.fr/api/explore/v2.1/catalog/datasets/bor_frequentation_piscine_tr/records"


class OpenDataProvider(ABC):
    def __init__(self, url: str) -> None:
        self.url = url

    def fetch_data(self) -> Any:
        response = requests.get(self.url)
        response.raise_for_status()
        return response.json()

    @abstractmethod
    def parse_data(self, data: Any):
        pass


class OpenDataBordeauxProvider(OpenDataProvider):
    def __init__(self) -> None:
        super().__init__(OPEN_DATA_BORDEAUX_URL)

    @staticmethod
    def parse_datetime(date: str) -> datetime:
        return datetime.fromisoformat(date)

    @staticmethod
    def is_opened(updated_at: datetime, nb_entries: int) -> bool:
        return time_difference_from_now(updated_at).days < ONE_DAY and nb_entries > 0

    @staticmethod
    def current_capacity(nb_entries: int, maximum_capacity: int) -> float:
        result = 0.0
        if nb_entries >= 0 and maximum_capacity > 0:
            result = (nb_entries / maximum_capacity) * 100
        return result

    def parse_data(self, data: Any):
        for entry in data["results"]:
            updated_at = self.parse_datetime(entry["datemiseajour"])

            yield {
                "_id": entry["fmizonnum"],
                "swimming_pool": entry["etablissement_etalib"],
                "basin": entry["fmizonlib"],
                "is_opened": self.is_opened(updated_at, entry["entree"]),
                "current_capacity": self.current_capacity(
                    entry["fmicourante"], entry["fmizonmax"]
                ),
                "maximum_capacity": entry["fmizonmax"],
                "updated_at": updated_at,
            }
