from django.urls import path
from .views import get_infant_counts

urlpatterns = [
    path('num_infants/', get_infant_counts, name='num_infants')
]
