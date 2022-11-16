from django.urls import path
from indicator.views import *

urlpatterns = [
    path('', index),
    path('api/indicators_request', IndicatorAPIList.as_view()),

]