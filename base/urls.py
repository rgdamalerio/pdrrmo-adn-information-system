from django.urls import path
from . import views


urlpatterns = [
    path('',views.getRoutes, name="routes"),
    path('persons/',views.getPersons, name="persons"),
    path('persons/<str:pk>/',views.getPerson, name="person"),
    path('households/',views.getHousehold, name="householapi"),
    path('aggregate/',views.getAggregaredHousehold, name="aggregate"),
    path('polygons/',views.getFlood, name="flood"),
    path('municipal/',views.getMunicipal, name="municipal"),
    path('barangay/',views.getBarangay, name="barangay"),
    path('households/<str:pk>/brgy/',views.getBrgy, name="households-barangay"),
    path('households/<str:pk>/info/',views.getHouseholdInfo, name="households-info"),
    path('households/permun/',views.getHouseholdPerMun, name="households-per-mun"),
    path('family/permun/',views.getFamilyPerMun, name="family-per-mun"),
    path('brgy/<str:pk>/info/',views.getBrgyInfo, name="brgy-info"),
    path('reports/',views.getTotalReport, name="total-report"),
    path('reports/flood/<str:pk>/',views.getFloodReportPerBarangay, name="flood-report"),
    path('flood/<str:pk>/info/',views.getFloodHazardInfo, name="flood-info"),
    path('flood/',views.getOverAllFloodReport, name="flood-over-all"),
    path('point/<str:pk>/senior/',views.getpointsenior, name="point-senior"),
]