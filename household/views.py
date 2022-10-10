from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Households
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_http_methods
from .forms import HouseholdSearchForm
from django.db import connection

def is_valid_queryparam(param):
    return param != '' and param is not None

@require_http_methods(["GET"])
def household_datasets(request):
  
  if request.user.is_authenticated:
    # # Do something for authenticated users.
    # print(request.GET)

    qs = Households.objects.all()

    controlnumber_icontains_query = request.GET.get('controlnumber')
    purok_icontains_query = request.GET.get('purok')
    respondent_icontains_query = request.GET.get('respondent')
    enumerator_icontains_query = request.GET.get('enumerator')
    municipality_exact = request.GET.get('municipality')
    barangay_exact = request.GET.get('barangay')
    enumerator_icontains_query = request.GET.get('enumerator')
    editor_icontains_query = request.GET.get('editor')
    year_construct_exact_query = request.GET.get('year_construct')
    estimated_cost_exact_query = request.GET.get('estimated_cost')
    number_bedrooms_exact_query = request.GET.get('number_bedrooms')
    number_storey_exact_query = request.GET.get('number_storey')
    access_electricity = request.GET.getlist('access_electricity')
    access_internet = request.GET.getlist('access_internet')
    medical_treatment_icontains_query = request.GET.get('medical_treatment')
    access_water_supply = request.GET.getlist('access_water_supply')
    potable = request.GET.getlist('potable')
    floods_occur = request.GET.getlist('floods_occur')
    year_flooded_exact = request.GET.get('year_flooded')
    experience_evacuate = request.GET.getlist('experience_evacuate')
    year_evacuate_exact = request.GET.get('year_evacuate')
    access_health_medical_facility = request.GET.getlist('access_health_medical_facility')
    access_telecommuniciation = request.GET.getlist('access_telecommuniciation')
    access_drill_simulation = request.GET.getlist('access_drill_simulation')
    householdbuildingtypes_exact = request.GET.get('householdbuildingtypes')
    householdtenuralstatus_exact = request.GET.get('householdtenuralstatus')
    householdroofmaterials_exact = request.GET.get('householdroofmaterials')
    householdwallmaterials_exact = request.GET.get('householdwallmaterials')
    householdwatertenuralstatus_exact = request.GET.get('householdwatertenuralstatus')
    waterlevelsystems_exact = request.GET.get('waterlevelsystems')
    evacuationareas_exact = request.GET.get('evacuationareas')


    if is_valid_queryparam(controlnumber_icontains_query):
      qs = qs.filter(controlnumber__icontains=controlnumber_icontains_query)
    
    if is_valid_queryparam(purok_icontains_query):
      qs = qs.filter(purok__icontains=purok_icontains_query)

    if is_valid_queryparam(respondent_icontains_query):
      qs = qs.filter(respondent__icontains=respondent_icontains_query)

    if is_valid_queryparam(enumerator_icontains_query):
      qs = qs.filter(enumerator__icontains=enumerator_icontains_query)
    
    if is_valid_queryparam(municipality_exact):
      qs = qs.filter(municipality__exact=municipality_exact)

    if is_valid_queryparam(barangay_exact):
      qs = qs.filter(barangay__exact=barangay_exact)

    if is_valid_queryparam(enumerator_icontains_query):
      qs = qs.filter(enumerator__icontains=enumerator_icontains_query)
    
    if is_valid_queryparam(editor_icontains_query):
      qs = qs.filter(editor__icontains=editor_icontains_query)

    if is_valid_queryparam(year_construct_exact_query):
      qs = qs.filter(year_construct__exact=year_construct_exact_query)
  
    if is_valid_queryparam(estimated_cost_exact_query):
      qs = qs.filter(estimated_cost__exact=estimated_cost_exact_query)

    if is_valid_queryparam(number_bedrooms_exact_query):
        qs = qs.filter(number_bedrooms__exact=number_bedrooms_exact_query)
  
    if is_valid_queryparam(number_storey_exact_query):
            qs = qs.filter(number_storey__exact=number_storey_exact_query)

    if is_valid_queryparam(medical_treatment_icontains_query):
            qs = qs.filter(medical_treatment__icontains=medical_treatment_icontains_query)      

    if is_valid_queryparam(year_flooded_exact):
            qs = qs.filter(year_flooded__exact=year_flooded_exact)   

    if is_valid_queryparam(year_evacuate_exact):
            qs = qs.filter(year_evacuate__exact=year_evacuate_exact)  
    
    if is_valid_queryparam(householdbuildingtypes_exact):
          qs = qs.filter(householdbuildingtypes__exact=householdbuildingtypes_exact)  

    if is_valid_queryparam(householdtenuralstatus_exact):
          qs = qs.filter(householdtenuralstatus__exact=householdtenuralstatus_exact)          

    if is_valid_queryparam(householdroofmaterials_exact):
          qs = qs.filter(householdroofmaterials__exact=householdroofmaterials_exact)  
    
    if is_valid_queryparam(householdwallmaterials_exact):
          qs = qs.filter(householdwallmaterials__exact=householdwallmaterials_exact) 

    if is_valid_queryparam(householdwatertenuralstatus_exact):
          qs = qs.filter(householdwatertenuralstatus__exact=householdwatertenuralstatus_exact) 
    
    if is_valid_queryparam(waterlevelsystems_exact):
          qs = qs.filter(waterlevelsystems__exact=waterlevelsystems_exact) 
  
    if is_valid_queryparam(evacuationareas_exact):
          qs = qs.filter(evacuationareas__exact=evacuationareas_exact) 
  
    # For Boolean field
    if access_electricity:
            qs = qs.filter(access_electricity__in=access_electricity)

    if access_internet:
            qs = qs.filter(access_internet__in=access_internet)

    if access_water_supply:
            qs = qs.filter(access_water_supply__in=access_water_supply)

    if potable:
            qs = qs.filter(potable__in=potable)
    
    if floods_occur:
          qs = qs.filter(floods_occur__in=floods_occur)

    if experience_evacuate:
          qs = qs.filter(experience_evacuate__in=experience_evacuate)

    if access_health_medical_facility:
          qs = qs.filter(access_health_medical_facility__in=access_health_medical_facility)

    if access_telecommuniciation:
          qs = qs.filter(access_telecommuniciation__in=access_telecommuniciation)

    if access_drill_simulation:
          qs = qs.filter(access_drill_simulation__in=access_drill_simulation)


    # households = serialize('geojson',qs,use_natural_foreign_keys=True)
    households = serialize('geojson',qs,use_natural_foreign_keys=True,fields=('pk','location','latitude','longitude'))
    return HttpResponse(households,content_type='json')
   
  else:
    # Do something for anonymous users.
    raise PermissionDenied()

#AJAX
@require_http_methods(["GET"])
def household_info(request):
  if request.user.is_authenticated:
    # Do something for authenticated users.
    households = serialize('geojson',Households.objects.filter(pk=[request.GET.get('pk')]).values(),use_natural_foreign_keys=True)
    print(connection.queries)
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
