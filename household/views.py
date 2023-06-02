from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Households
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_http_methods
from .forms import HouseholdSearchForm
from .serializers import HouseholdSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from aggregate.models import AggregatedFamiliesandPopulation
from django.db.models import Sum
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import Households

def is_valid_queryparam(param):
    return param != '' and param is not None

@require_http_methods(["GET"])
def household_datasets(request):
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.groups.filter(name='admin').exists():
            # Return all households for superusers and admin group
            qs = Households.objects.all()
        else:
            # Filter households based on the user's municipality
            municipality = request.user.userlocation.psgccode_mun
            qs = Households.objects.filter(municipality=municipality)
        
        controlnumber_icontains_query = request.GET.get('controlnumber')
        purok_fk_icontains_query = request.GET.get('purok_fk')

        if controlnumber_icontains_query:
            qs = qs.filter(controlnumber__icontains=controlnumber_icontains_query)

        if purok_fk_icontains_query:
            qs = qs.filter(purok__icontains=purok_fk_icontains_query)

        # ... add the rest of your filter conditions here
        
        households = serialize('geojson', qs, use_natural_foreign_keys=True, fields=('pk', 'location', 'latitude', 'longitude'))

        return HttpResponse(households, content_type='application/json')
    
    else:
        qs = Households.objects.none()
        return HttpResponse(qs, content_type='application/json')


#AJAX
@require_http_methods(["GET"])
@api_view(['GET'])
def household_info(request):
  if request.user.is_authenticated:
    # # Do something for authenticated users.

    qs = Households.objects.get(pk=request.GET.get('pk'))
    serialize = HouseholdSerializer([qs],many=True)
    return Response(serialize.data)
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

#AJAX
@require_http_methods(['POST'])
def chart_view(request):
  if request.user.is_authenticated:
    qresult = AggregatedFamiliesandPopulation.objects.values('munname').annotate(
        total_households=Sum('households'),
        total_male=Sum('male'),
        total_female=Sum('female'),
        total_male_infant=Sum('male_infant'),
        total_female_infant=Sum('female_infant'),
        total_male_children=Sum('male_children'),
        total_female_children=Sum('female_children'),
        total_male_adult=Sum('male_adult'),
        total_female_adult=Sum('female_adult'),
        total_male_elderly=Sum('male_elderly'),
        total_female_elderly=Sum('female_elderly'),
        total_ip_male=Sum('ip_male'),
        total_ip_female=Sum('ip_female')
    )
    labels = []
    data = []
    for item in qresult:
        labels.append(item['munname'])
        data.append([
            item['total_households'],
            item['total_male'],
            item['total_female'],
            item['total_male_infant'],
            item['total_female_infant'],
            item['total_male_children'],
            item['total_female_children'],
            item['total_male_adult'],
            item['total_female_adult'],
            item['total_male_elderly'],
            item['total_female_elderly'],
            item['total_ip_male'],
            item['total_ip_female'],
        ])

    context = {'labels': labels, 'data': data}
    return render(request,'household/chart_view_content.html', context)
  else:
    # Do something for anonymous users.
    raise PermissionDenied()


