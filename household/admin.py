from django.contrib import admin
from django.contrib.gis.db import models
from .models import Households, Demographies, Availprograms, Hhlivelihoods
from leaflet.admin import LeafletGeoAdmin
from mapwidgets.widgets import GooglePointFieldWidget, MapboxPointFieldWidget
from household.forms import HouseholdForm


from datetime import date
import datetime
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html




# /Related model with inline view in household model
class DemographiesInline(admin.StackedInline):
  model = Demographies
  extra = 0
  readonly_fields = ['owner','created_at','updated_at','age',]


  def age(self,demography):
    today = date.today()
    bday = demography.birthdate.strftime("%Y-%m-%d %H:%M:%S")
    datem = datetime.datetime.strptime(bday,"%Y-%m-%d %H:%M:%S")
    return today.year - datem.year - ((today.month, today.day) < (datem.month, datem.day))



class LivelihoodsInline(admin.StackedInline):
  model = Hhlivelihoods
  extra = 0
  readonly_fields = ['owner','created_at','updated_at',]

# Register your models here.
@admin.register(Households)
class HouseholdsAdmin(admin.ModelAdmin):
  form = HouseholdForm
  formfield_overrides = {
      models.PointField: {"widget": GooglePointFieldWidget}
  }
  readonly_fields = ('enumerator','editor',)
  fields = ['respondent','municipality', 'barangay','purok_fk','location','householdbuildingtypes',
            'householdtenuralstatus','year_construct','estimated_cost', 'number_bedrooms', 'number_storey',
            'access_electricity', 'householdroofmaterials','householdwallmaterials','medical_treatment',
            'access_water_supply','potable','householdwatertenuralstatus','waterlevelsystems','floods_occur',
            'year_flooded','experience_evacuate','year_evacuate','evacuationareas','access_health_medical_facility',
            'access_telecommuniciation','access_drill_simulation','image','enumerator','editor'
           ]
  list_display = ('controlnumber','municipality','barangay','purok_fk','respondent',
    'date_interview','created_at','updated_at','owner','views_demographies_link','views_availprograms_link','views_hhlivelihoods_link')
  list_editable = ('respondent','purok_fk')
  list_per_page = 10
  
  def views_demographies_link(self, obj):
    count_demographies = obj.demographies_set.count()
    changelist_link = (
      reverse("admin:household_demographies_changelist")  + "?" + urlencode({"controlnumber": obj.controlnumber})
    )
    add_link = (
      reverse("admin:household_demographies_add") + "?" + urlencode({"controlnumber": obj.controlnumber})
    )

    if count_demographies > 1:
      return format_html('<a href="{}">{} Members | <a href="{}">Add</a>', changelist_link, count_demographies, add_link)
    elif count_demographies == 1:
      return format_html('<a href="{}">{} Member | <a href="{}">Add</a>', changelist_link, count_demographies, add_link)
    else:
        return format_html('<a href="{}"> None | <a href="{}">Add</a>', changelist_link, add_link)
  views_demographies_link.short_description = "Family Members"


  def views_availprograms_link(self, obj):
    count_availprograms = obj.availprograms_set.count()

    changelist_link = (
      reverse("admin:household_availprograms_changelist") + "?" + urlencode({"controlnumber": obj.controlnumber})
    )
    add_link = (
      reverse("admin:household_availprograms_add") + "?" + urlencode({"controlnumber": obj.controlnumber})
    )
    if count_availprograms > 1:
      return format_html('<a href="{}">{} Programs | <a href="{}">Add</a>', changelist_link, count_availprograms,add_link)
    elif count_availprograms == 1:
      return format_html('<a href="{}">{} Program | <a href="{}">Add</a>', changelist_link, count_availprograms,add_link) 
    else:
      return format_html('<a href="{}"> None | <a href="{}">Add</a>', changelist_link, add_link)

  views_availprograms_link.short_description = "Availed Programs"

  def views_hhlivelihoods_link(self, obj):
    count_hhlivelihoods = obj.hhlivelihoods_set.count()

    changelist_link = (
      reverse("admin:household_hhlivelihoods_changelist") + "?" + urlencode({"controlnumber": obj.controlnumber})
    )
    add_link = (
      reverse("admin:household_hhlivelihoods_add") + "?" + urlencode({"controlnumber": obj.controlnumber})
    )
    
    if count_hhlivelihoods > 1:
      return format_html('<a href="{}">{} Livelihoods | <a href="{}">Add</a>', changelist_link, count_hhlivelihoods, add_link)
    elif count_hhlivelihoods == 1:
      return format_html('<a href="{}">{} Livelihood | <a href="{}">Add</a>', changelist_link, count_hhlivelihoods, add_link)
    else:
      return format_html('<a href="{}"> None | <a href="{}">Add</a>', changelist_link, add_link)

  views_hhlivelihoods_link.short_description = "Livelihoods"

  search_fields = ('respondent',)
  list_filter = ('municipality_id','barangay_id','access_electricity', 'access_internet','access_water_supply','potable',
    'floods_occur','experience_evacuate','access_health_medical_facility',
    'access_telecommuniciation','access_drill_simulation')
  inlines = [
    #DemographiesInline,
    #AvailprogramsInline,
    #LivelihoodsInline
  ]

  class Media:
      js = (
          'js/chained-address.js',
      )
    


@admin.register(Demographies)
class DemographiesAdmin(admin.ModelAdmin):
  list_display = ('controlnumber_id','lastname','firstname','middlename','extension','birthdate','age','primary_occupation',
    'created_at','updated_at','owner')
  fields = ['controlnumber','lastname','firstname','middlename','extension','nuclear_family','relationshiptohead',
            'gender','birthdate', 'marital_status', 'ethnicity_by_blood', 'member_ip', 'informal_settler', 'religion',
            'person_with_special_needs', 'type_of_disability', 'is_ofw', 'residence', 'nutritional_status', 'nutritional_status_recorded',
            'currently_attending_school', 'current_grade_level_attending', 'highest_eductional_attainment', 'course_completed_vocational',
            'can_read_and_write', 'primary_occupation', 'monthly_income', 'sss_member', 'gsis_member', 'philhealth_member', 
            'dependent_of_philhealth_member', 'owner']
  readonly_fields = ['owner','created_at','updated_at','age',]
  list_editable = ('lastname','firstname','middlename','extension','birthdate','primary_occupation',)
  #list_display_links = ('lastname',)
  list_per_page = 10
  
  #list_filter = ('controlnumber_id',)
  search_fields = ('lastname',)


  '''def has_add_permission(self, request):
        return False'''
  
  def age(self,demography):
    today = date.today()
    bday = demography.birthdate.strftime("%Y-%m-%d %H:%M:%S")
    datem = datetime.datetime.strptime(bday,"%Y-%m-%d %H:%M:%S")
    return today.year - datem.year - ((today.month, today.day) < (datem.month, datem.day))


@admin.register(Availprograms)
class AvailprogramsAdmin(admin.ModelAdmin):
  list_display = ('controlnumber','type_of_program','name_of_program','number_of_beneficiaries','program_implementor','created_at','updated_at','owner')
  search_fields = ('controlnumber',)

@admin.register(Hhlivelihoods)
class HlivelihoodsAdmin(admin.ModelAdmin):
  list_display = ('controlnumber','products','market_value','area','livelihood_tenural_status','with_insurance','livelihood','created_at','updated_at','owner')
  search_fields = ('controlnumber',)
  
  class Meta:
    verbose_name_plural = "Household livelihoods"


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
