
from django.contrib import admin
from .models import FloodReport, LandslideReport, StormSurgeReport
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import Permission
from library.models import UserLocation


class FilterReportsAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        user = request.user
        try:
            user_location = user.userlocation 
        except UserLocation.DoesNotExist:
            user_location = None
        
        # Check if user belongs to the "municipality" group or is an admin
        if user.groups.filter(name='municipality').exists() or user.is_superuser:
            if user_location:
                obj.municipality = user_location.psgccode_mun
            obj.save()
        else:
            raise PermissionDenied("You do not have permission to save this object.")
            
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        try:
            user_location = request.user.userlocation
        except UserLocation.DoesNotExist:
            user_location = None
        
        # Check if user is an admin or has no location
        if request.user.is_superuser or not user_location:
            return qs
        
        # Check if user belongs to the "municipality" group
        if request.user.groups.filter(name='municipality').exists():
            return qs.filter(municipality_name=user_location.psgccode_mun)
        return qs.none()
    
    def has_change_permission(self, request, obj=None):
        if not obj:
            return True
        try:
            user_location = request.user.userlocation 
        except UserLocation.DoesNotExist:
            user_location = None
        
        # Check if user belongs to the "municipality" group or is an admin
        if request.user.groups.filter(name='municipality').exists() or request.user.is_superuser:
            if user_location:
                return obj.municipality == user_location.psgccode_mun
            return True
        
        return False

# Register your models here.
@admin.register(FloodReport)
class FloodReportAdmin(FilterReportsAdmin):
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
class LandslideReportAdmin(FilterReportsAdmin):
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
class StormSurgeReporAdmin(FilterReportsAdmin):
    def has_add_permission(self, request):
        return False
    
    list_display = ('ssid','municipality_name','barangay_name','household','person','num_male','num_female','num_male_infant','num_female_infant',
                    'num_male_children','num_female_children','num_male_adult','num_female_adult','num_male_elderly','num_female_elderly',
                    'num_ip_male','num_ip_female')
    
    '''def status(self, obj):
        if obj.ssid == 1:
            return 'Knee Deep Surge Height'
        elif obj.ssid == 2:
            return 'Chest Deep Surge Height'
        elif obj.ssid == 3:
            return 'Above Head Surge Height'
    status.short_description = 'Storm Surge Susceptibility'''
        

    search_fields = ('municipality_name','barangay_name',)
    ordering = ('municipality_name','barangay_name',)
    list_filter = ('ssid',)
    list_per_page = 10
