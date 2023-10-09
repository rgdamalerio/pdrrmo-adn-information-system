from django.contrib import admin
from django.contrib.gis.db import models
from .models import Households, Demographies, Availprograms, Hhlivelihoods, Families, Familydetails
from leaflet.admin import LeafletGeoAdmin
from mapwidgets.widgets import GooglePointFieldWidget, MapboxPointFieldWidget
from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from household.forms import HouseholdForm, DemographiesForm
from django import forms
from datetime import date
import datetime
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html



class FamiliesInline(admin.StackedInline):
  model = Families
  exclude = ('owner',)
  extra = 0

  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name in ['household', 'family_head']:
      kwargs['widget'] = ForeignKeyRawIdWidget(
          rel=db_field.remote_field,
          admin_site=admin.site,
          attrs={'style': 'width: 215px;'}
      )
    return super().formfield_for_foreignkey(db_field, request, **kwargs)
  def label_from_instance(self, obj):
        return obj.family_head 

  formfield_overrides = {
      models.CharField: {'widget': forms.TextInput(attrs={'size': '30'})},  
      models.ForeignKey: {'widget': forms.Select(attrs={'style': 'width: 215px;'})},  
  }
 

class FamilydetailsInline(admin.StackedInline):
  model = Familydetails
  exclude = ('owner','status',)
  extra = 3
  
  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name in ['fam_fk','fam_member']:
        kwargs['widget'] = ForeignKeyRawIdWidget(
          rel=db_field.remote_field,
          admin_site=admin.site,
          attrs={'style': 'width: 215px;'}
        )
    return super().formfield_for_foreignkey(db_field, request, **kwargs)
  
  formfield_overrides = {
      models.CharField: {'widget': forms.TextInput(attrs={'size': '30'})},  
      models.ForeignKey: {'widget': forms.Select(attrs={'style': 'width: 215px;'})},  
  }
  

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
class HouseholdsAdmin(LeafletGeoAdmin):
    def get_queryset(self, request):
      qs = super().get_queryset(request)
      if hasattr(request, 'households'):
        return request.households
      return qs
    form = HouseholdForm
    settings_overrides = {
      'TILES': [('Mapbox Satellite', 'https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v12/tiles/{z}/{x}/{y}?access_token={accessToken}', {
              'attribution': 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
              'accessToken': 'pk.eyJ1IjoiaWFtdGVrc29uIiwiYSI6ImNqdjV4YzI4YjB0aXk0ZHBtNnVnNWxlM20ifQ.FjQJyCTodXASYtOK8IrLQA',
              'maxZoom': 20,
          }),
          ('Mapbox V1', 'https://api.tiles.mapbox.com/styles/v1/{username}/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
              'attribution': 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
              'username': 'iamtekson',
              'id': 'cjwhym7s70tae1co8zf17a3r5',
              'accessToken': 'pk.eyJ1IjoiaWFtdGVrc29uIiwiYSI6ImNqdjV4YzI4YjB0aXk0ZHBtNnVnNWxlM20ifQ.FjQJyCTodXASYtOK8IrLQA'
          })],
    }
    '''formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }'''
    readonly_fields = ('enumerator','editor',)
    fields = ['respondent','date_interview','municipality', 'barangay','purok_fk','location','longitude','latitude','householdbuildingtypes',
              'householdtenuralstatus','year_construct','estimated_cost', 'number_bedrooms', 'number_storey',
              'access_electricity', 'householdroofmaterials','householdwallmaterials','medical_treatment',
              'access_water_supply','potable','householdwatertenuralstatus','waterlevelsystems','floods_occur',
              'year_flooded','experience_evacuate','year_evacuate','evacuationareas','access_health_medical_facility',
              'access_telecommuniciation','access_drill_simulation','image','enumerator','editor'
            ]
    list_display = ('household_controlnumber','municipality','barangay','purok_fk','respondent','date_interview',
              'views_families_link','views_availprograms_link','views_hhlivelihoods_link','created_at','updated_at')
    search_fields = ('controlnumber', 'respondent', 'municipality__munname', 'barangay__brgyname',)
    list_filter = ('municipality_id','barangay_id','access_electricity','householdbuildingtypes','access_internet','access_water_supply','potable',
      'floods_occur','experience_evacuate','access_health_medical_facility',
      'access_telecommuniciation','access_drill_simulation')
    list_per_page = 20


    def views_families_link(self, obj):
      num_families = obj.families_set.count()
      changelist_link = (
        reverse("admin:household_families_changelist")  + "?" + urlencode({"household": obj.controlnumber})
      )
      add_link = (
        reverse("admin:household_families_add") + "?" + urlencode({"household": obj.controlnumber})
      )

      if num_families > 1:
        return format_html('<a href="{}">{} Families | <a href="{}">Add</a>', changelist_link, num_families, add_link)
      elif num_families == 1:
        return format_html('<a href="{}">{} Family | <a href="{}">Add</a>', changelist_link, num_families, add_link)
      else:
          return format_html('<a href="{}"> None | <a href="{}">Add</a>', changelist_link, add_link)
    views_families_link.short_description = "No. of Families"


    def views_availprograms_link(self, obj):
      num_availprograms = obj.availprograms_set.count()

      changelist_link = (
        reverse("admin:household_availprograms_changelist") + "?" + urlencode({"controlnumber": obj.controlnumber})
      )
      add_link = (
        reverse("admin:household_availprograms_add") + "?" + urlencode({"controlnumber": obj.controlnumber})
      )
      if num_availprograms > 1:
          return format_html('<a href="{}">{} Programs | <a href="{}">Add</a>', changelist_link, num_availprograms,add_link)
      elif num_availprograms == 1:
          return format_html('<a href="{}">{} Program | <a href="{}">Add</a>', changelist_link, num_availprograms,add_link) 
      else:
        return format_html('<a href="{}"> None | <a href="{}">Add</a>', changelist_link, add_link)

    views_availprograms_link.short_description = "Availed Programs"

    def views_hhlivelihoods_link(self, obj):
      num_hhlivelihoods = obj.hhlivelihoods_set.count()

      changelist_link = (
        reverse("admin:household_hhlivelihoods_changelist") + "?" + urlencode({"controlnumber": obj.controlnumber})
      )
      add_link = (
        reverse("admin:household_hhlivelihoods_add") + "?" + urlencode({"controlnumber": obj.controlnumber})
      )
      
      if num_hhlivelihoods > 1:
        return format_html('<a href="{}">{} Livelihoods | <a href="{}">Add</a>', changelist_link, num_hhlivelihoods, add_link)
      elif num_hhlivelihoods == 1:
        return format_html('<a href="{}">{} Livelihood | <a href="{}">Add</a>', changelist_link, num_hhlivelihoods, add_link)
      else:
        return format_html('<a href="{}"> None | <a href="{}">Add</a>', changelist_link, add_link)

    views_hhlivelihoods_link.short_description = "Livelihoods"
  
    inlines = [
      FamiliesInline,
    ]
    formfield_overrides = {
          models.CharField: {'widget': forms.TextInput(attrs={'size': '18'})},
          models.ForeignKey: {'widget': forms.Select(attrs={'style': 'width: 200px;'})}
      }
    class Media:
        js = (
            'js/chained-address.js',
        )
    

