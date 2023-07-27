from reports.models import FloodReport, LandslideReport, StormSurgeReport
from library.models import Municipalities
from django.utils.deprecation import MiddlewareMixin

class ReportsMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        if user.is_authenticated:
            if user.is_superuser or user.groups.filter(name='admin').exists():
                pass  # superusers and admin group can see all households
            else:
                try:
                    user_location = user.userlocation
                    matching_municipality = Municipalities.objects.get(munname=user_location.psgccode_mun)
                    flood = FloodReport.objects.filter(municipality_name=matching_municipality)
                    storm_surge = StormSurgeReport.objects.filter(municipality_name=matching_municipality)
                    landslide = LandslideReport.objects.filter(municipality_name=matching_municipality)
                    request.flood = flood
                    request.storm_surge = storm_surge
                    request.landslide = landslide
                 
                except Municipalities.DoesNotExist:
                    request.flood = FloodReport.objects.none()
                    request.storm_surge = StormSurgeReport.objects.none()
                    request.landslide = LandslideReport.objects.none()

        response = self.get_response(request)
        return response
