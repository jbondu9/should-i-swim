from rest_framework.serializers import ModelSerializer

from pools.models import Pool


class PoolSerializer(ModelSerializer):
    class Meta:
        model = Pool
        fields = ["_id", "swimming_pool", "basin"]


class PoolDetailSerializer(ModelSerializer):
    class Meta:
        model = Pool
        fields = [
            "_id",
            "swimming_pool",
            "basin",
            "is_opened",
            "current_capacity",
            "maximum_capacity",
            "updated_at",
        ]
