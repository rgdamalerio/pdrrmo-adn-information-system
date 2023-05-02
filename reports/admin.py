from django.contrib import admin
from .models import FloodReport, LandslideReport, StormSurgeReport

# Register your models here.
@admin.register(FloodReport)
class FloodReportAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    list_display = ('status','municipality_name','barangay_name','household','person','num_male','num_female','num_male_infant','num_female_infant',
                    'num_male_children','num_female_children','num_male_adult','num_female_adult','num_male_elderly','num_female_elderly',
                    'num_ip_male','num_ip_female')
    
    def status(self, obj):
        if obj.flood_id == 'LF':
            return 'Low Flood'
        elif obj.flood_id == 'HF':
            return 'High Flood'
        elif obj.flood_id == 'MF':
            return 'Moderate Flood'
        else:
            return 'Very High Flood'
    status.short_description = 'Flood Susceptibility'
        
    status.short_description = 'Landslide Susceptibility'
    search_fields = ('flood_id','municipality_name','barangay_name',)
    list_filter = ('flood_id',)
    ordering = ('flood_id','municipality_name','barangay_name',)
    list_per_page = 10

@admin.register(LandslideReport)
class LandslideReportAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    list_display = ('status','municipality_name','barangay_name','household','person','num_male','num_female','num_male_infant','num_female_infant',
                    'num_male_children','num_female_children','num_male_adult','num_female_adult','num_male_elderly','num_female_elderly',
                    'num_ip_male','num_ip_female')
    
    def status(self, obj):
        if obj.ril_id == 'LL':
            return 'Low Landslide'
        elif obj.ril_id == 'HL':
            return 'High Landslide'
        elif obj.ril_id == 'ML':
            return 'Moderate Landslide'
        else:
            return 'Very High Landslide'
    status.short_description = 'Landslide Susceptibility'

    search_fields = ('ril_id','municipality_name','barangay_name',)
    list_filter = ('ril_id',)
    ordering = ('ril_id','municipality_name','barangay_name',)
    list_per_page = 10

@admin.register(StormSurgeReport)
class LandslideReportAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    
    list_display = ('status','municipality_name','barangay_name','household','person','num_male','num_female','num_male_infant','num_female_infant',
                    'num_male_children','num_female_children','num_male_adult','num_female_adult','num_male_elderly','num_female_elderly',
                    'num_ip_male','num_ip_female')
    
    def status(self, obj):
        if obj.surge_id == 1:
            return 'Knee Deep Surge Height'
        elif obj.surge_id == 2:
            return 'Chest Deep Surge Height'
        elif obj.surge_id == 3:
            return 'Above Head Surge Height'
    status.short_description = 'Storm Surge Susceptibility'
        

    search_fields = ('municipality_name','barangay_name',)
    ordering = ('municipality_name','barangay_name',)
    list_filter = ('surge_id',)
    list_per_page = 10

    
        
        
    
