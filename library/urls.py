from django.urls import path

from .views import barangay_list

urlpatterns = [
    path('barangay/<str:municipality_id>/', barangay_list, name='barangay'),  
]