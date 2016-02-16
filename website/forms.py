from django import forms
from .models import *

class CountryForm(forms.ModelForm):
    continent = forms.ModelChoiceField(label="Kontynent", queryset=Continent.objects.all())
        
    class Meta:
        model = Country
        fields = ('name', 'about', 'photo', 'continent',)

class CityForm(forms.ModelForm):
    country = forms.ModelChoiceField(label="Kraj", queryset=Country.objects.all())
        
    class Meta:
        model = City
        fields = ('name', 'about', 'photo', 'country',)
