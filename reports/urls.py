from django.urls import path
from . import views

urlpatterns = [
    path('reports/download/<str:model>/', views.ViewPDF.as_view(), name='pdf_download'),
    #path('pdf_view/<str:model>/', views.ViewPDF.as_view(), name='pdf_view_default'),
]
