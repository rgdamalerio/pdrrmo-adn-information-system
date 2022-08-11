from django.contrib import admin
from .models import Households, Demographies, Availprograms, Hhlivelihoods
from leaflet.admin import LeafletGeoAdmin

from datetime import date
import datetime

# Register your models here.
class HouseholdsAdmin(LeafletGeoAdmin):
  readonly_fields = ('enumerator','editor',)
  fields = ['respondent','municipality', 'barangay', 'purok', 'location','householdbuildingtypes',
            'householdtenuralstatus','year_construct','estimated_cost', 'number_bedrooms', 'number_storey',
            'access_electricity', 'householdroofmaterials','householdwallmaterials','medical_treatment',
            'access_water_supply','potable','householdwatertenuralstatus','waterlevelsystems','floods_occur',
            'year_flooded','experience_evacuate','year_evacuate','evacuationareas','access_health_medical_facility',
            'access_telecommuniciation','access_drill_simulation','image','enumerator','editor'
           ]
  list_display = ('controlnumber','municipality','barangay','purok','respondent',
    'date_interview','created_at','updated_at','owner')
  search_fields = ('respondent',)
  list_filter = ('municipality_id','barangay_id','access_electricity', 'access_internet','access_water_supply','potable',
    'floods_occur','experience_evacuate','access_health_medical_facility',
    'access_telecommuniciation','access_drill_simulation')

class DemographiesAdmin(admin.ModelAdmin):
  list_display = ('lastname','firstname','middlename','birthdate','age','controlnumber_id',
    'created_at','updated_at','owner')
  fields = ['controlnumber','lastname','firstname','middlename','extension','nuclear_family','relationshiptohead',
            'gender','birthdate', 'marital_status', 'ethnicity_by_blood', 'member_ip', 'informal_settler', 'religion',
            'person_with_special_needs', 'type_of_disability', 'is_ofw', 'residence', 'nutritional_status', 'nutritional_status_recorded',
            'currently_attending_school', 'current_grade_level_attending', 'highest_eductional_attainment', 'course_completed_vocational',
            'can_read_and_write', 'primary_occupation', 'monthly_income', 'sss_member', 'gsis_member', 'philhealth_member', 
            'dependent_of_philhealth_member', 'owner']

  def age(self,demography):
    today = date.today()
    bday = demography.birthdate.strftime("%Y-%m-%d %H:%M:%S")
    datem = datetime.datetime.strptime(bday,"%Y-%m-%d %H:%M:%S")
    return today.year - datem.year - ((today.month, today.day) < (datem.month, datem.day))

class AvailprogramsAdmin(admin.ModelAdmin):
  list_display = ('controlnumber','type_of_program','name_of_program','number_of_beneficiaries','program_implementor','created_at','updated_at','owner')

class HlivelihoodsAdmin(admin.ModelAdmin):
  list_display = ('controlnumber','products','market_value','area','livelihood_tenural_status','with_insurance','livelihood','created_at','updated_at','owner')

  class Meta:
    verbose_name_plural = "Household livelihoods"


admin.site.register(Households,HouseholdsAdmin)
admin.site.register(Demographies,DemographiesAdmin)
admin.site.register(Availprograms,AvailprogramsAdmin)
admin.site.register(Hhlivelihoods,HlivelihoodsAdmin)


# def has_change_permission(self, request, obj=None):
#         if obj:
#             if obj.municipality_id == "160212000":
#                  return False
#             else:
#                  return True
#                  #return request.user.has_perm('Update Panaytayon')
#         return super(HouseholdsAdmin, self).has_change_permission(self, request, obj)
# def has_view_permission(self, request, obj=None):
#   return False

# def has_add_permission(self, request):
#   return False

# def has_change_permission(self, request, obj=None):
#   return False

# def has_delete_permission(self, request, obj=None):
#   return False