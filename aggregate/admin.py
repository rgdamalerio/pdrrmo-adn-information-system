from django.contrib import admin
from .models import Familiesandpopulation, Barangays




# Register your models here.
#@admin.register(Familiesandpopulation)
class FamiliesandpopulationAdmin(admin.ModelAdmin):
  
  # @admin.action(description='Generate PDF file')
  # def generatePDF(modeladmin, request, queryset):
  #       url ='templates/admin/aggregate/?pks=' + ','.join(str([q.pk for q in queryset]))
  # actions = [generatePDF]
  
  # @admin.action(description='Generate PDF file')
  # def export_pdf(modeladmin, request, queryset):
  #       url ='export_pdf' 
  # actions = [export_pdf]
  
  list_display = (
      "municipality",
      "barangay",
      "num_of_family",
      "num_of_individuals_m",
      "num_of_individuals_f",
      "num_of_infant_m",
      "num_of_infant_f",
      "num_of_children_m",
      "num_of_children_f",
      "num_of_adult_m",
      "num_of_adult_f",
      "num_of_elderly_m",
      "num_of_elderly_f",
      "num_of_pwd_m",
      "num_of_pwd_f",
      "num_of_ip_m",
      "num_of_ip_f",
      )
  #search_fields = (
  #    "municipality",
  #    )
  
  
# Register your models here.
admin.site.register(Familiesandpopulation,FamiliesandpopulationAdmin)



# class SampletableAdmin(admin.ModelAdmin):
#   list_display = (
#       "stpsgccode",
#       "stmunname",
#       "stcreated_at",
#       "stupdated_at",
#       )
  
#admin.site.register(Sampletable,SampletableAdmin)


# class PersonAdmin(admin.ModelAdmin):
#     @admin.action(description='Generate PDF file')
#     def generatePDF(modeladmin, request, queryset):
#         url ='templates/admin/aggregate/?pks=' + ','.join(str([q.pk for q in queryset]))
       
#     actions = [generatePDF]

# admin.site.register(Person, PersonAdmin)