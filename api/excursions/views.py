from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response


# Create your views here.
from rest_framework import viewsets
from . import serializers
from . import models


class ExcursionViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ExcursionSerializer
    queryset = models.Excursion.objects.raw(
        "SELECT * FROM excursions_excursion")
    lookup_field = 'sid'

    def retrieve(self, request, *args, **kwargs):
        excursion_id = kwargs.get('sid', None)
        instance = models.Excursion.objects.raw(
            'SELECT * FROM excursions_excursion WHERE excursions_excursion.sid\
             = %s', [excursion_id])
        serializer = self.get_serializer(instance[0])
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        excursion_id = kwargs.get('sid', None)
        partial = True
        instance = models.Excursion.objects.raw('SELECT * FROM \
                    excursions_excursion WHERE excursions_excursion.sid\
                    = %s', [excursion_id])
        serializer = self.get_serializer(instance[0], data=request.data,
                                         partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
