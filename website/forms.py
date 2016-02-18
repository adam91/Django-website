from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
