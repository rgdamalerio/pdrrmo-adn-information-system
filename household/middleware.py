from .models import Households, Demographies, Hhlivelihoods, Availprograms
from library.models import Municipalities
from django.utils.deprecation import MiddlewareMixin

class HouseholdsMiddleware(MiddlewareMixin):
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
                    households = Households.objects.filter(municipality=matching_municipality.psgccode)
                    demographies = Demographies.objects.filter(controlnumber__in=households.values_list('controlnumber', flat=True))
                    hlivelihoods = Hhlivelihoods.objects.filter(controlnumber__in=households.values_list('controlnumber', flat=True))
                    availprograms = Availprograms.objects.filter(controlnumber__in=households.values_list('controlnumber', flat=True))
                    request.households = households
                    request.demographies = demographies
                   
                    request.livelihoods = hlivelihoods
                    request.availprograms = availprograms
                except Municipalities.DoesNotExist:
                    request.households = Households.objects.none()

        response = self.get_response(request)
        return response
