from django.db import models


class record(models.Model):
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    contact = models.IntegerField()
