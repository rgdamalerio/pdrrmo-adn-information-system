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

class Buildingtypes(models.Model):
  type = models.TextField(unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.type

  class Meta:
    verbose_name_plural = "Building types"

class Buildinguses(models.Model):
  use = models.CharField(max_length=255,unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.use

  class Meta:
    verbose_name_plural = "Building uses"

class Buildingwallmaterials(models.Model):
  material = models.TextField(unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.material

  class Meta:
    verbose_name_plural = "Building wall materials"

class Disabilities(models.Model):
  description = models.CharField(max_length=255,unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.description

  class Meta:
    verbose_name_plural = "Disabilities"

class Farmingtechs(models.Model):
  technology = models.CharField(max_length=125,unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.technology

  class Meta:
    verbose_name_plural = "Farming technology"

class Genders(models.Model):
  gender = models.CharField(max_length=50,unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.gender

  class Meta:
    verbose_name_plural = "Genders"

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

class Evacuationareas(models.Model):
  evacuation_area = models.CharField(max_length=255,unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.evacuation_area

  class Meta:
    verbose_name_plural = "Evacuation areas"

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

class Householdroofmaterials(models.Model):
  description = models.TextField(unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.description

  class Meta:
    verbose_name_plural = "Household roof materials"

class Householdtenuralstatus(models.Model):
  description = models.TextField(unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.description

  class Meta:
    verbose_name_plural = "Household tenural status"

class Householdbuildingtypes(models.Model):
  type = models.TextField(unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.type

  class Meta:
    verbose_name_plural = "Household building types"

class Householdwallmaterials(models.Model):
  description = models.TextField(unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.description

  class Meta:
    verbose_name_plural = "Household wall materials"

class Householdwatertenuralstatus(models.Model):
  status = models.CharField(max_length=50,unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.status

  class Meta:
    verbose_name_plural = "Household water tenural status"

class Livelihoods(models.Model):
  description = models.TextField(unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.description

  class Meta:
    verbose_name_plural = "Livelihoods"

class Maritalstatus(models.Model):
  status = models.CharField(max_length=25,unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.status

  class Meta:
    verbose_name_plural = "Marital status"

class Monthlyincomes(models.Model):
  income = models.CharField(max_length=25,unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.income

  class Meta:
    verbose_name_plural = "Monthly incomes"

class Nutritionalstatus(models.Model):
  status = models.CharField(max_length=25,unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.status

  class Meta:
    verbose_name_plural = "Nutritional status"

class Relationshiptoheads(models.Model):
  relationship = models.CharField(max_length=50,unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.relationship

  class Meta:
    verbose_name_plural = "Relationship to head"

class Livelihoodtenuralstatus(models.Model):
  status = models.CharField(max_length=250,unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.status

  class Meta:
    verbose_name_plural = "Livelihood tenural status"

class Trackstrandcourses(models.Model):
  description = models.CharField(max_length=250,unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.description

  class Meta:
    verbose_name_plural = "Track/strand/courses"

class Typeofprograms(models.Model):
  type = models.CharField(max_length=250,unique=True)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.type

  class Meta:
    verbose_name_plural = "Type of programs"