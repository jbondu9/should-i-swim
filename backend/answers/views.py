from random import choice

from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.viewsets import ReadOnlyModelViewSet

from answers.models import Answer
from answers.serializers import AnswerSerializer


class AnswerViewset(ReadOnlyModelViewSet):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        queryset = Answer.objects.all()

        open_param = self.request.query_params.get("open")
        bound_param = self.request.query_params.get("bound")

        if open_param is not None:
            is_open = open_param.lower() == "true"
            queryset = queryset.filter(open=is_open)

        if bound_param is not None:
            try:
                bound_value = float(bound_param)
                queryset = queryset.filter(
                    lower_bound__lt=bound_value, upper_bound__gte=bound_value
                )
            except ValueError:
                pass

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if queryset.exists():
            random_answer = choice(queryset)
            serializer = self.get_serializer(random_answer)
            return Response(serializer.data)
        else:
            return Response({"message": "No answers found."}, status=HTTP_404_NOT_FOUND)
