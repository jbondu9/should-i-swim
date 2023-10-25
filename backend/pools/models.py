from django.db import models


class Pool(models.Model):
    _id = models.IntegerField(primary_key=True)
    pool_name = models.CharField(max_length=255)
    swimming_pool_name = models.CharField(max_length=255)

    open = models.BooleanField(default=False)
    current_capacity = models.IntegerField(default=0)
    maximum_capacity = models.IntegerField(default=0)

    updated_at = models.DateTimeField(auto_now=True)
