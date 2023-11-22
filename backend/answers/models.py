from django.db import models

from answers.enums import Reason
from answers.utils import get_lower_bound, get_open, get_upper_bound


class Answer(models.Model):
    REASON_CHOICES = (
        (Reason.CLOSED.name, Reason.CLOSED.value),
        (Reason.NEARLY_EMPTY.name, Reason.NEARLY_EMPTY.value),
        (Reason.FEW_PEOPLE.name, Reason.FEW_PEOPLE.value),
        (Reason.HALF_FULL.name, Reason.HALF_FULL.value),
        (Reason.CROWED.name, Reason.CROWED.value),
        (Reason.TOTALLY_FULL.name, Reason.TOTALLY_FULL.value),
    )

    status = models.CharField(max_length=12, choices=REASON_CHOICES)
    description = models.CharField(max_length=255)
    open = models.BooleanField(default=True)
    lower_bound = models.IntegerField(default=0)
    upper_bound = models.IntegerField(default=100)

    def clean(self) -> None:
        self.open = get_open(self.status)
        self.lower_bound = get_lower_bound(self.status)
        self.upper_bound = get_upper_bound(self.status)
        super().clean()
