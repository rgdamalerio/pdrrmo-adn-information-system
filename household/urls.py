from django.urls import path

from .views import household_datasets

urlpatterns = [
    path('household_data/', household_datasets, name='household'),  
]