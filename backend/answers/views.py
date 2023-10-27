from rest_framework.viewsets import ReadOnlyModelViewSet

from answers.models import Answer
from answers.serializers import AnswerSerializer


class AnswerViewset(ReadOnlyModelViewSet):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        queryset = Answer.objects.all()

        open = self.request.query_params.get("open")
        bound = self.request.query_params.get("bound")

        if open is not None:
            queryset = queryset.filter(open=False if open == "false" else True)

        if bound is not None:
            queryset = queryset.filter(
                lower_bound__lt=float(bound), upper_bound__gte=float(bound)
            )

        return queryset
