from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Municipalities(models.Model):
  psgccode = models.CharField(max_length=255,primary_key=True)
  munname = models.CharField(max_length=255,unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
        return self.munname

  class Meta:
    verbose_name_plural = "Municipalities"


class Barangays(models.Model):
  psgcmun = models.ForeignKey(Municipalities,on_delete=models.CASCADE)
  psgccode = models.CharField(max_length=255,primary_key=True)
  brgyname = models.CharField(max_length=255)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.brgyname

  class Meta:
    verbose_name_plural = "Barangays"

class Buildingroofmaterials(models.Model):
  description = models.TextField(unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.description

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

class Buildingwallmaterials(models.Model):
  material = models.TextField(unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.material

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

class Evacuationareas(models.Model):
  evacuation_area = models.CharField(max_length=255,unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.evacuation_area

  class Meta:
    verbose_name_plural = "Evacuation areas"
    ordering = ['pk']

class Waterlevelsystems(models.Model):
  level = models.CharField(max_length=50,unique=True)
  description = models.TextField(unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.description

  class Meta:
    verbose_name_plural = "Water level systems"
    ordering = ['pk']

class Householdroofmaterials(models.Model):
  description = models.TextField(unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.description

  class Meta:
    verbose_name_plural = "Household roof materials"
    ordering = ['pk']

class Householdtenuralstatus(models.Model):
  description = models.TextField(unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.description

  class Meta:
    verbose_name_plural = "Household tenural status"
    ordering = ['pk']

class Householdbuildingtypes(models.Model):
  type = models.TextField(unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.type

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

class Householdwatertenuralstatus(models.Model):
  status = models.CharField(max_length=50,unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.status

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