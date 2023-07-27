from .models import FloodReport
from django.shortcuts import render
from django.urls import reverse
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from django.apps import apps

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

class ViewPDF(View):
    def get_queryset(self, model_name):
        try:
            model_class = apps.get_model('reports', model_name)
            return model_class.objects.all()
        except LookupError:
            return None

    def get(self, request, model, *args, **kwargs):
        qs = self.get_queryset(model)
        
        if not qs:
            return HttpResponse("Invalid model name.")

        # PDF generation logic here, using the 'qs' queryset
        sum_male = 0
        sum_female = 0
        for data in qs:
            sum_male += data.num_male 
            sum_female += data.num_female
        context = {'flood_data': qs, 'total_male': sum_male, 'total_female': sum_female}
        pdf = render_to_pdf('reports/pdf_template.html', context)

        # Create the download URL here using the current view's URL and adding a query parameter
        download_url = reverse('pdf_download', args=[model]) + '?download=true'
        filename = f'{model}.pdf' 
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        response['X-Accel-Redirect'] = download_url
        return response
    
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