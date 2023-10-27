from django.db import models

from answers.enums import Reason


class Answer(models.Model):
    REASON_CHOICES = (
        (Reason.CLOSED, "CLOSED"),
        (Reason.NEARLY_EMPTY, "NEARLY_EMPTY"),
        (Reason.FEW_PEOPLE, "FEW_PEOPLE"),
        (Reason.HALF_FULL, "HALF_FULL"),
        (Reason.CROWED, "CROWED"),
        (Reason.TOTALLY_FULL, "TOTALLY_FULL"),
    )
    reason_name = models.CharField(max_length=12, choices=REASON_CHOICES)
    reason_description = models.CharField(max_length=255)
    open = models.BooleanField(default=True)
    lower_bound = models.IntegerField(default=0)
    upper_bound = models.IntegerField(default=100)
