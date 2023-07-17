from .models import FloodReport
from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

#Opens up page as PDF
class ViewPDF(View):
	def get(self, request, *args, **kwargs):
		qs = FloodReport.objects.all()
		
		flood_report = list(qs)
		sum_male = 0
		sum_female = 0
		for data in flood_report:
			sum_male += data.num_male 
			sum_female += data.num_female
		context = {'flood_data': flood_report, 'total_male': sum_male,'total_female': sum_male}
		pdf = render_to_pdf('reports/pdf_template.html',context)
		return HttpResponse(pdf, content_type='application/pdf')


#Automaticly downloads to PDF file
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		qs = FloodReport.objects.all()
		
		flood_report = list(qs)
		sum_male = 0
		sum_female = 0
		for data in flood_report:
			sum_male += data.num_male 
			sum_female += data.num_female
		context = {'flood_data': flood_report, 'total_male': sum_male,'total_female': sum_male}
		pdf = render_to_pdf('reports/pdf_template.html',context)
		response = HttpResponse(pdf, content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename="AffectedFamiliesandPopulation.pdf"'
		return response


def index(request):
	context = {}
	return render(request, 'app/index.html', context)