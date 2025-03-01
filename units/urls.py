# units/urls.py

from django.urls import path
from .views import ConversionViewSet

urlpatterns = [
    path('convert/', ConversionViewSet.as_view({'post': 'convert'}), name='convert'),
    path('convert/batch/', ConversionViewSet.as_view({'post': 'batch_convert'}), name='batch_convert'),
    path('supported-units/<str:unit_type>/', ConversionViewSet.as_view({'get': 'supported_units'}), name='supported_units'),
    # Add more paths as needed
]