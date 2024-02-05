from rest_framework import serializers
from django.contrib.auth.models import User
from household.models import Demographies,Households,Municipalities,Barangays
from base.models import Householdinfo,Householdpermun,Familiespermun,Brgyinfo,AdnTotalReport,FloodHazardInfo,FloodReportPerBarangay,OverAllFloodReport,MaterializedPointSenior
from aggregate.models import AggregatedFamiliesandPopulation


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demographies
        fields = '__all__'

class HouseholdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Households
        fields = ['longitude','latitude','location','barangay']

class AggregatedHouseholdSerializer(serializers.ModelSerializer):
    class Meta:
        model = AggregatedFamiliesandPopulation
        fields = '__all__'

class MunicipalitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipalities
        fields = '__all__'

class BarangaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Barangays
        fields = '__all__'

class HouseholdInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Householdinfo
        fields = '__all__'

class HouseholdPerMunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Householdpermun
        fields = '__all__'

class FamliyPerMunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familiespermun
        fields = '__all__'

class BrgyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brgyinfo
        fields = '__all__'

class TotalReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdnTotalReport
        fields = '__all__'


class FloodHazardInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FloodHazardInfo
        fields = '__all__'

class FloodReportPerBarangaySerializer(serializers.ModelSerializer):
    class Meta:
        model = FloodReportPerBarangay
        fields = '__all__'
        

class OverAllFloodReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverAllFloodReport
        fields = '__all__'

class PointSeniorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterializedPointSenior
        fields = '__all__'