
from django.urls import path
from . import views 


app_name = "aggregate"
urlpatterns = [
    #path('', views.index, name='index'),
    path('export_aggregate_xls', views.exportFamilyandPopulation, name='export_aggregate'),
    #path('print_aggregate', views.print_aggregate, name="print_aggregate"),
    # path('<int:id>/generatePDF/', views.generatePDF, name='generatePDF'),
    #path('export_pdf', views.export_pdf, name='export_pdf'),
]

# urlpatterns = [
#     path("", views.some, name='some'),
# ]
