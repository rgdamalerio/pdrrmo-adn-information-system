# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class AggregateFamiliesandpopulation(models.Model):
    fp_id = models.BigAutoField(primary_key=True)
    num_of_individuals_m = models.IntegerField()
    num_of_individuals_f = models.IntegerField()
    num_of_infant_m = models.IntegerField()
    num_of_infant_f = models.IntegerField()
    num_of_children_m = models.IntegerField()
    num_of_children_f = models.IntegerField()
    num_of_adult_m = models.IntegerField()
    num_of_adult_f = models.IntegerField()
    num_of_elderly_m = models.IntegerField()
    num_of_elderly_f = models.IntegerField()
    num_of_pwd_m = models.IntegerField()
    num_of_pwd_f = models.IntegerField()
    num_of_ip_m = models.IntegerField()
    num_of_ip_f = models.IntegerField()
    barangay = models.ForeignKey('LibraryBarangays', models.DO_NOTHING, blank=True, null=True)
    municipality = models.ForeignKey('LibraryMunicipalities', models.DO_NOTHING)
    num_of_family = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'aggregate_familiesandpopulation'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class Caraga(models.Model):
    gid = models.AutoField(primary_key=True)
    id = models.IntegerField(blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    geom = models.MultiPolygonField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caraga'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EvacuatonCenter(models.Model):
    gid = models.AutoField(primary_key=True)
    landmark = models.CharField(max_length=50, blank=True, null=True)
    lndmk_desc = models.CharField(max_length=50, blank=True, null=True)
    mun_name = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    lndmk_clas = models.CharField(max_length=10, blank=True, null=True)
    load_limit = models.FloatField(blank=True, null=True)
    max_height = models.FloatField(blank=True, null=True)
    remarks = models.CharField(max_length=50, blank=True, null=True)
    geom = models.PointField(srid=0, dim=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evacuaton_center'


class Flood(models.Model):
    gid = models.AutoField(primary_key=True)
    floodsusc = models.CharField(max_length=3, blank=True, null=True)
    susceptibi = models.CharField(max_length=33, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flood'


class HouseholdAvailprograms(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_of_program = models.CharField(max_length=150)
    number_of_beneficiaries = models.SmallIntegerField()
    program_implementor = models.CharField(max_length=150)
    created_at = models.DateField()
    updated_at = models.DateField()
    controlnumber = models.ForeignKey('HouseholdHouseholds', models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    type_of_program = models.ForeignKey('LibraryTypeofprograms', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'household_availprograms'


class HouseholdDemographies(models.Model):
    id = models.BigAutoField(primary_key=True)
    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50, blank=True, null=True)
    extension = models.CharField(max_length=15, blank=True, null=True)
    birthdate = models.DateField()
    ethnicity_by_blood = models.CharField(max_length=150, blank=True, null=True)
    member_ip = models.BooleanField()
    informal_settler = models.BooleanField()
    religion = models.CharField(max_length=150)
    person_with_special_needs = models.BooleanField()
    is_ofw = models.BooleanField()
    residence = models.BooleanField()
    nutritional_status_recorded = models.DateField(blank=True, null=True)
    currently_attending_school = models.BooleanField()
    can_read_and_write = models.BooleanField()
    primary_occupation = models.CharField(max_length=255, blank=True, null=True)
    sss_member = models.BooleanField()
    gsis_member = models.BooleanField()
    philhealth_member = models.BooleanField()
    dependent_of_philhealth_member = models.BooleanField()
    created_at = models.DateField()
    updated_at = models.DateField()
    controlnumber = models.ForeignKey('HouseholdHouseholds', models.DO_NOTHING, blank=True, null=True)
    course_completed_vocational = models.ForeignKey('LibraryTrackstrandcourses', models.DO_NOTHING, blank=True, null=True)
    current_grade_level_attending = models.ForeignKey('LibraryGradelevels', models.DO_NOTHING, blank=True, null=True)
    gender = models.ForeignKey('LibraryGenders', models.DO_NOTHING, blank=True, null=True)
    highest_eductional_attainment = models.ForeignKey('LibraryGradelevels', models.DO_NOTHING, blank=True, null=True)
    marital_status = models.ForeignKey('LibraryMaritalstatus', models.DO_NOTHING, blank=True, null=True)
    monthly_income = models.ForeignKey('LibraryMonthlyincomes', models.DO_NOTHING, blank=True, null=True)
    nuclear_family = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    nutritional_status = models.ForeignKey('LibraryNutritionalstatus', models.DO_NOTHING, blank=True, null=True)
    relationshiptohead = models.ForeignKey('LibraryRelationshiptoheads', models.DO_NOTHING, blank=True, null=True)
    type_of_disability = models.ForeignKey('LibraryDisabilities', models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'household_demographies'


class HouseholdHhlivelihoods(models.Model):
    id = models.BigAutoField(primary_key=True)
    market_value = models.IntegerField()
    products = models.CharField(max_length=255)
    with_insurance = models.BooleanField()
    created_at = models.DateField()
    updated_at = models.DateField()
    controlnumber = models.ForeignKey('HouseholdHouseholds', models.DO_NOTHING, blank=True, null=True)
    livelihood = models.ForeignKey('LibraryLivelihoods', models.DO_NOTHING, blank=True, null=True)
    livelihood_tenural_status = models.ForeignKey('LibraryLivelihoodtenuralstatus', models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    area = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'household_hhlivelihoods'


class HouseholdHouseholds(models.Model):
    controlnumber = models.TextField(primary_key=True)
    purok = models.CharField(max_length=25, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    location = models.PointField(blank=True, null=True)
    respondent = models.CharField(max_length=50)
    date_interview = models.DateField()
    enumerator = models.CharField(max_length=50)
    editor = models.CharField(max_length=50)
    year_construct = models.IntegerField()
    estimated_cost = models.IntegerField()
    number_bedrooms = models.SmallIntegerField()
    number_storey = models.SmallIntegerField()
    access_electricity = models.BooleanField()
    access_internet = models.BooleanField()
    medical_treatment = models.TextField(blank=True, null=True)
    access_water_supply = models.BooleanField()
    potable = models.BooleanField()
    floods_occur = models.BooleanField()
    year_flooded = models.IntegerField(blank=True, null=True)
    experience_evacuate = models.BooleanField()
    year_evacuate = models.IntegerField(blank=True, null=True)
    access_health_medical_facility = models.BooleanField()
    access_telecommuniciation = models.BooleanField()
    access_drill_simulation = models.BooleanField()
    image = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateField()
    updated_at = models.DateField()
    barangay = models.ForeignKey('LibraryBarangays', models.DO_NOTHING, blank=True, null=True)
    evacuationareas = models.ForeignKey('LibraryEvacuationareas', models.DO_NOTHING, blank=True, null=True)
    householdbuildingtypes = models.ForeignKey('LibraryHouseholdbuildingtypes', models.DO_NOTHING, blank=True, null=True)
    householdroofmaterials = models.ForeignKey('LibraryHouseholdroofmaterials', models.DO_NOTHING, blank=True, null=True)
    householdtenuralstatus = models.ForeignKey('LibraryHouseholdtenuralstatus', models.DO_NOTHING, blank=True, null=True)
    householdwallmaterials = models.ForeignKey('LibraryBuildingwallmaterials', models.DO_NOTHING, blank=True, null=True)
    householdwatertenuralstatus = models.ForeignKey('LibraryHouseholdwatertenuralstatus', models.DO_NOTHING, blank=True, null=True)
    municipality = models.ForeignKey('LibraryMunicipalities', models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    waterlevelsystems = models.ForeignKey('LibraryWaterlevelsystems', models.DO_NOTHING, blank=True, null=True)
    purok_id = models.ForeignKey('LibraryPurok', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'household_households'


class Layer(models.Model):
    topology = models.OneToOneField('Topology', models.DO_NOTHING, primary_key=True)
    layer_id = models.IntegerField()
    schema_name = models.CharField(max_length=-1)
    table_name = models.CharField(max_length=-1)
    feature_column = models.CharField(max_length=-1)
    feature_type = models.IntegerField()
    level = models.IntegerField()
    child_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layer'
        unique_together = (('topology', 'layer_id'), ('schema_name', 'table_name', 'feature_column'),)


class LibraryBarangays(models.Model):
    psgccode = models.CharField(primary_key=True, max_length=255)
    brgyname = models.CharField(max_length=255)
    created_at = models.DateField()
    updated_at = models.DateField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)
    psgcmun = models.ForeignKey('LibraryMunicipalities', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'library_barangays'


class LibraryBuildingroofmaterials(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.TextField(unique=True)
    created_at = models.DateField()
    updated_at = models.DateField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'library_buildingroofmaterials'


class LibraryBuildingstatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.TextField(unique=True)
    created_at = models.DateField()
    updated_at = models.DateField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'library_buildingstatus'


class LibraryBuildingtypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.TextField(unique=True)
    created_at = models.DateField()
    updated_at = models.DateField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'library_buildingtypes'


class LibraryBuildinguses(models.Model):
    id = models.BigAutoField(primary_key=True)
    use = models.CharField(unique=True, max_length=255)
    created_at = models.DateField()
    updated_at = models.DateField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'library_buildinguses'


class LibraryBuildingwallmaterials(models.Model):
    id = models.BigAutoField(primary_key=True)
    material = models.TextField(unique=True)
    created_at = models.DateField()
    updated_at = models.DateField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'library_buildingwallmaterials'


class LibraryDisabilities(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(unique=True, max_length=255)
    created_at = models.DateField()
    updated_at = models.DateField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'library_disabilities'


class LibraryEvacuationareas(models.Model):
    id = models.BigAutoField(primary_key=True)
    evacuation_area = models.CharField(unique=True, max_length=255)
    created_at = models.DateField()
    updated_at = models.DateField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'library_evacuationareas'


class LibraryFarmingtechs(models.Model):
    id = models.BigAutoField(primary_key=True)
    technology = models.CharField(unique=True, max_length=125)
    created_at = models.DateField()
    updated_at = models.DateField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'library_farmingtechs'


class LibraryGenders(models.Model):
    id = models.BigAutoField(primary_key=True)
    gender = models.CharField(unique=True, max_length=50)
    created_at = models.DateField()
    updated_at = models.DateField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'library_genders'


class LibraryGradelevels(models.Model):
    code = models.IntegerField(primary_key=True)
    description = models.CharField(unique=True, max_length=255)
    created_at = models.DateField()
    updated_at = models.DateField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'library_gradelevels'


class LibraryHouseholdbuildingtypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.TextField(unique=True)
    created_at = models.DateField()
    updated_at = models.DateField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'library_householdbuildingtypes'


class LibraryHouseholdroofmaterials(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.TextField(unique=True)
    created_at = models.DateField()
    updated_at = models.DateField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'library_householdroofmaterials'


class LibraryHouseholdtenuralstatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.TextField(unique=True)
    created_at = models.DateField()
    updated_at = models.DateField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'library_householdtenuralstatus'


class LibraryHouseholdwallmaterials(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.TextField(unique=True)
    created_at = models.DateField()
    updated_at = models.DateField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'library_householdwallmaterials'


class LibraryHouseholdwatertenuralstatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(unique=True, max_length=50)
    created_at = models.DateField()
    updated_at = models.DateField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'library_householdwatertenuralstatus'


class LibraryLivelihoods(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.TextField(unique=True)
    created_at = models.DateField()
    updated_at = models.DateField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'library_livelihoods'


class LibraryLivelihoodtenuralstatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(unique=True, max_length=250)
    created_at = models.DateField()
    updated_at = models.DateField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'library_livelihoodtenuralstatus'


class LibraryMaritalstatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(unique=True, max_length=25)
    created_at = models.DateField()
    updated_at = models.DateField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'library_maritalstatus'


class LibraryMonthlyincomes(models.Model):
    id = models.BigAutoField(primary_key=True)
    income = models.CharField(unique=True, max_length=25)
    created_at = models.DateField()
    updated_at = models.DateField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'library_monthlyincomes'


class LibraryMunicipalities(models.Model):
    psgccode = models.CharField(primary_key=True, max_length=255)
    munname = models.CharField(unique=True, max_length=255)
    created_at = models.DateField()
    updated_at = models.DateField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'library_municipalities'


class LibraryNutritionalstatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(unique=True, max_length=25)
    created_at = models.DateField()
    updated_at = models.DateField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'library_nutritionalstatus'


class LibraryPurok(models.Model):
    purok_id = models.BigAutoField(primary_key=True)
    purok_name = models.CharField(max_length=255)
    psgccode_brgy = models.ForeignKey(LibraryBarangays, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'library_purok'


class LibraryRelationshiptoheads(models.Model):
    id = models.BigAutoField(primary_key=True)
    relationship = models.CharField(unique=True, max_length=50)
    created_at = models.DateField()
    updated_at = models.DateField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'library_relationshiptoheads'


class LibraryTrackstrandcourses(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(unique=True, max_length=250)
    created_at = models.DateField()
    updated_at = models.DateField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'library_trackstrandcourses'


class LibraryTypeofprograms(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(unique=True, max_length=250)
    created_at = models.DateField()
    updated_at = models.DateField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'library_typeofprograms'


class LibraryWaterlevelsystems(models.Model):
    id = models.BigAutoField(primary_key=True)
    level = models.CharField(unique=True, max_length=50)
    description = models.TextField(unique=True)
    created_at = models.DateField()
    updated_at = models.DateField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'library_waterlevelsystems'


class MajorRivers(models.Model):
    gid = models.AutoField(primary_key=True)
    id = models.SmallIntegerField(blank=True, null=True)
    riv_name = models.CharField(max_length=23, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    length = models.SmallIntegerField(blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'major_rivers'


class Ril(models.Model):
    gid = models.AutoField(primary_key=True)
    lndslidesu = models.CharField(max_length=50, blank=True, null=True)
    susceptibi = models.CharField(max_length=45, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ril'


class Topology(models.Model):
    name = models.CharField(unique=True, max_length=-1)
    srid = models.IntegerField()
    precision = models.FloatField()
    hasz = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'topology'


class UsersUserprofile(models.Model):
    id = models.BigAutoField(primary_key=True)
    contact_number = models.CharField(max_length=17)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_userprofile'
