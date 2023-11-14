from rest_framework.viewsets import ReadOnlyModelViewSet

from pools.models import Pool
from pools.serializers import PoolDetailSerializer, PoolSerializer


class PoolViewset(ReadOnlyModelViewSet):
    serializer_class = PoolSerializer
    detail_serializer_class = PoolDetailSerializer

    def get_queryset(self):
        return Pool.objects.all().order_by("swimming_pool")

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()
