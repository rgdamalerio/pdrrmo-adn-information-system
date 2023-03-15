from django.urls import path

from .views import barangay_list, purok_list

urlpatterns = [
    path('barangay/<str:municipality_id>/', barangay_list, name='barangay'), 
    path('purok/<str:barangay_id>/', purok_list, name='purok'),
]