from rest_framework import serializers
from .models import Households, Demographies

class DemographySerializer(serializers.ModelSerializer):

  class Meta:
    model = Demographies
    fields = ['controlnumber','lastname','firstname','middlename','extension','nuclear_family','relationshiptohead',
            'gender','birthdate', 'marital_status', 'ethnicity_by_blood', 'member_ip', 'informal_settler', 'religion',
            'person_with_special_needs', 'type_of_disability', 'is_ofw', 'residence', 'nutritional_status', 'nutritional_status_recorded',
            'currently_attending_school', 'current_grade_level_attending', 'highest_eductional_attainment', 'course_completed_vocational',
            'can_read_and_write', 'primary_occupation', 'monthly_income', 'sss_member', 'gsis_member', 'philhealth_member', 
            'dependent_of_philhealth_member', 'owner']

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
  evacuationareas = serializers.StringRelatedField()

  demographies_set = DemographySerializer(many=True, read_only=True)


  class Meta:
    model = Households
    fields = ['controlnumber','latitude','longitude','respondent','municipality', 'barangay', 'purok', 'location','householdbuildingtypes',
            'householdtenuralstatus','year_construct','estimated_cost', 'number_bedrooms', 'number_storey',
            'access_electricity', 'householdroofmaterials','householdwallmaterials','medical_treatment',
            'access_water_supply','potable','householdwatertenuralstatus','waterlevelsystems','floods_occur',
            'year_flooded','experience_evacuate','year_evacuate','evacuationareas','access_health_medical_facility',
            'access_telecommuniciation','access_drill_simulation','image','enumerator','editor','demographies_set']
    # fields = '__all__'
