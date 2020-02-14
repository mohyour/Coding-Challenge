from rest_framework import serializers
from . import models

class ExcursionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Excursion
        fields = "__all__"
