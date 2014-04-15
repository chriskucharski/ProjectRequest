from django import forms

SYSTEM_CHOICES = (
    ('default','Please choose'),
    ('asset_reporting','Asset Reporting'),
    ('client_reporting','Client Reporting'),
    ('gips','GIPS'),
    ('report_rendering','Report Rendering'),
    ('sant','SANT'),
    ('web','Web'),
    ('general_technology','General Technology'),
)

class ContactForm(forms.Form):
    error_css_class = 'inplaceError'
    required_css_class = 'roundify'
            
    requester = forms.CharField(max_length=100)
    department = forms.CharField(max_length=55)
    subject = forms.CharField(max_length=100)
    description = forms.CharField(max_length=255)
    business_sponsor = forms.CharField(max_length=100)
    requested_delivery_date = forms.DateField()
    system = forms.ChoiceField(choices=SYSTEM_CHOICES)