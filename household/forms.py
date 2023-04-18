from email.policy import default
from django import forms
from household.models import Households
from library.models import Municipalities, Barangays, Purok
from library.views import municipality_list, barangay_list, purok_list

class HouseholdForm(forms.ModelForm):
    class Meta:
        model = Households

        fields = ['municipality','barangay','purok_fk']

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
            barangay_init_form = [(b.psgccode, b.brgyname) for b in Barangays.objects.filter(
                    municipality=kwargs['instance'].municipality
                )]
        except:
            pass
        barangay_init_form = [('', '---------')]
        
        try:
            self.initial['purok_fk'] = kwargs['instance'].purok_fk.purok_id
            purok_init_form = [(p.purok_id, p.purok_name) for p in Purok.objects.filter(
                    barangay=kwargs['instance'].barangay
                )]
        except:
            purok_init_form = [('', '---------')]
 
        
        # Override the form, add onchange attribute to call the ajax function
        self.fields['municipality'].widget = forms.Select(
            attrs={
                'id': 'id_municipality',
                'onchange': 'getBarangay(this.value)',
                'style': 'width:200px'
            },
            choices=municipality_list,
        )

        self.fields['barangay'].widget = forms.Select(
            attrs={
                'id': 'id_barangay',
                'onchange': 'getPurok(this.value)',
                'style': 'width:200px'
            },
            choices=barangay_init_form,
        )

        self.fields['purok_fk'].widget = forms.Select(
           attrs={
                'id': 'id_purok_id',
                'style': 'width:200px',
            
           },
            choices=purok_init_form,
        )


class HouseholdSearchForm(forms.ModelForm):
    class Meta:
        model = Households
        fields = ['controlnumber','respondent','municipality','barangay','purok_fk',
            'householdbuildingtypes','householdtenuralstatus','householdroofmaterials',
            'householdwallmaterials','householdwatertenuralstatus','waterlevelsystems','evacuationareas',
            'enumerator','editor','year_construct','estimated_cost',
            'number_bedrooms','number_storey','access_electricity',
            'access_internet','medical_treatment','access_water_supply',
            'potable','floods_occur','year_flooded','experience_evacuate',
            'year_evacuate','access_health_medical_facility','access_telecommuniciation',
            'access_drill_simulation']
 

    def __init__(self, *args, **kwargs):
        super(HouseholdSearchForm, self).__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


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

        try:
            self.initial['purok_fk'] = kwargs['instance'].purok_fk.purok_id
            purok_init_form = [(p.purok_id, p.purok_name) for p in Purok.objects.filter(
                    barangay=kwargs['instance'].barangay
                )]
        except:
            purok_init_form = [('', '---------')]
 
        
        # Override the form, add onchange attribute to call the ajax function
        self.fields['municipality'].widget = forms.Select(
            attrs={
                'id': 'id_municipality',
                'onchange': 'getBarangay(this.value)',
                'class': 'form-control'
            },
            choices=municipality_list,
        )
        self.fields['barangay'].widget = forms.Select(
            attrs={
                'id': 'id_barangay',
                'onchange': 'getPurok(this.value)',
                'class': 'form-control'
            },
            choices=barangay_init_form,
        )
        self.fields['purok_fk'].widget = forms.Select(
           attrs={
                'id': 'id_purok_id',
                'class': 'form-control',
            
            },
            choices=purok_init_form,
        )


        # Override the form, add onchange attribute to call the ajax function
        self.fields['controlnumber'].widget = forms.TextInput(
            attrs={
                'class': 'form-control'
            },
        )

        # Multiple select box for boolean field
        self.fields['access_electricity'].widget = forms.CheckboxSelectMultiple(attrs={"unchecked":""},choices=[(True, 'Yes'),(False, 'No')])
        self.fields['access_internet'].widget = forms.CheckboxSelectMultiple(attrs={"unchecked":""},choices=[(True, 'Yes'),(False, 'No')])
        self.fields['access_water_supply'].widget = forms.CheckboxSelectMultiple(attrs={"unchecked":""},choices=[(True, 'Yes'),(False, 'No')])
        self.fields['potable'].widget = forms.CheckboxSelectMultiple(attrs={"unchecked":""},choices=[(True, 'Yes'),(False, 'No')])
        self.fields['floods_occur'].widget = forms.CheckboxSelectMultiple(attrs={"unchecked":""},choices=[(True, 'Yes'),(False, 'No')])
        self.fields['experience_evacuate'].widget = forms.CheckboxSelectMultiple(attrs={"unchecked":""},choices=[(True, 'Yes'),(False, 'No')])
        self.fields['access_health_medical_facility'].widget = forms.CheckboxSelectMultiple(attrs={"unchecked":""},choices=[(True, 'Yes'),(False, 'No')])
        self.fields['access_telecommuniciation'].widget = forms.CheckboxSelectMultiple(attrs={"unchecked":""},choices=[(True, 'Yes'),(False, 'No')]) 
        self.fields['access_drill_simulation'].widget = forms.CheckboxSelectMultiple(attrs={"unchecked":""},choices=[(True, 'Yes'),(False, 'No')])

    class Media:
        js = (
            'js/chained-address-advance-search.js',
        )
    