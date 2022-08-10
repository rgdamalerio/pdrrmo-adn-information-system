from django.contrib import admin
from .models import Households
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
# Register your models here.
class HouseholdsAdmin(LeafletGeoAdmin):
  list_display = ("controlnumber","municipality","barangay","purok","respondent",
    "date_interview","created_at","updated_at","owner")
  search_fields = ("respondent",)
  

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