from rest_framework.serializers import ModelSerializer

from pools.models import Pool


class PoolSerializer(ModelSerializer):
    class Meta:
        model = Pool
        fields = [
            "swimming_pool_name",
            "pool_name",
            "open",
            "maximum_capacity",
            "current_capacity",
            "updated_at",
        ]
