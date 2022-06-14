from django.urls import path

from .models import *
from .views import *


urlpatterns = [
    ## Shipment ##
    path('get-shipment/<int:id>', ShipmentView.as_view({ 'get' : 'get_shipment' })),
    path('create-shipment', ShipmentView.as_view({ 'post' : 'create_shipment' })),
    path('get-shipment-status/<int:id>', ShipmentView.as_view({ 'get' : 'get_shipment_status' })),
    path('update-shipment/<int:id>', ShipmentView.as_view({ 'patch' : 'update_shipment' })),
    ## Shipment Label
    path('shipment-label/<int:id>', ShipmentLabelView.as_view({ 'get' : 'get_shipment_label' }))
]