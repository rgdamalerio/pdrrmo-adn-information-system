from pyexpat import model
from django.utils.translation import gettext as _
from django.db import models
from django.contrib.gis.db import models
from library.models import Municipalities, Barangays, Householdbuildingtypes, \
  Householdtenuralstatus, Householdroofmaterials, Buildingwallmaterials, \
  Householdwatertenuralstatus, Waterlevelsystems, Evacuationareas, Relationshiptoheads, \
  Genders, Maritalstatus, Disabilities, Nutritionalstatus, Gradelevels, Trackstrandcourses, \
  Monthlyincomes, Typeofprograms, Livelihoods, Livelihoodtenuralstatus, Purok, Familystatus,Familyrelationship
from django.contrib.auth.models import User
from django import forms
import uuid
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)    

def year_choices():
    return [(r,r) for r in range(1900, datetime.date.today().year+1)]


class Households(models.Model):
  def getBarangay(self):
    brgycode = self.barangay
    return brgycode
  controlnumber = models.TextField(primary_key=True)
  def save(self, *args, **kwargs):
    if not self.controlnumber: 
        self.controlnumber = str(uuid.uuid4())
    super(Households, self).save(*args, **kwargs)

  purok_fk = models.ForeignKey(Purok,null=True,on_delete=models.SET_NULL,verbose_name='Purok')
  longitude = models.CharField(max_length=50,null=True)
  latitude = models.CharField(max_length=50,null=True)
  location = models.PointField(srid=4326,null=True,)
  respondent = models.CharField(max_length=50,null=True)
  date_interview = models.DateField(_('Date interviewed'))
  enumerator = models.CharField(max_length=50,null=True)
  editor = models.CharField(max_length=50,null=True)
  year_construct = models.IntegerField(_('Building/House year construct'),validators=[MinValueValidator(1900), max_value_current_year],null=True)
  estimated_cost = models.IntegerField(null=True)
  number_bedrooms = models.SmallIntegerField(null=True)
  number_storey = models.SmallIntegerField(null=True)
  access_electricity = models.BooleanField(_('Access to electricity'),null=True)
  access_internet = models.BooleanField(_('Access to internet'),null=True)
  medical_treatment = models.TextField(null=True,blank=True)
  access_water_supply = models.BooleanField(_('Access to water supply'),null=True)
  potable = models.BooleanField(_('Safe to drink'),null=True)
  floods_occur = models.BooleanField(_('Flood occur in your area'),null=True)
  year_flooded = models.IntegerField(validators=[MinValueValidator(1900), max_value_current_year],null=True,blank=True)
  experience_evacuate = models.BooleanField(_('Experienced evacuation during calamity'))
  year_evacuate = models.IntegerField(validators=[MinValueValidator(1900), max_value_current_year],null=True,blank=True)
  access_health_medical_facility = models.BooleanField(_('Access to health and medical facility'),null=True)
  access_telecommuniciation = models.BooleanField(_('Access to telecommunication'),null=True)
  access_drill_simulation = models.BooleanField(_('Access/Join drill and simulation'),null=True)
  image = models.ImageField(upload_to ='uploads/',null=True)
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
    return str(self.respondent)
  
  def munname(self):
    return self.municipality.munname
  
  def household_controlnumber(self):
    return str(self.controlnumber)[:20] + "..."
  
  class Meta:
    verbose_name_plural = "Households"

  class MyForm(forms.ModelForm):
    year = forms.TypedChoiceField(coerce=int, choices=year_choices, initial=current_year)

