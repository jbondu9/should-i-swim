from django.db import models


class Pool(models.Model):
    _id = models.IntegerField(primary_key=True)

    swimming_pool = models.CharField(max_length=255)
    basin = models.CharField(max_length=255)

    is_opened = models.BooleanField(default=False)
    current_capacity = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    maximum_capacity = models.IntegerField(default=0)

    updated_at = models.DateTimeField()
