from django.urls import path
from .views import export_infant_counts

urlpatterns = [
    path('num_infants/', export_infant_counts, name='num_infants')
]
