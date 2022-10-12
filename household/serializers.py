from rest_framework import serializers
from .models import Households

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


  class Meta:
    model = Households
    fields = ['controlnumber','latitude','longitude','respondent','municipality', 'barangay', 'purok', 'location','householdbuildingtypes',
            'householdtenuralstatus','year_construct','estimated_cost', 'number_bedrooms', 'number_storey',
            'access_electricity', 'householdroofmaterials','householdwallmaterials','medical_treatment',
            'access_water_supply','potable','householdwatertenuralstatus','waterlevelsystems','floods_occur',
            'year_flooded','experience_evacuate','year_evacuate','evacuationareas','access_health_medical_facility',
            'access_telecommuniciation','access_drill_simulation','image','enumerator','editor','demographies_set']
    # fields = '__all__'
