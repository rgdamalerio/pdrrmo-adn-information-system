
from django.urls import path
from . import views 


app_name = "aggregate"
urlpatterns = [
    path('chart-data', views.chart_view, name='chart_data'),
    path('export_aggregate_xls', views.exportFamilyandPopulation, name='export_aggregate'),
    path('population_data', views.get_data, name='population_data'),
]
    #path('print_aggregate', views.print_aggregate, name="print_aggregate"),
    # path('<int:id>/generatePDF/', views.generatePDF, name='generatePDF'),
    #path('export_pdf', views.export_pdf, name='export_pdf'),
     #path('aggregated_data', views.aggregated_data, name='aggregated_data'),
