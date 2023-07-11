from django.contrib import admin
from .models import Familiesandpopulation, Barangays, AggregatedFamiliesandPopulation
from household.middleware import *
from django.core.exceptions import PermissionDenied
from library.models import UserLocation



class FilterUserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        user = request.user
        try:
            user_location = user.userlocation 
        except UserLocation.DoesNotExist:
            user_location = None
        
        # Check if user belongs to the "municipality" group or is an admin
        if user.groups.filter(name='municipality').exists() or user.is_superuser:
            if user_location:
                obj.municipality = user_location.psgccode_mun
            obj.save()
        else:
            raise PermissionDenied("You do not have permission to save this object.")
            
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        try:
            user_location = request.user.userlocation
        except UserLocation.DoesNotExist:
            user_location = None
        
        # Check if user is an admin or has no location
        if request.user.is_superuser or not user_location:
            return qs
        
        # Check if user belongs to the "municipality" group
        if request.user.groups.filter(name='municipality').exists():
            return qs.filter(munname=user_location.psgccode_mun)
        return qs.none()
    
    def has_change_permission(self, request, obj=None):
        if not obj:
            return True
        try:
            user_location = request.user.userlocation 
        except UserLocation.DoesNotExist:
            user_location = None
        
        # Check if user belongs to the "municipality" group or is an admin
        if request.user.groups.filter(name='municipality').exists() or request.user.is_superuser:
            if user_location:
                return obj.municipality == user_location.psgccode_mun
            return True
        
        return False



@admin.register(AggregatedFamiliesandPopulation)
class AggregatedFamiliesandPopulationAdmin(FilterUserAdmin):
  def has_add_permission(self, request):
    return False
  
  change_list_template = 'aggregate/change_list.html'
  list_display = ('munname','brgyname','households','families','male','female','male_infant','female_infant','male_children',
                  'female_children','male_adult','female_adult','male_elderly','female_elderly','ip_male','ip_female')
  ordering = ['munname','brgyname','households']
  search_fields = ('munname','brgyname',)
  list_per_page = 15

  


