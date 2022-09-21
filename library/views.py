from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from library.models import Municipalities, Barangays

@login_required
def municipality_list(request):
  municipality = Municipalities.objects.all()
  return JsonResponse({'data': [{'psgccode': m.psgccode, 'munname': m.munname} for m in municipality]})


@login_required
def barangay_list(request,municipality_id):
  barangays = Barangays.objects.filter(psgcmun=municipality_id)
  return JsonResponse({'data': [{'psgccode': b.psgccode, 'brgyname': b.brgyname} for b in barangays]})