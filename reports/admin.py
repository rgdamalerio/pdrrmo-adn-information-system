from django.contrib import admin
from .models import FloodReport, LandslideReport, StormSurgeReport
from .views import ViewPDF
from django.urls import path




# Register your models here.
@admin.register(FloodReport)
class FloodReportAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('pdf_download/<str:model>/', ViewPDF.as_view(), name="pdf_download"),
        ]
        return my_urls + urls

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['queryset'] = FloodReport.objects.all()
        return super().changelist_view(request, extra_context=extra_context)
    def get_queryset(self, request):
      queryset = super().get_queryset(request)
      if hasattr(request, 'flood'):
        return request.flood
      return queryset
    change_list_template = 'reports/change_list.html'
    
    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request):
        return False
    list_display = ('status','municipality_name','barangay_name','purok_name','household','families','person','num_male','num_female','num_male_infant','num_female_infant',
                    'num_male_children','num_female_children','num_male_adult','num_female_adult','num_male_elderly','num_female_elderly','num_pwd_male','num_pwd_female',
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
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('pdf_download/<str:model>/', ViewPDF.as_view(), name="pdf_download"),
        ]
        return my_urls + urls

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['queryset'] = LandslideReport.objects.all()
        return super().changelist_view(request, extra_context=extra_context)
    
    def get_queryset(self, request):
      queryset = super().get_queryset(request)
      if hasattr(request, 'landslide'):
        return request.landslide
      return queryset
    
    change_list_template = 'reports/change_list.html'
    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request):
        return False
    list_display = ('status','municipality_name','barangay_name','purok_name','household','families','person','num_male','num_female','num_male_infant','num_female_infant',
                    'num_male_children','num_female_children','num_male_adult','num_female_adult','num_male_elderly','num_female_elderly','num_pwd_male','num_pwd_female',
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
class StormSurgeReporAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('pdf_download/<str:model>/', ViewPDF.as_view(), name="pdf_download"),
        ]
        return my_urls + urls

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['queryset'] = StormSurgeReport.objects.all()
        return super().changelist_view(request, extra_context=extra_context)
    
    def get_queryset(self, request):
      queryset = super().get_queryset(request)
      if hasattr(request, 'storm_surge'):
        return request.storm_surge
      return queryset
    
    change_list_template = 'reports/change_list.html'
    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request):
        return False
    
    list_display = ('ss_id','municipality_name','barangay_name','purok_name','household','families','person','num_male','num_female','num_male_infant','num_female_infant',
                    'num_male_children','num_female_children','num_male_adult','num_female_adult','num_male_elderly','num_female_elderly','num_pwd_male','num_pwd_female',
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
    list_filter = ('ss_id',)
    list_per_page = 10
