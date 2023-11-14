from pools.models import Pool
from pools.providers import OpenDataBordeauxProvider


def refresh_data_of_bordeaux():
    bordeaux_provider = OpenDataBordeauxProvider()

    raw_data = bordeaux_provider.fetch_data()
    parsed_data = bordeaux_provider.parse_data(raw_data)

    for data in parsed_data:
        Pool.objects.update_or_create(
            _id=data["_id"],
            defaults=data,
        )
