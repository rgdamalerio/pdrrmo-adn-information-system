from pyexpat import model
from django.utils.translation import gettext as _
from django.db import models
from django.contrib.gis.db import models
from library.models import Municipalities, Barangays, Householdbuildingtypes, \
  Householdtenuralstatus, Householdroofmaterials, Buildingwallmaterials, \
  Householdwatertenuralstatus, Waterlevelsystems, Evacuationareas, Relationshiptoheads, \
  Genders, Maritalstatus, Disabilities, Nutritionalstatus, Gradelevels, Trackstrandcourses, \
  Monthlyincomes, Typeofprograms, Livelihoods, Livelihoodtenuralstatus
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

  def getBarangay(self):
    brgycode = self.barangay
    return brgycode

  controlnumber = models.TextField(primary_key=True)
  purok = models.CharField(max_length=25,null=True)
  longitude = models.CharField(max_length=50,null=True)
  latitude = models.CharField(max_length=50,null=True)
  location = models.PointField(srid=4326)
  respondent = models.CharField(max_length=50)
  date_interview = models.DateField(_('Date interviewed'))
  enumerator = models.CharField(max_length=50)
  editor = models.CharField(max_length=50)
  year_construct = models.IntegerField(_('Building/House year construct'),validators=[MinValueValidator(1940), max_value_current_year])
  estimated_cost = models.IntegerField()
  number_bedrooms = models.SmallIntegerField()
  number_storey = models.SmallIntegerField()
  access_electricity = models.BooleanField(_('Access to electricity'))
  access_internet = models.BooleanField(_('Access to internet'))
  medical_treatment = models.TextField(null=True,blank=True)
  access_water_supply = models.BooleanField(_('Access to water supply'))
  potable = models.BooleanField(_('Safe to drink'))
  floods_occur = models.BooleanField(_('Flood occur in your area'))
  year_flooded = models.IntegerField(validators=[MinValueValidator(1940), max_value_current_year],null=True)
  experience_evacuate = models.BooleanField(_('Experience evacuation during calamity'))
  year_evacuate = models.IntegerField(validators=[MinValueValidator(1940), max_value_current_year],null=True,blank=True)
  access_health_medical_facility = models.BooleanField(_('Access to health and medical facility'))
  access_telecommuniciation = models.BooleanField(_('Access to telecommunication'))
  access_drill_simulation = models.BooleanField(_('Access/Join drill and simulation'))
  image = models.ImageField(upload_to ='uploads/'+ str(getBarangay) + '/',null=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,default=1)
  municipality = models.ForeignKey(Municipalities,to_field="psgccode",null=True,on_delete=models.SET_NULL,verbose_name='Municipality')
  barangay = models.ForeignKey(Barangays,to_field="psgccode",on_delete=models.SET_NULL,null=True,verbose_name='Barangay')
  householdbuildingtypes = models.ForeignKey(Householdbuildingtypes,null=True,on_delete=models.SET_NULL,verbose_name='Building types')
  householdtenuralstatus = models.ForeignKey(Householdtenuralstatus,null=True,on_delete=models.SET_NULL,verbose_name='Tenural status')
  householdroofmaterials = models.ForeignKey(Householdroofmaterials,null=True,on_delete=models.SET_NULL,verbose_name='Roof material')
  householdwallmaterials = models.ForeignKey(Buildingwallmaterials,null=True,on_delete=models.SET_NULL,verbose_name='Wall material')
  householdwatertenuralstatus = models.ForeignKey(Householdwatertenuralstatus,null=True,on_delete=models.SET_NULL,verbose_name='Water tenural status')
  waterlevelsystems = models.ForeignKey(Waterlevelsystems,null=True,on_delete=models.SET_NULL,verbose_name='Level of water system')
  evacuationareas = models.ForeignKey(Evacuationareas,null=True,on_delete=models.SET_NULL,verbose_name='Nearest evacuation center')

  
  def __str__(self):
    return self.respondent

  def munname(self):
    return self.municipality.munname

  class Meta:
    verbose_name_plural = "Households"

  class MyForm(forms.ModelForm):
    year = forms.TypedChoiceField(coerce=int, choices=year_choices, initial=current_year)

