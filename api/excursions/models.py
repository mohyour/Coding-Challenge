from django.db import models
from django_mysql.models import ListCharField


# Create your models here.
class Excursion(models.Model):
    sid = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=90)
    detailPageName = models.CharField(max_length=90)
    portID = models.CharField(max_length=90)
    type = models.CharField(max_length=90)
    typology = ListCharField(
        base_field=models.CharField(max_length=90),
        max_length=90
    )
    activityLevel = models.CharField(max_length=90)
    collectionType = models.CharField(max_length=90)
    duration = models.TextField()
    language = ListCharField(
        base_field=models.CharField(max_length=90),
        max_length=90
    )
    priceLevel = models.IntegerField()
    currency = models.CharField(max_length=90)
    mealInfo = models.CharField(max_length=90, blank=True)
    status = models.CharField(max_length=90)
    shortDescription = models.CharField(max_length=100, blank=True)
    longDescription = models.TextField()
    externalContent = models.BooleanField()
    minimumAge = models.CharField(max_length=90, blank=True)
    wheelChairAccessible = models.BooleanField()
    featured = models.BooleanField()

    def __str__(self):
        return "{} - {}".format(self.name, self.detailPageName)
