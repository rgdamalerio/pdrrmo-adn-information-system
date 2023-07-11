from aggregate.models import AggregatedFamiliesandPopulation
from datetime import datetime
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import openpyxl
import xlsxwriter
from django.views.generic import View
from openpyxl.styles import Font, PatternFill
from openpyxl.utils import get_column_letter
from io import StringIO
from openpyxl import load_workbook
from django.db import models
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.db.models import Sum

def index(request): 
    return render(request,'aggregate/index.html')

def exportFamilyandPopulation(request):
    user = request.user

    # Check if user belongs to the "municipality" group or is an admin
    if user.groups.filter(name='municipality').exists() or user.is_superuser:
        if user.is_superuser:
            aggregated = AggregatedFamiliesandPopulation.objects.all()
        else:
            user_location = user.userlocation
            municipality = user_location.psgccode_mun
            aggregated = AggregatedFamiliesandPopulation.objects.filter(munname=municipality)

        # Create a new workbook
        workbook = xlsxwriter.Workbook('FamiliesandPopulation.xlsx')
        worksheet = workbook.add_worksheet()

        bold_format = workbook.add_format({'bold': True})
        fill_format = workbook.add_format({'bg_color': 'yellow'})

        headers = ['Municipality', 'Barangay', 'No. of Households', 'Individuals (M)', 'Individuals (F)',
                   'Infant 0-11months (M)', 'Infant 0-11months (F)', 'Children 1-17y/o (M)', 'Children 1-17y/o (F)',
                   'Adult 18-59y/o (M)', 'Adult 18-59y/o (F)', 'Elderly 60y/o above (M)', 'Elderly 60y/o above (F)',
                   'IP (M)', 'IP (F)']

        # Write headers with formatting
        for col_num, header_title in enumerate(headers):
            worksheet.write(6, col_num, header_title, bold_format)
            worksheet.set_column(col_num, col_num, 18)

        # Write data
        row = 7
        for data in aggregated:
            worksheet.write(row, 0, data.munname)
            worksheet.write(row, 1, data.brgyname)
            worksheet.write(row, 2, data.households)
            worksheet.write(row, 3, data.male)
            worksheet.write(row, 4, data.female)
            worksheet.write(row, 5, data.male_infant)
            worksheet.write(row, 6, data.female_infant)
            worksheet.write(row, 7, data.male_children)
            worksheet.write(row, 8, data.female_children)
            worksheet.write(row, 9, data.male_adult)
            worksheet.write(row, 10, data.female_adult)
            worksheet.write(row, 11, data.male_elderly)
            worksheet.write(row, 12, data.female_elderly)
            worksheet.write(row, 13, data.ip_male)
            worksheet.write(row, 14, data.ip_female)
            row += 1

        workbook.close()

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=FamiliesandPopulation.xlsx'
        with open('FamiliesandPopulation.xlsx', 'rb') as file:
            response.write(file.read())
        return response

    else:
        return HttpResponse('You do not have permission to export data')



def chart_view(request):
    return render(request, 'aggregate/population_chart.html')

def get_data(request, *args, **kwargs):
    qresult = AggregatedFamiliesandPopulation.objects.values('munname').annotate(
        total_households=Sum('households'),
        total_male=Sum('male'),
        total_female=Sum('female'),
        total_male_infant=Sum('male_infant'),
        total_female_infant=Sum('female_infant'),
        total_male_children=Sum('male_children'),
        total_female_children=Sum('female_children'),
        total_male_adult=Sum('male_adult'),
        total_female_adult=Sum('female_adult'),
        total_male_elderly=Sum('male_elderly'),
        total_female_elderly=Sum('female_elderly'),
        total_ip_male=Sum('ip_male'),
        total_ip_female=Sum('ip_female')
    )
    data = list(qresult)
    #data = serializers.serialize('json', ser_data)
    return HttpResponse(data, content_type='application/json')