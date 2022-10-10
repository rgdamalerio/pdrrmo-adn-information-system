from django.urls import path

from .views import household_datasets, household_search_form, household_info

urlpatterns = [
    path('household_data/', household_datasets, name='household'),  
    path('household_info/', household_info, name='householdinfo'),  
    path('household_search_form/', household_search_form, name='household_search_form'),  
]