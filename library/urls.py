from django.urls import path
from .views import municipality_list, barangay_list, purok_list

urlpatterns = [
    path('municipality/', municipality_list, name='municipality_list'),
    path('barangay/<str:municipality_id>/', barangay_list, name='barangay'), 
    path('purok/<str:barangay_id>/', purok_list, name='purok'),
]