from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .persons import persons
from household.models import Demographies,Households,Barangays,Municipalities 
from .serializer import PersonSerializer,HouseholdSerializer,MunicipalitiesSerializer,BarangaySerializer,HouseholdInfoSerializer,AggregatedHouseholdSerializer,HouseholdPerMunSerializer, FamliyPerMunSerializer,BrgyInfoSerializer,TotalReportSerializer,FloodHazardInfoSerializer,FloodReportPerBarangaySerializer,OverAllFloodReportSerializer,PointSeniorSerializer
from base.models import AdnFlood,Barangay,Householdinfo,Householdpermun,Familiespermun,Brgyinfo,AdnTotalReport,FloodHazardInfo,FloodReportPerBarangay,OverAllFloodReport,MaterializedPointSenior
from aggregate.models import AggregatedFamiliesandPopulation
from django.core.serializers import serialize
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage,Page,PageNotAnInteger

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/persons/',
        '/api/persons/create/',

        '/api/persons/upload/',
    ]
    return Response(routes)

@api_view(['GET'])
def getPersons(request):
    persons = Demographies.objects.all()[:100]
    serializer = PersonSerializer(persons, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getHousehold(request):
    households = Householdinfo.objects.all()[:100]
    serializer = HouseholdInfoSerializer(households,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAggregaredHousehold(request):
    query = request.query_params.get('keyword')
    
    if query == None:
        query = ''

    aggregated = AggregatedFamiliesandPopulation.objects.all()

    page = request.query_params.get('page')
    paginator = Paginator(aggregated, 20)

    try:
        aggregated = paginator.page(page)
    except PageNotAnInteger:
        aggregated = paginator.page(1)
    except EmptyPage:
        aggregated = paginator.page(paginator.num_pages)

    if page == None:
        page = 1

    page = int(page)


    serializer = AggregatedHouseholdSerializer(aggregated,many=True)

    return Response({'aggregate':serializer.data, 'page':page, 'pages':paginator.num_pages})

@api_view(['GET'])
def getFlood(request):
    flood = Barangay.objects.all()
    serialized_data = serialize("geojson",flood,geometry_field="polygon",fields=("gid","barangayna","brgypsgc","brgyarea","provname","munname","provpsgc","regname","regpsgc","munpsgc","brgypopn","popden","munarea", "munpopn", "avehhsize", "land_sus", "area_ha","arm_confli", "mining_are", "flooded", "geom"))
    return HttpResponse(serialized_data, content_type="application/json")


@api_view(['GET'])
def getPerson(request, pk):
    person =None
    for i in persons:
        if i['_id'] == pk:
            person = i
            break
    return Response(person)

@api_view(['GET'])
def getMunicipal(request):
    municipalities = Municipalities.objects.all()
    serializer = MunicipalitiesSerializer(municipalities,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBarangay(request):
    barangays = Barangays.objects.all().order_by('psgccode')
    serializer = BarangaySerializer(barangays,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBrgy(request, pk):
    householdsBrgy =  Householdinfo.objects.filter(brgycode=pk)
    serializer = HouseholdInfoSerializer(householdsBrgy,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getHouseholdInfo(request,pk):
    householdInfo =  Householdinfo.objects.filter(brgycode=pk)
    serializer = HouseholdInfoSerializer(householdInfo,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getHouseholdPerMun(request):
    householdpermun =  Householdpermun.objects.all()
    serializer = HouseholdPerMunSerializer(householdpermun,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getFamilyPerMun(request):
    familypermun = Familiespermun.objects.all()
    serializer =FamliyPerMunSerializer(familypermun,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBrgyInfo(request,pk):
    info =  Brgyinfo.objects.filter(psgccode=pk)
    serializer = BrgyInfoSerializer(info,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getTotalReport(request):
    adnTotal = AdnTotalReport.objects.all()
    serializer = TotalReportSerializer(adnTotal,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getFloodHazardInfo(request,pk):
    floodInfo = FloodHazardInfo.objects.filter(brgycode=pk)
    serializer = FloodHazardInfoSerializer(floodInfo,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getFloodReportPerBarangay(request,pk):
    floodInfo = FloodReportPerBarangay.objects.filter(brgycode=pk)
    serializer = FloodReportPerBarangaySerializer(floodInfo,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getOverAllFloodReport(request):
    overallfloodreport = OverAllFloodReport.objects.all()
    serializer = OverAllFloodReportSerializer(overallfloodreport,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getpointsenior(request,pk):
    pointsenior = MaterializedPointSenior.objects.filter(flood_id=pk)
    serializer = PointSeniorSerializer(pointsenior,many=True)
    return Response(serializer.data)
