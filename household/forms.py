from django import forms
from household.models import Households
from library.models import Municipalities, Barangays
from library.views import municipality_list

class HouseholdForm(forms.ModelForm):
    class Meta:
        model = Households

        fields = ['municipality', 'barangay']

    def __init__(self, *args, **kwargs):
        super(HouseholdForm, self).__init__(*args, **kwargs)

        # when there is instance key, select the default value
        # Municipality always loaded for initial data, because Municipality is on the first level 
        try:
          self.initial['municipality'] = kwargs['instance'].municipality.psgccode
        except:
          pass
        municipality_list = [('', '---------')] + [(i.psgccode, i.munname) for i in Municipalities.objects.all()]

        # Barangay is on the child level, it will be loaded when user click the parent level
        try:
          self.initial['barangays'] = kwargs['instance'].barangays.psgccode
          barangay_init_form = [(i.psgccode, i.brgyname) for i in Barangays.objects.filter(
                municipality=kwargs['instance'].municipality
            )]
        except:
            barangay_init_form = [('', '---------')]

        
        # Override the form, add onchange attribute to call the ajax function
        self.fields['municipality'].widget = forms.Select(
            attrs={
                'id': 'id_municipality',
                'onchange': 'getBarangay(this.value)',
                'style': 'width:200px'
            },
            choices=municipality_list,
        )

class HouseholdSearchForm(forms.ModelForm):
    class Meta:
        model = Households
        fields = ['controlnumber', 'purok','respondent','municipality','barangay',
            'date_interview','enumerator','editor','year_construct','estimated_cost',
            'number_bedrooms','number_storey','access_electricity']

    def __init__(self, *args, **kwargs):
        super(HouseholdSearchForm, self).__init__(*args, **kwargs)

        # when there is instance key, select the default value
        # Municipality always loaded for initial data, because Municipality is on the first level 
        try:
          self.initial['municipality'] = kwargs['instance'].municipality.psgccode
        except:
          pass
        municipality_list = [('', '---------')] + [(i.psgccode, i.munname) for i in Municipalities.objects.all()]

        # Barangay is on the child level, it will be loaded when user click the parent level
        try:
          self.initial['barangays'] = kwargs['instance'].barangays.psgccode
          barangay_init_form = [(i.psgccode, i.brgyname) for i in Barangays.objects.filter(
                municipality=kwargs['instance'].municipality
            )]
        except:
            barangay_init_form = [('', '---------')]

        
        # Override the form, add onchange attribute to call the ajax function
        self.fields['municipality'].widget = forms.Select(
            attrs={
                'id': 'id_municipality',
                'onchange': 'getBarangay(this.value)',
                'style': 'width:200px'
            },
            choices=municipality_list,
        )