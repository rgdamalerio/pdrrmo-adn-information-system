from django.contrib import admin
from .models import Households
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
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
  list_display = ("controlnumber","municipality","barangay","purok","respondent",
    "date_interview","created_at","updated_at","owner")
  search_fields = ("respondent",)
  list_filter = ('municipality_id','barangay_id','access_electricity', 'access_internet','access_water_supply','potable',
    'floods_occur','experience_evacuate','access_health_medical_facility',
    'access_telecommuniciation','access_drill_simulation')

admin.site.register(Households,HouseholdsAdmin)

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