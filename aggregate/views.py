from aggregate.models import AggregatedFamiliesandPopulation
from datetime import datetime
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from openpyxl.styles import Font, PatternFill
from openpyxl.utils import get_column_letter
from io import StringIO
from openpyxl import Workbook
from django.db import models
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.db.models import Sum

def index(request): 
    return render(request,'aggregate/index.html')



def exportFamilyandPopulation(request):
    try:
        user = request.user

        # Check if user belongs to the "municipality" group or is an admin
        if user.groups.filter(name='municipality').exists() or user.is_superuser:
            if user.is_superuser:
                aggregated = AggregatedFamiliesandPopulation.objects.all()
            else:
                user_location = user.userlocation
                municipality = user_location.psgccode_mun
                aggregated = AggregatedFamiliesandPopulation.objects.filter(munname=municipality)

            workbook = Workbook()
            worksheet = workbook.active

            worksheet.print_options.fit_to_page = True
            worksheet.print_options.fit_to_width = 1

            bold_font = Font(bold=True)
            fill = PatternFill(start_color='FFCC00', end_color='FFCC00', fill_type='solid')
            headers = [
                'Municipality', 'Barangay', 'No. of Households', 'Individuals (M)', 'Individuals (F)',
                'Infant 0-11months (M)', 'Infant 0-11months (F)', 'Children 1-17y/o (M)', 'Children 1-17y/o (F)',
                'Adult 18-59y/o (M)', 'Adult 18-59y/o (F)', 'Elderly 60y/o above (M)', 'Elderly 60y/o above (F)',
                'IP (M)', 'IP (F)'
            ]

            for col_num, header_title in enumerate(headers, 1):
                cell = worksheet.cell(row=7, column=col_num, value=header_title)
                cell.font = bold_font
                cell.fill = fill
                column_letter = get_column_letter(col_num)
                worksheet.column_dimensions[column_letter].width = 18

            for data in aggregated:
                worksheet.append([
                    data.munname, data.brgyname, data.households, data.male, data.female, data.male_infant,
                    data.female_infant, data.male_children, data.female_children, data.male_adult,
                    data.female_adult, data.male_elderly, data.female_elderly, data.ip_male, data.ip_female
                ])

            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=FamiliesandPopulation.xlsx'
            workbook.save(response)
            return response

        else:
            return HttpResponse('You do not have permission to export data')

    except Exception as e:
        error_message = f'An error occurred: {str(e)}'
        return render(request, 'aggregate/error_template.html', {'error_message': error_message})


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
