from rest_framework.viewsets import ReadOnlyModelViewSet

from pools.models import Pool
from pools.serializers import PoolDetailSerializer, PoolSerializer


class PoolViewset(ReadOnlyModelViewSet):
    serializer_class = PoolSerializer

    detail_serializer_class = PoolDetailSerializer

    def get_queryset(self):
        return Pool.objects.all().order_by("swimming_pool_name")

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()

    def update_pool_data(self, instance):
        if instance.has_to_be_refreshed:
            instance.set_refreshed_data()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        self.update_pool_data(instance)
        return super().retrieve(request, *args, **kwargs)
