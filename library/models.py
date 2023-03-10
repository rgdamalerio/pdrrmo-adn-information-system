from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

class MunicipalitiesManager(models.Manager):
    def get_by_natural_key(self, munname):
        return self.get(municipality_name=munname)

# Create your models here.
class Municipalities(models.Model):
  psgccode = models.CharField(max_length=255,primary_key=True)
  munname = models.CharField(max_length=255,unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  objects = MunicipalitiesManager()

  def __str__(self):
        return self.munname
  
  def natural_key(self):
        return (self.munname)

  class Meta:
    verbose_name_plural = "Municipalities"

class BarangaysManager(models.Manager):
    def get_by_natural_key(self, brgyname):
        return self.get(barangay_name=brgyname)

class Barangays(models.Model):
  psgcmun = models.ForeignKey(Municipalities,on_delete=models.CASCADE)
  psgccode = models.CharField(max_length=255,primary_key=True)
  brgyname = models.CharField(max_length=255)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  objects = BarangaysManager()

  def __str__(self):
    return self.brgyname

  def natural_key(self):
    return (self.brgyname)

  class Meta:
    verbose_name_plural = "Barangays"

class Purok(models.Model):
  purok_id = models.AutoField(primary_key=True)
  purok_name = models.CharField(max_length=255, verbose_name="Purok")
  psgccode_brgy = models.ForeignKey(Barangays, null=True, on_delete=models.CASCADE, verbose_name="Barangay")

  def __str__(self):
    return self.purok_name
  
  class Meta:
    verbose_name_plural = "Purok"

class BuildingroofmaterialsManager(models.Manager):
    def get_by_natural_key(self, description):
        return self.get(Buildingroofmaterials_description=description)

class Buildingroofmaterials(models.Model):
  description = models.TextField(unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  objects = BuildingroofmaterialsManager()

  def __str__(self):
    return self.description

  def natural_key(self):
    return (self.description)

  class Meta:
    verbose_name_plural = "Building roof materials"

class Buildingstatus(models.Model):
  status = models.TextField(unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.status

  class Meta:
    verbose_name_plural = "Building status"
    ordering = ['pk']

class Buildingtypes(models.Model):
  type = models.TextField(unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.type

  class Meta:
    verbose_name_plural = "Building types"
    ordering = ['pk']

class Buildinguses(models.Model):
  use = models.CharField(max_length=255,unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.use

  class Meta:
    verbose_name_plural = "Building uses"
    ordering = ['pk']

class BuildingwallmaterialsManager(models.Manager):
    def get_by_natural_key(self, material):
        return self.get(Buildingwallmaterials_material=material)

class Buildingwallmaterials(models.Model):
  material = models.TextField(unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  objects = BuildingwallmaterialsManager()

  def __str__(self):
    return self.material

  def natural_key(self):
    return (self.material)

  class Meta:
    verbose_name_plural = "Building wall materials"
    ordering = ['pk']

class Disabilities(models.Model):
  description = models.CharField(max_length=255,unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.description

  class Meta:
    verbose_name_plural = "Disabilities"
    ordering = ['pk']

class Farmingtechs(models.Model):
  technology = models.CharField(max_length=125,unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.technology

  class Meta:
    verbose_name_plural = "Farming technology"
    ordering = ['pk']

class Genders(models.Model):
  gender = models.CharField(max_length=50,unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.gender

  class Meta:
    verbose_name_plural = "Genders"
    ordering = ['pk']

class Gradelevels(models.Model):
  code = models.IntegerField(primary_key=True,unique=True)
  description = models.CharField(max_length=255,unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.description

  class Meta:
    verbose_name_plural = "Grade levels"
    ordering = ['pk']

class EvacuationareasManager(models.Manager):
    def get_by_natural_key(self, evacuation_area):
        return self.get(Evacuationareas_evacuation_area=evacuation_area)

class Evacuationareas(models.Model):
  evacuation_area = models.CharField(max_length=255,unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  objects = EvacuationareasManager()

  def __str__(self):
    return self.evacuation_area

  def natural_key(self):
    return (self.evacuation_area)

  class Meta:
    verbose_name_plural = "Evacuation areas"
    ordering = ['pk']

class WaterlevelsystemsManager(models.Manager):
    def get_by_natural_key(self, description):
        return self.get(Waterlevelsystems_description=description)

class Waterlevelsystems(models.Model):
  level = models.CharField(max_length=50,unique=True)
  description = models.TextField(unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  objects = WaterlevelsystemsManager()

  def __str__(self):
    return self.description

  def natural_key(self):
    return (self.description)

  class Meta:
    verbose_name_plural = "Water level systems"
    ordering = ['pk']

class HouseholdroofmaterialsManager(models.Manager):
    def get_by_natural_key(self, description):
        return self.get(Householdroofmaterials_description=description)


class Householdroofmaterials(models.Model):
  description = models.TextField(unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  objects = HouseholdroofmaterialsManager()

  def __str__(self):
    return self.description

  def natural_key(self):
    return (self.description)

  class Meta:
    verbose_name_plural = "Household roof materials"
    ordering = ['pk']

class HouseholdtenuralstatusManager(models.Manager):
    def get_by_natural_key(self, description):
        return self.get(Householdtenuralstatus_description=description)

class Householdtenuralstatus(models.Model):
  description = models.TextField(unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  objects = HouseholdtenuralstatusManager()

  def __str__(self):
    return self.description

  def natural_key(self):
    return (self.description)

  class Meta:
    verbose_name_plural = "Household tenural status"
    ordering = ['pk']

class HouseholdbuildingtypesManager(models.Manager):
    def get_by_natural_key(self, type):
        return self.get(Householdbuildingtypes_type=type)

class Householdbuildingtypes(models.Model):
  type = models.TextField(unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  objects = HouseholdbuildingtypesManager()

  def __str__(self):
    return self.type

  def natural_key(self):
    return (self.type)

  class Meta:
    verbose_name_plural = "Household building types"
    ordering = ['pk']

class Householdwallmaterials(models.Model):
  description = models.TextField(unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.description

  class Meta:
    verbose_name_plural = "Household wall materials"
    ordering = ['pk']

class HouseholdwatertenuralstatusManager(models.Manager):
    def get_by_natural_key(self, status):
        return self.get(Householdwatertenuralstatus_description=status)

class Householdwatertenuralstatus(models.Model):
  status = models.CharField(max_length=50,unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  objects = HouseholdwatertenuralstatusManager()

  def __str__(self):
    return self.status

  def natural_key(self):
    return (self.status)

  class Meta:
    verbose_name_plural = "Household water tenural status"
    ordering = ['pk']

class Livelihoods(models.Model):
  description = models.TextField(unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.description

  class Meta:
    verbose_name_plural = "Livelihoods"
    ordering = ['pk']

class Maritalstatus(models.Model):
  status = models.CharField(max_length=25,unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.status

  class Meta:
    verbose_name_plural = "Marital status"
    ordering = ['pk']

class Monthlyincomes(models.Model):
  income = models.CharField(max_length=25,unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.income

  class Meta:
    verbose_name_plural = "Monthly incomes"
    ordering = ['pk']

class Nutritionalstatus(models.Model):
  status = models.CharField(max_length=25,unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.status

  class Meta:
    verbose_name_plural = "Nutritional status"
    ordering = ['pk']

class Relationshiptoheads(models.Model):
  relationship = models.CharField(max_length=50,unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.relationship

  class Meta:
    verbose_name_plural = "Relationship to head"
    ordering = ['pk']

class Livelihoodtenuralstatus(models.Model):
  status = models.CharField(max_length=250,unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.status

  class Meta:
    verbose_name_plural = "Livelihood tenural status"
    ordering = ['pk']

class Trackstrandcourses(models.Model):
  description = models.CharField(max_length=250,unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.description

  class Meta:
    verbose_name_plural = "Track/strand/courses"
    ordering = ['pk']

class Typeofprograms(models.Model):
  type = models.CharField(max_length=250,unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.type

  class Meta:
    verbose_name_plural = "Type of programs"
    ordering = ['pk']