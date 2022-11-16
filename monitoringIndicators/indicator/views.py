from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .models import DiodIndicator
from .serializers import IndicatorSerializer
from .models import DiodIndicator


class IndicatorAPIList(generics.ListCreateAPIView):
    queryset = DiodIndicator.objects.all()
    serializer_class = IndicatorSerializer


def index(request):
    latest_value_indicator = DiodIndicator.objects.all()
    data = {
        'obj': {
            'Значение индикатора': latest_value_indicator[len(latest_value_indicator)-1].value
        }
    }
    return render(request, 'indicator/index.html', data)
