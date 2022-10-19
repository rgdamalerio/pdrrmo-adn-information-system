
from django.urls import path
from . import views


app_name = "aggregate"
urlpatterns = [
    path("", views.index, name="index"),
]

# urlpatterns = [
#     path("", views.some, name='some'),
# ]
