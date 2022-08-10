from django.utils.translation import gettext as _
from django.db import models
from django.contrib.gis.db import models
from library.models import Municipalities, Barangays, Householdbuildingtypes, \
  Householdtenuralstatus, Householdroofmaterials, Buildingwallmaterials, \
  Householdwatertenuralstatus, Waterlevelsystems, Evacuationareas
from django.contrib.auth.models import User
from django import forms

import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)    

def year_choices():
    return [(r,r) for r in range(1940, datetime.date.today().year+1)]


# Create your models here.
class Households(models.Model):
  controlnumber = models.TextField(primary_key=True)
  purok = models.CharField(max_length=25,null=True)
  longitude = models.CharField(max_length=50,null=True)
  latitude = models.CharField(max_length=50,null=True)
  location = models.PointField(srid=4326)
  respondent = models.CharField(max_length=50)
  date_interview = models.DateField(_('Date interviewed'))
  enumerator = models.CharField(max_length=50)
  editor = models.CharField(max_length=50)
  year_construct = models.IntegerField(_('Building/House year construct'),validators=[MinValueValidator(1940), max_value_current_year],default=current_year())
  estimated_cost = models.IntegerField()
  number_bedrooms = models.SmallIntegerField()
  number_storey = models.SmallIntegerField()
  access_electricity = models.BooleanField(_('Access to electricity'))
  access_internet = models.BooleanField(_('Access to internet'))
  medical_treatment = models.TextField(null=True)
  access_water_supply = models.BooleanField(_('Access to water supply'))
  potable = models.BooleanField(_('Safe to drink'))
  floods_occur = models.BooleanField(_('Flood occur in your area'))
  year_flooded = models.IntegerField(validators=[MinValueValidator(1940), max_value_current_year],default=current_year(),null=True)
  experience_evacuate = models.BooleanField(_('Experience evacuation during calamity'))
  year_evacuate = models.IntegerField(validators=[MinValueValidator(1940), max_value_current_year],default=current_year(),null=True)
  access_health_medical_facility = models.BooleanField(_('Access to health and medical facility'))
  access_telecommuniciation = models.BooleanField(_('Access to telecommunication'))
  access_drill_simulation = models.BooleanField(_('Access/Join drill and simulation'))
  image = models.ImageField(upload_to ='uploads/',null=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,default=1)
  municipality = models.ForeignKey(Municipalities,to_field="psgccode",on_delete=models.CASCADE,verbose_name='Municipality')
  barangay = models.ForeignKey(Barangays,to_field="psgccode",on_delete=models.CASCADE,null=True,verbose_name='Barangay')
  householdbuildingtypes = models.ForeignKey(Householdbuildingtypes,on_delete=models.CASCADE,verbose_name='Building types')
  householdtenuralstatus = models.ForeignKey(Householdtenuralstatus,on_delete=models.CASCADE,verbose_name='Tenural status')
  householdroofmaterials = models.ForeignKey(Householdroofmaterials,on_delete=models.CASCADE,verbose_name='Roof material')
  householdwallmaterials = models.ForeignKey(Buildingwallmaterials,on_delete=models.CASCADE,verbose_name='Wall material')
  householdwatertenuralstatus = models.ForeignKey(Householdwatertenuralstatus,on_delete=models.CASCADE,verbose_name='Water tenural status')
  waterlevelsystems = models.ForeignKey(Waterlevelsystems,on_delete=models.CASCADE,verbose_name='Level of water system')
  evacuationareas = models.ForeignKey(Evacuationareas,on_delete=models.CASCADE,verbose_name='Nearest evacuation center')

  def __str__(self):
    return self.respondent

  class Meta:
    verbose_name_plural = "Households"

  class MyForm(forms.ModelForm):
    year = forms.TypedChoiceField(coerce=int, choices=year_choices, initial=current_year)
