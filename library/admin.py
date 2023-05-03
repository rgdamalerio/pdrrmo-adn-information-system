from django.contrib import admin
from .models import Municipalities,Barangays,Buildingroofmaterials, \
  Buildingstatus, Buildingtypes, Buildinguses, Buildingwallmaterials, \
  Disabilities, Farmingtechs, Genders, Gradelevels, Evacuationareas, \
  Waterlevelsystems, Householdroofmaterials, Householdtenuralstatus, \
  Householdbuildingtypes, Householdwallmaterials, Householdwatertenuralstatus, \
  Livelihoods, Maritalstatus, Monthlyincomes, Nutritionalstatus, Relationshiptoheads, \
  Livelihoodtenuralstatus, Trackstrandcourses, Typeofprograms, Purok, Familystatus, Familyrelationship

class PuroksInline(admin.StackedInline):
  model = Purok
  extra = 0

class BarangaysInline(admin.StackedInline):
  model= Barangays
  extra = 0

# Register your models here.
class MunicipalitiesAdmin(admin.ModelAdmin):
  list_display = ("psgccode","munname","created_at","updated_at","owner")
  inlines = [BarangaysInline]

class BarangaysAdmin(admin.ModelAdmin):
  list_display = ("psgccode","brgyname","created_at","updated_at","owner","psgcmun")
  search_fields = ('brgyname',)
  inlines = [PuroksInline]

class BuildingroofmaterialsAdmin(admin.ModelAdmin):
  list_display = ("id","description","created_at","updated_at","owner")

class BuildingstatusAdmin(admin.ModelAdmin):
  list_display = ("id","status","created_at","updated_at","owner")

class BuildingtypesAdmin(admin.ModelAdmin):
  list_display = ("id","type","created_at","updated_at","owner")

class BuildingusesAdmin(admin.ModelAdmin):
  list_display = ("id","use","created_at","updated_at","owner")

class BuildingwallmaterialsAdmin(admin.ModelAdmin):
  list_display = ("id","material","created_at","updated_at","owner")

class DisabilitiesAdmin(admin.ModelAdmin):
  list_display = ("id","description","created_at","updated_at","owner")

class FarmingtechsAdmin(admin.ModelAdmin):
  list_display = ("id","technology","created_at","updated_at","owner")

class GendersAdmin(admin.ModelAdmin):
  list_display = ("id","gender","created_at","updated_at","owner")

class GradelevelsAdmin(admin.ModelAdmin):
  list_display = ("code","description","created_at","updated_at","owner")

class EvacuationareasAdmin(admin.ModelAdmin):
  list_display = ("id","evacuation_area","created_at","updated_at","owner")

class WaterlevelsystemsAdmin(admin.ModelAdmin):
  list_display = ("id","level","description","created_at","updated_at","owner")

class HouseholdroofmaterialsAdmin(admin.ModelAdmin):
  list_display = ("id","description","created_at","updated_at","owner")

class HouseholdtenuralstatusAdmin(admin.ModelAdmin):
  list_display = ("id","description","created_at","updated_at","owner")

class HouseholdbuildingtypesAdmin(admin.ModelAdmin):
  list_display = ("id","type","created_at","updated_at","owner")

class HouseholdwallmaterialsAdmin(admin.ModelAdmin):
  list_display = ("id","description","created_at","updated_at","owner")

class HouseholdwatertenuralstatusAdmin(admin.ModelAdmin):
  list_display = ("id","status","created_at","updated_at","owner")

class LivelihoodsAdmin(admin.ModelAdmin):
  list_display = ("id","description","created_at","updated_at","owner")

class MaritalstatusAdmin(admin.ModelAdmin):
  list_display = ("id","status","created_at","updated_at","owner")

class MonthlyincomesAdmin(admin.ModelAdmin):
  list_display = ("id","income","created_at","updated_at","owner")

class NutritionalstatusAdmin(admin.ModelAdmin):
  list_display = ("id","status","created_at","updated_at","owner")

class RelationshiptoheadsAdmin(admin.ModelAdmin):
  list_display = ("id","relationship","created_at","updated_at","owner")

class LivelihoodtenuralstatusAdmin(admin.ModelAdmin):
  list_display = ("id","status","created_at","updated_at","owner")

class TrackstrandcoursesAdmin(admin.ModelAdmin):
  list_display = ("id","description","created_at","updated_at","owner")

class TypeofprogramsAdmin(admin.ModelAdmin):
  list_display = ("id","type","created_at","updated_at","owner")

class FamilystatusAdmin(admin.ModelAdmin):
  list_display = ("id","type","created_at","updated_at","owner")

class FamilyrelationshipAdmin(admin.ModelAdmin):
  list_display = ("id","type","created_at","updated_at","owner")


admin.site.register(Municipalities,MunicipalitiesAdmin)
admin.site.register(Barangays,BarangaysAdmin)
admin.site.register(Buildingroofmaterials,BuildingroofmaterialsAdmin)
admin.site.register(Buildingstatus,BuildingstatusAdmin)
admin.site.register(Buildingtypes,BuildingtypesAdmin)
admin.site.register(Buildinguses,BuildingusesAdmin)
admin.site.register(Buildingwallmaterials,BuildingwallmaterialsAdmin)
admin.site.register(Disabilities,DisabilitiesAdmin)
admin.site.register(Farmingtechs,FarmingtechsAdmin)
admin.site.register(Genders,GendersAdmin)
admin.site.register(Gradelevels,GradelevelsAdmin)
admin.site.register(Evacuationareas,EvacuationareasAdmin)
admin.site.register(Waterlevelsystems,WaterlevelsystemsAdmin)
admin.site.register(Householdroofmaterials,HouseholdroofmaterialsAdmin)
admin.site.register(Householdtenuralstatus,HouseholdtenuralstatusAdmin)
admin.site.register(Householdbuildingtypes,HouseholdbuildingtypesAdmin)
admin.site.register(Householdwallmaterials,HouseholdwallmaterialsAdmin)
admin.site.register(Householdwatertenuralstatus,HouseholdwatertenuralstatusAdmin)
admin.site.register(Livelihoods,LivelihoodsAdmin)
admin.site.register(Maritalstatus,MaritalstatusAdmin)
admin.site.register(Monthlyincomes,MonthlyincomesAdmin)
admin.site.register(Nutritionalstatus,NutritionalstatusAdmin)
admin.site.register(Relationshiptoheads,RelationshiptoheadsAdmin)
admin.site.register(Livelihoodtenuralstatus,LivelihoodtenuralstatusAdmin)
admin.site.register(Trackstrandcourses,TrackstrandcoursesAdmin)
admin.site.register(Typeofprograms,TypeofprogramsAdmin)
admin.site.register(Familystatus,FamilystatusAdmin)
admin.site.register(Familyrelationship,FamilyrelationshipAdmin)
