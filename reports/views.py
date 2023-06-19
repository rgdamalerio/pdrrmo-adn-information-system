import json
import os
import matplotlib
matplotlib.use('agg') 
from docx import Document
from docx.shared import Inches
import matplotlib.pyplot as plt
from django.shortcuts import render
from reports.models import *
from django.db.models import Sum
from django.http import HttpResponse, JsonResponse
from django.core import serializers


def get_infant_counts(request):
    infant_counts = FloodReport.objects.values('barangay_name').annotate(
        total_infants=Sum('num_male_infant') + Sum('num_female_infant')
    )

    # Create a chart data list
    chart_data = []
    for result in infant_counts:
        barangay_name = result['barangay_name']
        total_infants = result['total_infants']
        chart_data.append({'Barangay': barangay_name, 'Total Infants': total_infants})

    # Generate the chart using matplotlib
    labels = [data['Barangay'] for data in chart_data]
    values = [data['Total Infants'] for data in chart_data]
    fig = plt.figure(figsize=(12, 6))
    plt.barh(labels, values)
    plt.xlabel('Total Infants')
    plt.ylabel('Barangay')
    plt.title('Infant Counts by Barangay (Flood Hazard)')
    plt.yticks(rotation=0, fontsize=7)

    # Set the download path
    file_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'document.docx')

    # Create a Word document
    document = Document()

    # Save the chart as an image
    chart_image_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'chart.png')
    plt.savefig(chart_image_path)

    # Insert the chart image into the Word document
    document.add_picture(chart_image_path, width=Inches(6), height=Inches(4.5))

    # Save the Word document
    document.save(file_path)

    # Return the document as an HTTP response
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = 'attachment; filename=document.docx'
        return response