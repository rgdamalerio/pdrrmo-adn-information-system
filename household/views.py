from http.client import HTTPResponse
from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from household.models import Households
from django.core.exceptions import PermissionDenied, BadRequest

# Create your views here.
def household_datasets(request):
  if request.user.is_authenticated:
    # Do something for authenticated users.
    households = serialize('geojson',Households.objects.all())
    return HttpResponse(households,content_type='json')
  else:
    # Do something for anonymous users.
    raise PermissionDenied()

def search_households(request):
  if request.method == 'POST':
    if request.user.is_authenticated:
      # Do something for authenticated users.
      pass
    else:
      # Do something for anonymous users.
      raise PermissionDenied()
  else:
      raise BadRequest() 