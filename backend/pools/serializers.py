from rest_framework.serializers import ModelSerializer

from pools.models import Pool


class PoolSerializer(ModelSerializer):
    class Meta:
        model = Pool
        fields = ["_id", "pool_name", "swimming_pool_name"]


class PoolDetailSerializer(ModelSerializer):
    class Meta:
        model = Pool
        fields = [
            "_id",
            "pool_name",
            "swimming_pool_name",
            "is_opened",
            "current_capacity",
            "maximum_capacity",
            "updated_at",
        ]
