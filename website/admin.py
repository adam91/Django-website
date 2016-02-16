from django.contrib import admin
from .models import *

admin.site.register(Continent)

class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'continent',]
admin.site.register(Country, CountryAdmin)
admin.site.register(City)
