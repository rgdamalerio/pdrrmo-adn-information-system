from django.contrib import admin
from .models import FloodReport

# Register your models here.
@admin.register(FloodReport)
class FloodReportAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    list_display = ('flood_id','municipality_name','barangay_name','household','person','num_male','num_female','num_male_infant','num_female_infant',
                    'num_male_children','num_female_children','num_male_adult','num_female_adult','num_male_elderly','num_female_elderly',
                    'num_ip_male','num_ip_female')
    search_fields = ('flood_id','municipality_name','barangay_name',)
    list_filter = ('flood_id',)
    ordering = ('flood_id','municipality_name','barangay_name',)
    list_per_page = 10

    
