from django import forms 
from .models import productRegistrationModel

class productRegisterForm(forms.Form):
    user = forms.CharField(max_length=200)
    first_last_name = forms.CharField(max_length=200)
    prudoct_name = forms.CharField(max_length=200)
    prudoct_code = forms.CharField(max_length=200)




class SearchBoxForm(forms.Form):
    search_text = forms.CharField(max_length=100)
