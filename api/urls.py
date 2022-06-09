from django.urls import path

from .models import *
from .views import *


urlpatterns = [
    path('create-shipment', ShipmentView.as_view({ 'post' : 'create_shipment' })),
]