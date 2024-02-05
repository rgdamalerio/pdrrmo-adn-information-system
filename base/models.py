from django.db import models
from django.contrib.gis.db import models
from library.models import Municipalities, Barangays, Householdbuildingtypes, \
  Householdtenuralstatus, Householdroofmaterials, Buildingwallmaterials, \
  Householdwatertenuralstatus, Waterlevelsystems, Evacuationareas, Relationshiptoheads, \
  Genders, Maritalstatus, Disabilities, Nutritionalstatus, Gradelevels, Trackstrandcourses, \
  Monthlyincomes, Typeofprograms, Livelihoods, Livelihoodtenuralstatus, Purok, Familystatus,Familyrelationship
from django.contrib.auth.models import User

class AdnFlood(models.Model):
    gid = models.IntegerField(primary_key=True)
    objectid = models.IntegerField()
    susc_ratin = models.CharField(max_length=255)
    shape_leng = models.FloatField()
    shape_area =  models.FloatField()
    descriptio = models.CharField(max_length=255)
    geom = models.PolygonField(srid=4326)
    
class Meta:
    db_table = 'adn_10kflood'


class Barangay(models.Model):
    gid = models.AutoField(primary_key=True)
    barangayna = models.CharField(max_length=64, blank=True, null=True)
    brgypsgc = models.IntegerField(blank=True, null=True)
    brgyarea = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    provname = models.CharField(max_length=50, blank=True, null=True)
    munname = models.CharField(max_length=50, blank=True, null=True)
    provpsgc = models.IntegerField(blank=True, null=True)
    regname = models.CharField(max_length=50, blank=True, null=True)
    regpsgc = models.IntegerField(blank=True, null=True)
    munpsgc = models.IntegerField(blank=True, null=True)
    brgypopn = models.IntegerField(blank=True, null=True)
    popden = models.FloatField(blank=True, null=True)
    munarea = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    munpopn = models.IntegerField(blank=True, null=True)
    avehhsize = models.FloatField(blank=True, null=True)
    land_sus = models.CharField(max_length=70, blank=True, null=True)
    area_ha = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    arm_confli = models.CharField(max_length=50, blank=True, null=True)
    mining_are = models.CharField(max_length=50, blank=True, null=True)
    flooded = models.FloatField(blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'barangay'


class Householdinfo(models.Model):
    household_number = models.TextField(primary_key=True,blank=True)
    geom = models.PointField(blank=True, null=True)
    lat = models.CharField(max_length=50, blank=True, null=True)
    long = models.CharField(max_length=50, blank=True, null=True)
    brgycode = models.CharField(max_length=255, blank=True, null=True)
    purok = models.CharField(max_length=255, blank=True, null=True)
    families = models.BigIntegerField(blank=True, null=True)
    person = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    infant_male = models.BigIntegerField(blank=True, null=True)
    infant_female = models.BigIntegerField(blank=True, null=True)
    elderly_male = models.BigIntegerField(blank=True, null=True)
    elderly_female = models.BigIntegerField(blank=True, null=True)
    drill = models.BigIntegerField(blank=True, null=True)
    philhealth = models.BigIntegerField(blank=True, null=True)
    sss_gsis = models.BigIntegerField(blank=True, null=True)
    illiteracy = models.BigIntegerField(blank=True, null=True)
    ip = models.BigIntegerField(blank=True, null=True)
    pwd = models.BigIntegerField(blank=True, null=True)
    malnurished = models.BigIntegerField(blank=True, null=True)


    class Meta:
        managed = False 
        db_table = 'householdInfo'


class Householdpermun(models.Model):
    munname = models.CharField(primary_key=True,max_length=255, blank=True)
    households = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False 
        db_table = 'householdpermun'


class Familiespermun(models.Model):
    munname = models.CharField(primary_key=True,max_length=255, blank=True)
    households = models.BigIntegerField(blank=True, null=True)
    families = models.BigIntegerField(blank=True, null=True)
    person = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    infant_male = models.BigIntegerField(blank=True, null=True)
    infant_female = models.BigIntegerField(blank=True, null=True)
    elderly_male = models.BigIntegerField(blank=True, null=True)
    elderly_female = models.BigIntegerField(blank=True, null=True)
    drill = models.BigIntegerField(blank=True, null=True)
    philhealth = models.BigIntegerField(blank=True, null=True)
    sss_gsis = models.BigIntegerField(blank=True, null=True)
    illiteracy = models.BigIntegerField(blank=True, null=True)
    ip = models.BigIntegerField(blank=True, null=True)
    pwd = models.BigIntegerField(blank=True, null=True)
    malnurished = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False  
        db_table = 'familiespermun'



class Brgyinfo(models.Model):
    munname = models.CharField(primary_key=True,max_length=255, blank=True)
    brgyname = models.CharField(max_length=255, blank=True, null=True)
    psgccode = models.CharField(max_length=255, blank=True, null=True)
    households = models.BigIntegerField(blank=True, null=True)
    families = models.BigIntegerField(blank=True, null=True)
    person = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    infant_male = models.BigIntegerField(blank=True, null=True)
    infant_female = models.BigIntegerField(blank=True, null=True)
    elderly_male = models.BigIntegerField(blank=True, null=True)
    elderly_female = models.BigIntegerField(blank=True, null=True)
    drill = models.BigIntegerField(blank=True, null=True)
    philhealth = models.BigIntegerField(blank=True, null=True)
    sss_gsis = models.BigIntegerField(blank=True, null=True)
    illiteracy = models.BigIntegerField(blank=True, null=True)
    ip = models.BigIntegerField(blank=True, null=True)
    pwd = models.BigIntegerField(blank=True, null=True)
    malnurished = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'brgyinfo'


class AdnTotalReport(models.Model):
    households = models.BigIntegerField(primary_key=True,blank=True)
    families = models.BigIntegerField(blank=True, null=True)
    person = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    infant = models.BigIntegerField(blank=True, null=True)
    elderly = models.BigIntegerField(blank=True, null=True)
    illiteracy = models.BigIntegerField(blank=True, null=True)
    ip = models.BigIntegerField(blank=True, null=True)
    pwd = models.BigIntegerField(blank=True, null=True)
    malnurished = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'adn_total_report'


class FloodHazardInfo(models.Model):
    municipality_name = models.CharField(primary_key=True,max_length=255, blank=True)
    flood_id = models.CharField(max_length=50, blank=True, null=True)
    barangay_name = models.CharField(max_length=255, blank=True, null=True)
    purok_name = models.CharField(max_length=255, blank=True, null=True)
    household_number = models.TextField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    lat = models.CharField(max_length=50, blank=True, null=True)
    long = models.CharField(max_length=50, blank=True, null=True)
    brgycode = models.CharField(max_length=255, blank=True, null=True)
    families = models.BigIntegerField(blank=True, null=True)
    person = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    infant_male = models.BigIntegerField(blank=True, null=True)
    infant_female = models.BigIntegerField(blank=True, null=True)
    elderly_male = models.BigIntegerField(blank=True, null=True)
    elderly_female = models.BigIntegerField(blank=True, null=True)
    drill = models.BigIntegerField(blank=True, null=True)
    philhealth = models.BigIntegerField(blank=True, null=True)
    sss_gsis = models.BigIntegerField(blank=True, null=True)
    illiteracy = models.BigIntegerField(blank=True, null=True)
    ip = models.BigIntegerField(blank=True, null=True)
    pwd = models.BigIntegerField(blank=True, null=True)
    malnurished = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'flood_hazard_info'


class FloodReportPerBarangay(models.Model):
    municipality_name = models.CharField(primary_key=True, max_length=255, blank=True)
    flood_id = models.CharField(max_length=50, blank=True, null=True)
    barangay_name = models.CharField(max_length=255, blank=True, null=True)
    brgycode = models.CharField(max_length=255, blank=True, null=True)
    household_number = models.BigIntegerField(blank=True, null=True)
    families = models.BigIntegerField(blank=True, null=True)
    person = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    infant_male = models.BigIntegerField(blank=True, null=True)
    infant_female = models.BigIntegerField(blank=True, null=True)
    elderly_male = models.BigIntegerField(blank=True, null=True)
    elderly_female = models.BigIntegerField(blank=True, null=True)
    drill = models.BigIntegerField(blank=True, null=True)
    philhealth = models.BigIntegerField(blank=True, null=True)
    sss_gsis = models.BigIntegerField(blank=True, null=True)
    illiteracy = models.BigIntegerField(blank=True, null=True)
    ip = models.BigIntegerField(blank=True, null=True)
    pwd = models.BigIntegerField(blank=True, null=True)
    malnurished = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'flood_report_per_barangay'


class OverAllFloodReport(models.Model):
    flood_id = models.CharField(primary_key=True, max_length=50, blank=True)
    household = models.BigIntegerField(blank=True, null=True)
    families = models.BigIntegerField(blank=True, null=True)
    person = models.BigIntegerField(blank=True, null=True)
    num_male = models.BigIntegerField(blank=True, null=True)
    num_female = models.BigIntegerField(blank=True, null=True)
    num_male_infant = models.BigIntegerField(blank=True, null=True)
    num_female_infant = models.BigIntegerField(blank=True, null=True)
    num_male_children = models.BigIntegerField(blank=True, null=True)
    num_female_children = models.BigIntegerField(blank=True, null=True)
    num_male_adult = models.BigIntegerField(blank=True, null=True)
    num_female_adult = models.BigIntegerField(blank=True, null=True)
    num_male_elderly = models.BigIntegerField(blank=True, null=True)
    num_female_elderly = models.BigIntegerField(blank=True, null=True)
    num_ip_male = models.BigIntegerField(blank=True, null=True)
    num_ip_female = models.BigIntegerField(blank=True, null=True)
    num_pwd_male = models.BigIntegerField(blank=True, null=True)
    num_pwd_female = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'over_all_flood_report'

# main table
class HouseholdHouseholds(models.Model):
    controlnumber = models.TextField(primary_key=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    location = models.PointField(blank=True, null=True)
    respondent = models.CharField(max_length=50, blank=True, null=True)
    date_interview = models.DateField()
    enumerator = models.CharField(max_length=50, blank=True, null=True)
    editor = models.CharField(max_length=50, blank=True, null=True)
    year_construct = models.IntegerField(blank=True, null=True)
    estimated_cost = models.IntegerField(blank=True, null=True)
    number_bedrooms = models.SmallIntegerField(blank=True, null=True)
    number_storey = models.SmallIntegerField(blank=True, null=True)
    access_electricity = models.BooleanField(blank=True, null=True)
    access_internet = models.BooleanField(blank=True, null=True)
    medical_treatment = models.TextField(blank=True, null=True)
    access_water_supply = models.BooleanField(blank=True, null=True)
    potable = models.BooleanField(blank=True, null=True)
    floods_occur = models.BooleanField(blank=True, null=True)
    year_flooded = models.IntegerField(blank=True, null=True)
    experience_evacuate = models.BooleanField()
    year_evacuate = models.IntegerField(blank=True, null=True)
    access_health_medical_facility = models.BooleanField(blank=True, null=True)
    access_telecommuniciation = models.BooleanField(blank=True, null=True)
    access_drill_simulation = models.BooleanField(blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()
    barangay = models.ForeignKey(Barangays, models.DO_NOTHING, blank=True, null=True)
    evacuationareas = models.ForeignKey(Evacuationareas, models.DO_NOTHING, blank=True, null=True)
    householdbuildingtypes = models.ForeignKey(Householdbuildingtypes, models.DO_NOTHING, blank=True, null=True)
    householdroofmaterials = models.ForeignKey(Householdroofmaterials, models.DO_NOTHING, blank=True, null=True)
    householdtenuralstatus = models.ForeignKey(Householdtenuralstatus, models.DO_NOTHING, blank=True, null=True)
    householdwallmaterials = models.ForeignKey(Buildingwallmaterials, models.DO_NOTHING, blank=True, null=True)
    householdwatertenuralstatus = models.ForeignKey(Householdwatertenuralstatus, models.DO_NOTHING, blank=True, null=True)
    municipality = models.ForeignKey(Municipalities, models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    waterlevelsystems = models.ForeignKey(Waterlevelsystems, models.DO_NOTHING, blank=True, null=True)
    purok_fk = models.ForeignKey(Purok, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'household_households'
        
# PointSenior

class MaterializedPointSenior(models.Model):
    household_number = models.TextField(primary_key=True)
    flood_id = models.CharField(max_length=50, blank=True, null=True)
    munname = models.CharField(max_length=255, blank=True, null=True)
    brgyname = models.CharField(max_length=255, blank=True, null=True)
    purok = models.CharField(max_length=255, blank=True, null=True)
    brgycode = models.CharField(max_length=255, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    lat = models.CharField(max_length=50, blank=True, null=True)
    long = models.CharField(max_length=50, blank=True, null=True)
    person = models.BigIntegerField(blank=True, null=True)
    elderly_male = models.BigIntegerField(blank=True, null=True)
    elderly_female = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'point_senior'