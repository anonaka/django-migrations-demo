from django.db import models

# Create your models here.


class SampleModel1(models.Model):
    name = models.CharField(max_length=200)
    # address = models.CharField(max_length=500, null=True)
    # age = models.IntegerField(null=True)