class Demographies(models.Model):
  controlnumber = models.ForeignKey(Households,null=True,on_delete=models.SET_NULL,verbose_name='Housedhold belong')
  lastname = models.CharField(max_length=50)
  firstname = models.CharField(max_length=50)
  middlename = models.CharField(max_length=50,null=True)
  extension = models.CharField(max_length=15,null=True,blank=True)
  nuclear_family = models.ForeignKey('self',on_delete=models.SET_NULL,verbose_name='Nuclear family belongs to',null=True,blank=True)
  relationshiptohead =  models.ForeignKey(Relationshiptoheads,null=True,on_delete=models.SET_NULL,verbose_name='Relationship to head')
  gender = models.ForeignKey(Genders,null=True,on_delete=models.SET_NULL,verbose_name='Gender')
  birthdate = models.DateField()
  marital_status = models.ForeignKey(Maritalstatus,null=True,on_delete=models.SET_NULL)
  ethnicity_by_blood = models.CharField(max_length=150,null=True,blank=True,verbose_name='Belongs to tribe/enthics')
  member_ip = models.BooleanField(verbose_name='Member of IP\'s')
  informal_settler = models.BooleanField()
  religion = models.CharField(max_length=150)
  person_with_special_needs = models.BooleanField()
  type_of_disability = models.ForeignKey(Disabilities,on_delete=models.SET_NULL,null=True,blank=True)
  is_ofw = models.BooleanField(verbose_name='Is OFW')
  residence = models.BooleanField()
  nutritional_status = models.ForeignKey(Nutritionalstatus,null=True,on_delete=models.SET_NULL)
  nutritional_status_recorded = models.DateField(null=True,blank=True)
  currently_attending_school = models.BooleanField(verbose_name='Currently attending in school')
  current_grade_level_attending = models.ForeignKey(Gradelevels,related_name='current_attending',on_delete=models.SET_NULL,null=True,blank=True)
  highest_eductional_attainment = models.ForeignKey(Gradelevels,related_name='%(class)s_highest_attending',on_delete=models.SET_NULL,null=True)
  course_completed_vocational = models.ForeignKey(Trackstrandcourses,on_delete=models.SET_NULL,verbose_name='Track/Strand/Course completed (for senior High school/Vocational/College)',null=True,blank=True)
  can_read_and_write = models.BooleanField(verbose_name='Can read and write or atleast high school graduate')
  primary_occupation = models.CharField(max_length=255,null=True,blank=True)
  monthly_income = models.ForeignKey(Monthlyincomes,null=True,on_delete=models.SET_NULL)
  sss_member = models.BooleanField()
  gsis_member = models.BooleanField()
  philhealth_member = models.BooleanField()
  dependent_of_philhealth_member = models.BooleanField()
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,default=1)


  def __str__(self):
    return str(self.lastname) +" "+ str(self.firstname) +" "+ str(self.middlename)


  class Meta:
    verbose_name_plural = "Demographies"


class Availprograms(models.Model):
  controlnumber = models.ForeignKey(Households,null=True,on_delete=models.SET_NULL,verbose_name='Housedhold belong')
  type_of_program = models.ForeignKey(Typeofprograms,null=True,on_delete=models.SET_NULL)
  name_of_program = models.CharField(max_length=150)
  number_of_beneficiaries = models.SmallIntegerField()
  program_implementor = models.CharField(max_length=150)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,default=1)

  def __str__(self):
    return self.name_of_program

  def save(self, *args, **kwargs):
    for field_name in ['program_implementor']:
        val = getattr(self, field_name, False)
        if val:
            setattr(self, field_name, val.capitalize())
    super(Availprograms, self).save(*args, **kwargs)

  class Meta:
    verbose_name_plural = "Avail Programs"

class Hhlivelihoods(models.Model):
  controlnumber = models.ForeignKey(Households,null=True,on_delete=models.SET_NULL,verbose_name='Housedhold belong')
  livelihood = models.ForeignKey(Livelihoods,null=True,on_delete=models.SET_NULL)
  market_value = models.IntegerField()
  products = models.CharField(max_length=255)
  area = models.FloatField(null=True,blank=True)
  livelihood_tenural_status = models.ForeignKey(Livelihoodtenuralstatus,null=True,on_delete=models.SET_NULL)
  with_insurance = models.BooleanField()
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,default=1)

  def __str__(self):
    return self.livelihood.description

  class Meta:
    verbose_name_plural = "Livelihoods"