from email.policy import default
from tabnanny import verbose
from django.db import models
from library.models import Municipalities, Barangays

# Create your models here.
class Familiesandpopulation(models.Model):
  fp_id = models.BigAutoField(primary_key=True)
  municipality = models.ForeignKey(Municipalities,to_field="psgccode",on_delete=models.CASCADE,verbose_name='Municipality')
  barangay = models.ForeignKey(Barangays,to_field="psgccode",on_delete=models.CASCADE,null=True,verbose_name='Barangay')
  num_of_family = models.IntegerField(default=0,verbose_name='No. of Families')
  num_of_individuals_m = models.IntegerField(verbose_name='Individuals (M)')
  num_of_individuals_f = models.IntegerField(verbose_name='Individuals (F)')
  num_of_infant_m = models.IntegerField(verbose_name='Infant 0-11months (M)')
  num_of_infant_f = models.IntegerField(verbose_name='Infant 0-11months (F)')
  num_of_children_m = models.IntegerField(verbose_name='Children 1-17y/o (M)')
  num_of_children_f = models.IntegerField(verbose_name='Children 1-17y/o (F)')
  num_of_adult_m = models.IntegerField(verbose_name='Adult 18-59y/o (M)')
  num_of_adult_f = models.IntegerField(verbose_name='Adult 18-59y/o (F)')
  num_of_elderly_m = models.IntegerField(verbose_name='Elderly 60y/o above (M)')
  num_of_elderly_f = models.IntegerField(verbose_name='Elderly 60y/o above (F)')
  num_of_pwd_m = models.IntegerField(verbose_name='PWD (M)')
  num_of_pwd_f = models.IntegerField(verbose_name='PWD (F)')
  num_of_ip_m = models.IntegerField(verbose_name='IP (M)')
  num_of_ip_f = models.IntegerField(verbose_name='IP (F)')

  #def __str__(self):
  #  return self.fp_id

  class Meta:
    verbose_name_plural = "No. of families and population"
    ordering = ['municipality','barangay']
    
class AggregatedFamiliesandPopulation(models.Model):
  munname = models.CharField(primary_key=True,max_length=50,verbose_name='Municipality')
  brgyname = models.CharField(max_length=50,null=True,verbose_name='Barangay')
  households = models.IntegerField(default=0,verbose_name='No. of Households')
  families = models.IntegerField(default=0,verbose_name='No. of Families')
  male = models.IntegerField(default=0,verbose_name='Individuals (M)')
  female = models.IntegerField(verbose_name='Individuals (F)')
  male_infant = models.IntegerField(verbose_name='Infant 0-11months (M)')
  female_infant = models.IntegerField(verbose_name='Infant 0-11months (F)')
  male_children = models.IntegerField(verbose_name='Children 1-17y/o (M)')
  female_children = models.IntegerField(verbose_name='Children 1-17y/o (F)')
  male_adult = models.IntegerField(verbose_name='Adult 18-59y/o (M)')
  female_adult = models.IntegerField(verbose_name='Adult 18-59y/o (F)')
  male_elderly = models.IntegerField(verbose_name='Elderly 60y/o above (M)')
  female_elderly = models.IntegerField(verbose_name='Elderly 60y/o above (F)')
  ip_male = models.IntegerField(verbose_name='IP (M)')
  ip_female = models.IntegerField(verbose_name='IP (F)')

  class Meta:
    db_table = 'aggregate'
    verbose_name_plural = "No. of families and population"

# Create your models here.

# class Sampletable(models.Model):
#   stpsgccode = models.CharField(max_length=255,primary_key=True)
#   stmunname = models.CharField(max_length=255,unique=True)
#   stcreated_at = models.DateField(auto_now_add=True)
#   stupdated_at = models.DateField(auto_now=True)

#   def __str__(self):
#         return self.munname

#   class Meta:
#     verbose_name_plural = "Sampletable"