class Demographies(models.Model):
  controlnumber = models.ForeignKey(Households,null=True,on_delete=models.SET_NULL,verbose_name='Housedhold belong')
  lastname = models.CharField(max_length=50)
  firstname = models.CharField(max_length=50)
  middlename = models.CharField(max_length=50,null=True,blank=True)
  extension = models.CharField(max_length=15,null=True,blank=True,verbose_name='Ext.')
  nuclear_family = models.ForeignKey('self',on_delete=models.SET_NULL,verbose_name='Nuclear family belongs to',null=True,blank=True)
  relationshiptohead =  models.ForeignKey(Relationshiptoheads,null=True,on_delete=models.SET_NULL,verbose_name='Relationship to head')
  gender = models.ForeignKey(Genders,null=True,on_delete=models.SET_NULL,verbose_name='Sex')
  birthdate = models.DateField()
  marital_status = models.ForeignKey(Maritalstatus,null=True,on_delete=models.SET_NULL)
  ethnicity_by_blood = models.CharField(max_length=150,null=True,blank=True,verbose_name='Belongs to tribe/enthics')
  member_ip = models.BooleanField(verbose_name='Member of IP\'s',null=True,blank=True)
  informal_settler = models.BooleanField(null=True)
  religion = models.CharField(max_length=150,null=True,blank=True)
  person_with_special_needs = models.BooleanField(null=True,verbose_name='Person w/ special needs')
  type_of_disability = models.ForeignKey(Disabilities,on_delete=models.SET_NULL,null=True,blank=True)
  is_ofw = models.BooleanField(verbose_name='Is OFW',null=True)
  residence = models.BooleanField(null=True,blank=True)
  nutritional_status = models.ForeignKey(Nutritionalstatus,null=True,on_delete=models.SET_NULL)
  nutritional_status_recorded = models.DateField(null=True,blank=True)
  currently_attending_school = models.BooleanField(verbose_name='Currently attending in school',null=True)
  current_grade_level_attending = models.ForeignKey(Gradelevels,related_name='current_attending',on_delete=models.SET_NULL,null=True,blank=True)
  highest_eductional_attainment = models.ForeignKey(Gradelevels,related_name='%(class)s_highest_attending',on_delete=models.SET_NULL,null=True)
  course_completed_vocational = models.ForeignKey(Trackstrandcourses,on_delete=models.SET_NULL,verbose_name='Track/Strand/Course completed (for senior High school/Vocational/College)',null=True,blank=True)
  can_read_and_write = models.BooleanField(verbose_name='Can read & write',null=True,blank=True)
  primary_occupation = models.CharField(max_length=255,null=True,blank=True)
  monthly_income = models.ForeignKey(Monthlyincomes,null=True,on_delete=models.SET_NULL)
  sss_member = models.BooleanField(null=True)
  gsis_member = models.BooleanField(null=True)
  philhealth_member = models.BooleanField(null=True)
  dependent_of_philhealth_member = models.BooleanField(null=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,verbose_name='Created by')

  def __str__(self):
    return f"{str(self.firstname)} {str(self.middlename)} {str(self.lastname)}"
  
  def format_birthdate(self):
      return self.birthdate.strftime("%m-%d-%Y")
  
  class Meta:
    verbose_name = "Individual"
    verbose_name_plural = "Individuals"

class Families(models.Model):
  fam_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
  household = models.ForeignKey(Households, on_delete=models.SET_NULL,null=True,blank=True,verbose_name='Household belong')
  family_head = models.ForeignKey(Demographies,on_delete=models.SET_NULL,null=True,blank=True,verbose_name='Head of the family')
  status = models.ForeignKey(Familystatus,on_delete=models.SET_NULL,null=True,blank=True,verbose_name='Family status')
  remarks = models.CharField(max_length=150,null=True,default='N/A')
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True,verbose_name='Created by')

  def __str__(self):
    return f"{self.family_head.firstname} {str(self.family_head.middlename)} {self.family_head.lastname}"

  class Meta:
    verbose_name = "Family"
    verbose_name_plural = "Families"

class Familydetails(models.Model):
  fam_fk = models.ForeignKey(Families,on_delete=models.SET_NULL,null=True,blank=True,verbose_name='Family head')
  fam_member = models.ForeignKey(Demographies,on_delete=models.SET_NULL,null=True,blank=True,verbose_name='Family member')
  relationship = models.ForeignKey(Familyrelationship,on_delete=models.SET_NULL,null=True,blank=True,verbose_name='Relationship to head')
  remarks = models.CharField(max_length=150,null=True,default='N/A')
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,verbose_name='Created by')

  def __str__(self):
    return str(self.fam_fk)
  
  class Meta:
    verbose_name = "Family Member"
    verbose_name_plural = "Demographies"


class Availprograms(models.Model):
  controlnumber = models.ForeignKey(Households,null=True,on_delete=models.SET_NULL,verbose_name='Beneficiary')
  type_of_program = models.ForeignKey(Typeofprograms,null=True,on_delete=models.SET_NULL)
  name_of_program = models.CharField(max_length=150)
  number_of_beneficiaries = models.SmallIntegerField(verbose_name='No. of beneficiaries')
  program_implementor = models.CharField(max_length=150)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,default=1,verbose_name='Created by')

  def __str__(self):
    return self.name_of_program
  
  def upper_progimplementor(self):
    return self.program_implementor.upper()
  
  upper_progimplementor.short_description = 'Program Implementor'
  
  class Meta:
    verbose_name_plural = "Availed Programs"

class Hhlivelihoods(models.Model):
  controlnumber = models.ForeignKey(Households,null=True,on_delete=models.SET_NULL,verbose_name='Livelihood belong')
  livelihood = models.ForeignKey(Livelihoods,null=True,on_delete=models.SET_NULL)
  market_value = models.IntegerField()
  products = models.CharField(max_length=255)
  area = models.FloatField(null=True,blank=True)
  livelihood_tenural_status = models.ForeignKey(Livelihoodtenuralstatus,null=True,on_delete=models.SET_NULL)
  with_insurance = models.BooleanField()
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,default=1,verbose_name='Created by')

  def __str__(self):
    return self.livelihood.description

  class Meta:
    verbose_name_plural = "Livelihoods"
