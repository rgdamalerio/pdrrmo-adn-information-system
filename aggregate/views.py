
from datetime import datetime
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse




# Create your views here.


def index(request):
    
    return render(request,'aggregate/index.html')

# def index(response):
#     return HttpResponse("hello world")
    #return HttpResponse()

# def some(request):
#     return HTTPResponse("hello world")




# Create your views here.
#@staff_member_required
# def generatePDF(request, id):
#     buffer = io.BytesIO()
#     x = canvas.Canvas(buffer)
#     x.drawString(100, 100, "Let's generate this pdf file.")
#     x.showPage()
#     x.save()
#     buffer.seek(0)
#     return FileResponse(buffer, as_attachment=True, filename='attempt1.pdf')


# def export_pdf(request):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename=Report'+str(datetime.now())+'.pdf'
    