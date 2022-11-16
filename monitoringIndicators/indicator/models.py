from django.db import models


class DiodIndicator(models.Model):
    value = models.FloatField()
    time_create = models.DateTimeField(auto_now_add=True)
