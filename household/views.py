from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Households
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_http_methods
from .forms import HouseholdSearchForm

@require_http_methods(["GET"])
def household_datasets(request):
  
  if request.user.is_authenticated:
    # Do something for authenticated users.
    print(request.GET)
    filter_params = {}
    if request.GET.get('controlnumber'):
      filter_params['controlnumber'] = request.GET.get('controlnumber')
    elif request.GET.get('purok'):
      filter_params['purok'] = request.GET.get('purok')
    else:
      pass

    households = serialize('geojson',Households.objects.filter(**filter_params))
    return HttpResponse(households,content_type='json')
   
  else:
    # Do something for anonymous users.
    raise PermissionDenied()

#AJAX
@require_http_methods(["GET"])
def household_search_form(request):
  if request.user.is_authenticated:
    # Do something for authenticated users.
    form = HouseholdSearchForm()
    context = {'form':form}
    return render(request,'household/household_search_form.html',context)
  else:
    # Do something for anonymous users.
    raise PermissionDenied()
