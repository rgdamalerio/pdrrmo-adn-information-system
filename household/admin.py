import imp
from django.contrib import admin
from .models import Households
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
# Register your models here.
class HouseholdsAdmin(LeafletGeoAdmin):
  list_display = ("controlnumber","municipality","barangay","purok","respondent",
    "date_interview","created_at","updated_at","owner")

admin.site.register(Households,HouseholdsAdmin)