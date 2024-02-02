from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from library.models import Municipalities, Barangays, Purok

@login_required
def municipality_list(request):
  if request.user.is_authenticated:
      if request.user.is_superuser or request.user.groups.filter(name='admin').exists():
        municipality = Municipalities.objects.all()
        return JsonResponse({'data': [{'psgccode': m.psgccode, 'munname': m.munname} for m in municipality]})
      else:
        user_mun = request.user.userlocation.psgccode_mun
        municipality = Municipalities.objects.filter(munname=user_mun)
        return JsonResponse({'data': [{'psgccode': m.psgccode, 'munname': m.munname} for m in municipality]})


@login_required
def barangay_list(request, municipality_id):
  barangays = Barangays.objects.filter(psgcmun_id=municipality_id)
  return JsonResponse({'data': [{'psgccode': b.psgccode, 'brgyname': b.brgyname} for b in barangays]})


@login_required
def purok_list(request, barangay_id):
  puroks = Purok.objects.filter(psgccode_brgy=barangay_id)
  return JsonResponse({'data': [{'purok_id': p.purok_id, 'purok_name': p.purok_name} for p in puroks]})