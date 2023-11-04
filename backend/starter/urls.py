from django.urls import include, path

from rest_framework.routers import SimpleRouter

from answers.views import AnswerViewset
from pools.views import PoolViewset

router = SimpleRouter()

router.register("answer", AnswerViewset, basename="answer")
router.register("pool", PoolViewset, basename="pool")

urlpatterns = [path("api/", include(router.urls))]
