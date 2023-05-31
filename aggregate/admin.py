from django.contrib import admin
from .models import Familiesandpopulation, Barangays, AggregatedFamiliesandPopulation
from household.middleware import *


class FilterUserAdmin(admin.ModelAdmin):
  def save_model(self, request, obj, form, change):
    user = request.user
    user_location = user.userlocation  # Assuming 'userlocation' is the OneToOneField related to User
    obj.municipality = user_location.psgccode_mun
    obj.save()

  def get_queryset(self, request):
    qs = super().get_queryset(request)
    user_location = request.user.userlocation
    return qs.filter(munname=user_location.psgccode_mun)

  def has_change_permission(self, request, obj=None):
    if not obj:
        return True
    user_location = request.user.userlocation
    return obj.municipality == user_location.psgccode_mun


@admin.register(AggregatedFamiliesandPopulation)
class AggregatedFamiliesandPopulationAdmin(FilterUserAdmin):
  def has_add_permission(self, request):
    return False
  
  change_list_template = 'aggregate/change_list.html'
  list_display = ('munname','brgyname','households','male','female','male_infant','female_infant','male_children',
                  'female_children','male_adult','female_adult','male_elderly','female_elderly','ip_male','ip_female')
  ordering = ['munname','brgyname','households']
  search_fields = ('munname','brgyname',)
  list_per_page = 15

  


