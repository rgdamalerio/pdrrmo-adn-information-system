from django.db import models
from tabnanny import verbose

# Create your models here.
class FloodReport(models.Model):
    flood_id = models.CharField(max_length=255,primary_key=True,verbose_name='Flood Susceptibility')
    municipality_name = models.CharField(max_length=255,verbose_name='Municipality')
    barangay_name = models.CharField(max_length=255,verbose_name='Barangay')
    household = models.IntegerField(verbose_name='No. of Households')
    person = models.IntegerField(verbose_name='No. of Persons')
    num_male = models.IntegerField(verbose_name='Individuals (M)')
    num_female = models.IntegerField(verbose_name='Individuals (F)')
    num_male_infant = models.IntegerField(verbose_name='Infant 0-11months (M)')
    num_female_infant = models.IntegerField(verbose_name='Infant 0-11months (F)')
    num_male_children = models.IntegerField(verbose_name='Children 1-17y/o (M)')
    num_female_children = models.IntegerField(verbose_name='Children 1-17y/o (F)')
    num_male_adult = models.IntegerField(verbose_name='Adult 18-59y/o (M)')
    num_female_adult = models.IntegerField(verbose_name='Adult 18-59y/o (F)')
    num_male_elderly = models.IntegerField(verbose_name='Elderly 60y/o above (M)')
    num_female_elderly = models.IntegerField(verbose_name='Elderly 60y/o above (F)')
    num_ip_male = models.IntegerField(verbose_name='IP (M)')
    num_ip_female = models.IntegerField(verbose_name='IP (F)')

    class Meta:
       db_table = 'flood_report'
       verbose_name_plural = "Flood"




