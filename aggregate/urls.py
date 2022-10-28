
from django.urls import path
from . import views


app_name = "aggregate"
urlpatterns = [
    path("", views.index, name="index"),
    # path('<int:id>/generatePDF/', views.generatePDF, name='generatePDF'),
    #path('export_pdf', views.export_pdf, name='export_pdf'),
]

# urlpatterns = [
#     path("", views.some, name='some'),
# ]
