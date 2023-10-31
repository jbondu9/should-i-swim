from rest_framework.viewsets import ReadOnlyModelViewSet

from pools.models import Pool
from pools.serializers import PoolSerializer, PoolDetailSerializer


class PoolViewset(ReadOnlyModelViewSet):
    serializer_class = PoolSerializer

    detail_serializer_class = PoolDetailSerializer

    def get_queryset(self):
        return Pool.objects.all().order_by("swimming_pool_name")

    def get_serializer_class(self):
        if self.action == "retrieve":
            instance = self.get_object()

            if instance.has_to_be_refreshed():
                instance.set_refresh_data()

            return self.detail_serializer_class
        return super().get_serializer_class()
