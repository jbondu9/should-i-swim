from datetime import datetime, timezone

from factory.django import DjangoModelFactory
from factory import Sequence

from pools.models import Pool


class PoolFactory(DjangoModelFactory):
    class Meta:
        model = Pool

    _id = Sequence(lambda x: x)
    swimming_pool = Sequence(lambda x: f"swimming_pool_{x}")
    basin = Sequence(lambda x: f"basin_{x}")

    is_opened = False
    current_capacity = 0.00
    maximum_capacity = 200

    updated_at = datetime.today().astimezone(timezone.utc)
