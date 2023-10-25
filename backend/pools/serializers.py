from rest_framework.serializers import ModelSerializer

from pools.models import Pool


class PoolListSerializer(ModelSerializer):
    class Meta:
        model = Pool
        fields = ["_id", "swimming_pool_name", "pool_name"]


class PoolDetailSerializer(ModelSerializer):
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