@admin.register(Demographies)
class DemographiesAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
      queryset = super().get_queryset(request)
      if hasattr(request, 'demographies'):
        return request.demographies
      return queryset
    form = DemographiesForm
    list_display  = ['controlnumber_id','relationshiptohead','lastname','firstname','middlename','extension','age',
              'gender','birthdate', 'marital_status','primary_occupation', 'religion',
              'can_read_and_write','person_with_special_needs','type_of_disability','created_at','updated_at']
      
    fields = ['controlnumber','lastname','firstname','middlename','extension',
              'gender','birthdate', 'marital_status', 'ethnicity_by_blood', 'member_ip', 'informal_settler', 'religion',
              'person_with_special_needs', 'type_of_disability', 'is_ofw', 'residence', 'nutritional_status', 'nutritional_status_recorded',
              'currently_attending_school', 'current_grade_level_attending', 'highest_eductional_attainment', 'course_completed_vocational',
              'can_read_and_write', 'primary_occupation', 'monthly_income', 'sss_member', 'gsis_member', 'philhealth_member', 
              'dependent_of_philhealth_member', 'owner']
    list_filter = ['marital_status']
    list_select_related = ('controlnumber',)
    list_per_page = 20
    ordering = ('-id',)

    readonly_fields = ['owner','created_at','updated_at','age',]
    list_editable = ['lastname','firstname','middlename','extension','birthdate','marital_status','primary_occupation','gender',
                    'religion','can_read_and_write','person_with_special_needs','type_of_disability']
    search_fields = ('controlnumber_id__controlnumber','lastname','firstname','middlename',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
      if db_field.name == 'controlnumber':
        kwargs['widget'] = ForeignKeyRawIdWidget(
            rel=db_field.remote_field,
            admin_site=admin.site,
            attrs={'size': '25', 'style': 'width: auto;', 'autocomplete_limit': 10},
        )
      return super().formfield_for_foreignkey(db_field, request, **kwargs)

    formfield_overrides = {
      models.CharField: {'widget': forms.TextInput(attrs={'size': '18','style': 'border: 1px solid #000;'})},
      models.ForeignKey: {'widget': forms.Select(attrs={'style': 'width: 100px;'})},
      models.DateField: {'widget': forms.DateInput(attrs={'size': '8','style': 'border: 1px solid #000;'})},
    }
    
    def age(self,demography):
      today = date.today()
      bday = demography.birthdate.strftime("%Y-%m-%d %H:%M:%S")
      datem = datetime.datetime.strptime(bday,"%Y-%m-%d %H:%M:%S")
      return today.year - datem.year - ((today.month, today.day) < (datem.month, datem.day))
    

@admin.register(Families)
class FamiliesAdmin(admin.ModelAdmin):
  def get_queryset(self, request):
    qs = super().get_queryset(request)
    if hasattr(request, 'families'):
      return request.families
    return qs

  list_display = ('household_id','household_controlnumber','family_head','family_members','status','remarks','created_at','updated_at','owner')
  search_fields = ['family_head__firstname', 'family_head__lastname', 'family_head__middlename', 'household__controlnumber']
  list_filter = ['status']
  list_per_page = 20
  exclude = ('owner',)

  def household_id(self, obj):
    return obj.household_id[:15]+"..."
  
  def household_controlnumber(self, obj):
      return obj.household.respondent
  household_controlnumber.short_description = 'Family belong'

  def save_model(self, request, obj, form, change):
    if not obj.pk:  
      if request.user.is_authenticated:
          obj.owner = request.user
      else:
        obj.owner = 1  
    super().save_model(request, obj, form, change)

  def family_members(self, obj):
    count_family_members = obj.familydetails_set.count()
    changelist_link = (
    reverse("admin:household_familydetails_changelist") + "?" + urlencode({"fam_fk": obj.fam_id})
    )
    add_link = (
      reverse("admin:household_familydetails_add") + "?" + urlencode({"fam_fk": obj.fam_id,})
    )

    if count_family_members > 1:
      return format_html('<a href="{}">{} Members | <a href="{}">Add</a>', changelist_link, count_family_members, add_link)
    elif count_family_members == 1:
      return format_html('<a href="{}">{} Member | <a href="{}">Add</a>', changelist_link, count_family_members, add_link)
    else:
      return format_html('<a href="{}"> None | <a href="{}">Add</a>', changelist_link, add_link)

  family_members.short_description = "No. of family members"

  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name in ['household', 'family_head']:
      kwargs['widget'] = ForeignKeyRawIdWidget(
              rel=db_field.remote_field,
              admin_site=admin.site,
              attrs={'size': '25', 'style': 'width: auto;', 'autocomplete_limit': 10},
      )
    return super().formfield_for_foreignkey(db_field, request, **kwargs)
  
  formfield_overrides = {
    models.CharField: {'widget': forms.TextInput(attrs={'size': '25'})},
    models.ForeignKey: {'widget': forms.Select(attrs={'style': 'width: 200px;'})}
    }
  inlines = [FamilydetailsInline]

@admin.register(Familydetails)
class FamilydetailsAdmin(admin.ModelAdmin):
  def get_queryset(self, request):
    qs = super().get_queryset(request)
    if hasattr(request, 'family_members'):
      return request.family_members
    return qs
  list_display = ('fam_fk','fam_member','member_birthdate','age','relationship','remarks','created_at','updated_at','owner')
  search_fields = ['fam_member__firstname','fam_member__middlename','fam_member__lastname','fam_fk__family_head__firstname',
                   'fam_fk__family_head__lastname','fam_fk__family_head__middlename']
  list_filter = ['relationship']
  exclude = ('owner','status')
  list_per_page = 20
  
  def save_model(self, request, obj, form, change):
    if not obj.pk: 
      if request.user.is_authenticated:
          obj.owner = request.user
      else:
        obj.owner = 1  
    super().save_model(request, obj, form, change)
    
  def member_birthdate(self, obj):
    return f"{obj.fam_member.birthdate.strftime('%B %d, %Y')}"
  member_birthdate.short_description = 'Birthdate'

  def age(self, obj):
    today = date.today()
    bday = obj.fam_member.birthdate
    return today.year - bday.year - ((today.month, today.day) < (bday.month, bday.day))
  age.short_description = 'Age'

  def formfield_for_foreignkey(self, db_field, request, **kwargs):
      if db_field.name in ['fam_fk', 'fam_member']:
        kwargs['widget'] = ForeignKeyRawIdWidget(
            rel=db_field.remote_field,
            admin_site=admin.site,
            attrs={'size': '25', 'style': 'width: auto;', 'autocomplete_limit': 10},
        ) 
      return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
  formfield_overrides = {
    models.CharField: {'widget': forms.TextInput(attrs={'size': '25'})},
    models.ForeignKey: {'widget': forms.Select(attrs={'style': 'width: 200px;'})}
    }

@admin.register(Availprograms)
class AvailprogramsAdmin(admin.ModelAdmin):
  def get_queryset(self, request):
    queryset = super().get_queryset(request)
    if hasattr(request, 'availprograms'):
      return request.availprograms
    return queryset
  list_display = ('controlnumber','type_of_program','name_of_program','number_of_beneficiaries','upper_progimplementor','created_at','updated_at','owner')
  search_fields = ('controlnumber',)
  list_filter = ['type_of_program']
  list_per_page = 20

  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name in ['controlnumber']:
      kwargs['widget'] = ForeignKeyRawIdWidget(
              rel=db_field.remote_field,
              admin_site=admin.site,
              attrs={'size': '25', 'style': 'width: auto;', 'autocomplete_limit': 10},
      )
    return super().formfield_for_foreignkey(db_field, request, **kwargs)
  
  formfield_overrides = {
    models.CharField: {'widget': forms.TextInput(attrs={'size': '25'})},
    models.ForeignKey: {'widget': forms.Select(attrs={'style': 'width: 190px;'})},
    models.FloatField: {'widget': forms.NumberInput(attrs={'style': 'width: 190px;'})},  
    models.IntegerField: {'widget': forms.NumberInput(attrs={'style': 'width: 190px;'})},  
  }

@admin.register(Hhlivelihoods)
class HlivelihoodsAdmin(admin.ModelAdmin):
  def get_queryset(self, request):
    queryset = super().get_queryset(request)
    if hasattr(request, 'livelihoods'):
      return request.livelihoods
    return queryset
  list_display = ('controlnumber','products','market_value','area','livelihood_tenural_status','with_insurance','livelihood','created_at','updated_at','owner')
  search_fields = ('controlnumber',)
  list_filter = ['livelihood_tenural_status']
  list_per_page = 20
  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name in ['controlnumber']:
      kwargs['widget'] = ForeignKeyRawIdWidget(
              rel=db_field.remote_field,
              admin_site=admin.site,
              attrs={'size': '25', 'style': 'width: auto;', 'autocomplete_limit': 10},
      )
    return super().formfield_for_foreignkey(db_field, request, **kwargs)
  
  formfield_overrides = {
    models.CharField: {'widget': forms.TextInput(attrs={'size': '25'})},
    models.ForeignKey: {'widget': forms.Select(attrs={'style': 'width: 190px;'})},
    models.FloatField: {'widget': forms.NumberInput(attrs={'style': 'width: 190px;'})},  
    models.IntegerField: {'widget': forms.NumberInput(attrs={'style': 'width: 190px;'})},  
  }

  class Meta:
    verbose_name_plural = "Household livelihoods"
