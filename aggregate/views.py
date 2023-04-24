from aggregate.models import AggregatedFamiliesandPopulation
from datetime import datetime
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
import openpyxl
from openpyxl.styles import Font, PatternFill
from openpyxl.utils import get_column_letter
from io import StringIO




def index(request):
    
    return render(request,'aggregate/index.html')

def exportFamilyandPopulation(request):
    aggregated = AggregatedFamiliesandPopulation.objects.all()
    workbook = openpyxl.Workbook()
    worksheet = workbook.active

    #for col_num in range(1, 4):
        #column_letter = get_column_letter(col_num)
        #worksheet.column_dimensions[column_letter].width = 15

    bold_font = Font(bold=True)
    fill = PatternFill(start_color='FFCC00', end_color='FFCC00', fill_type='solid')
    headers = ['Municipality','Barangay','No. of Households','Individuals (M)','Individuals (F)','Infant 0-11months (M)',
               'Infant 0-11months (F)','Children 1-17y/o (M)','Children 1-17y/o (F)','Adult 18-59y/o (M)','Adult 18-59y/o (F)',
               'Elderly 60y/o above (M)','Elderly 60y/o above (F)','IP (M)','IP (F)']
    
    for col_num, header_title in enumerate(headers, 1):
        cell = worksheet.cell(row=1, column=col_num, value=header_title)
        cell.font = bold_font
        cell.fill = fill
        column_letter = get_column_letter(col_num)
        worksheet.column_dimensions[column_letter].width = 16

    for data in aggregated:
        worksheet.append([data.munname,data.brgyname,data.households,data.male,data.female,data.male_infant,
                        data.female_infant,data.male_children,data.female_children,data.male_adult,
                        data.female_adult,data.male_elderly,data.female_elderly,data.ip_male,data.ip_female])
        
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=FamiliesandPopulation.xlsx'
    workbook.save(response)
    return response

    
'''def print_aggregate(request):
    queryset = AggregatedFamiliesandPopulation.objects.all()
    output = StringIO()
    for obj in queryset:
        output.write(str(obj) + "\n")

    response = HttpResponse(output.getvalue(), content_type="text/plain")
    response["Content-Disposition"] = "attachment; filename=FamiliesandPopulatio.txt"
    return response'''

 


