_ID = 200

MAXIMUM_CAPACITY = 200
CURRENT_CAPACITY = 111

UPDATED_AT = "2023-10-31T17:14:00+00:00"
NOW = "2023-10-31T17:42:31+00:00"

FAKE_POOL = {
    "_id": _ID,
    "pool_name": "Exterieur",
    "swimming_pool_name": "Piscine Stehelin",
    "maximum_capacity": MAXIMUM_CAPACITY,
    "updated_at": UPDATED_AT,
}


def mock_get_refreshed_data(self):
    return {
        "total_count": 1,
        "results": [
            {
                "fmizonnum": _ID,
                "entree": 541,
                "fmicourante": CURRENT_CAPACITY,
                "datemiseajour": NOW,
            }
        ],
    }
