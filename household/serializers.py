from rest_framework import serializers
from .models import Availprograms, Hhlivelihoods, Households, Demographies

class DemographySerializer(serializers.ModelSerializer):

  relationshiptohead = serializers.StringRelatedField()
  gender = serializers.StringRelatedField()
  marital_status = serializers.StringRelatedField()
  type_of_disability = serializers.StringRelatedField()
  nutritional_status = serializers.StringRelatedField()
  current_grade_level_attending = serializers.StringRelatedField()
  highest_eductional_attainment = serializers.StringRelatedField()
  course_completed_vocational = serializers.StringRelatedField()
  monthly_income = serializers.StringRelatedField()

  class Meta:
    model = Demographies
    fields = ['id','controlnumber','lastname','firstname','middlename','extension','nuclear_family','relationshiptohead',
            'gender','birthdate', 'marital_status', 'ethnicity_by_blood', 'member_ip', 'informal_settler', 'religion',
            'person_with_special_needs', 'type_of_disability', 'is_ofw', 'residence', 'nutritional_status', 'nutritional_status_recorded',
            'currently_attending_school', 'current_grade_level_attending', 'highest_eductional_attainment', 'course_completed_vocational',
            'can_read_and_write', 'primary_occupation', 'monthly_income', 'sss_member', 'gsis_member', 'philhealth_member', 
            'dependent_of_philhealth_member', 'owner']

class AvailedprogramsSerializer(serializers.ModelSerializer):

  type_of_program = serializers.StringRelatedField()
  
  class Meta:
    model = Availprograms
    fields = ['id','type_of_program','name_of_program','number_of_beneficiaries','program_implementor']

class LivelihoodSerializer(serializers.ModelSerializer):
  
  livelihood = serializers.StringRelatedField()
  livelihood_tenural_status = serializers.StringRelatedField()

  class Meta:
    model = Hhlivelihoods
    fields = ['id','livelihood','market_value','products','area','livelihood_tenural_status','with_insurance']

class HouseholdSerializer(serializers.ModelSerializer):

  municipality = serializers.StringRelatedField()
  barangay = serializers.StringRelatedField()
  householdbuildingtypes = serializers.StringRelatedField()
  householdtenuralstatus = serializers.StringRelatedField()
  householdroofmaterials = serializers.StringRelatedField()
  householdwallmaterials = serializers.StringRelatedField()
  medical_treatment = serializers.StringRelatedField()
  householdwatertenuralstatus = serializers.StringRelatedField()
  waterlevelsystems = serializers.StringRelatedField()
  evacuationareas = serializers.StringRelatedField()

  demographies_set = DemographySerializer(many=True, read_only=True)
  availprograms_set = AvailedprogramsSerializer(many=True, read_only=True)
  hhlivelihoods_set = LivelihoodSerializer(many=True, read_only=True)


  class Meta:
    model = Households
    fields = ['controlnumber','latitude','longitude','respondent','municipality', 'barangay', 'location','householdbuildingtypes',
            'householdtenuralstatus','year_construct','estimated_cost', 'number_bedrooms', 'number_storey',
            'access_electricity', 'householdroofmaterials','householdwallmaterials','medical_treatment',
            'access_water_supply','potable','householdwatertenuralstatus','waterlevelsystems','floods_occur',
            'year_flooded','experience_evacuate','year_evacuate','evacuationareas','access_health_medical_facility',
            'access_telecommuniciation','access_drill_simulation','image','enumerator','editor','demographies_set','availprograms_set','hhlivelihoods_set']
    # fields = '__all__'
