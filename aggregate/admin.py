from django.contrib import admin
from .models import Familiesandpopulation, Barangays, AggregatedFamiliesandPopulation


@admin.register(AggregatedFamiliesandPopulation)
class AggregatedFamiliesandPopulationAdmin(admin.ModelAdmin):
  def has_add_permission(self, request):
    return False
  
  change_list_template = 'aggregate/change_list.html'
  list_display = ('munname','brgyname','households','male','female','male_infant','female_infant','male_children',
                  'female_children','male_adult','female_adult','male_elderly','female_elderly','ip_male','ip_female')
  ordering = ['munname','brgyname','households']
  search_fields = ('munname','brgyname',)

  


