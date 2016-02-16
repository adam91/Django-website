from django.shortcuts import render, get_object_or_404, redirect

from .models import *
from .forms import CountryForm, CityForm

def all_continents(request):
    continents = Continent.objects.all().order_by('name')
    return render(request, 'website/all_continents.html', {'continents' : continents})

def all_countries(request):
    countries = Country.objects.all().order_by('name')
    return render(request, 'website/all_countries.html', {'countries' : countries})

def all_cities(request):
    cities = City.objects.all().order_by('name')
    return render(request, 'website/all_cities.html', {'cities' : cities})

def continent_detail(request, pk):
    continent = get_object_or_404(Continent, pk=pk)
    return render(request, 'website/continent_detail.html', {'continent': continent})

def country_detail(request, pk):
    country = get_object_or_404(Country, pk=pk)
    return render(request, 'website/country_detail.html', {'country': country})

def city_detail(request, pk):
    city = get_object_or_404(City, pk=pk)
    return render(request, 'website/city_detail.html', {'city': city})

def country_new(request):
    if request.method == "POST":
        form = CountryForm(request.POST, request.FILES)
        if form.is_valid():
            country = form.save(commit=False)
            country.save()
            form.save_m2m()
            return redirect('website.views.country_detail', pk=country.pk)
    else:
        form = CountryForm()
    return render(request, 'website/country_new.html', {'form': form})

def city_new(request):
    if request.method == "POST":
        form = CityForm(request.POST, request.FILES)
        if form.is_valid():
            city = form.save(commit=False)
            city.author = request.user
            city.save()
            form.save_m2m()
            return redirect('website.views.city_detail', pk=city.pk)
    else:
        form = CityForm()
    return render(request, 'website/city_new.html', {'form': form})


def country_edit(request, pk):
    country = get_object_or_404(Country, pk=pk)
    if request.method == "POST":
        form = CountryForm(request.POST, request.FILES, instance=country)
        if form.is_valid():
            country = form.save(commit=False)
            country.save()
            form.save_m2m()
            return redirect('website.views.country_detail', pk=country.pk)
    else:
        form = CountryForm(instance=country)
    return render(request, 'website/country_new.html', {'form': form})


def city_edit(request, pk):
    city = get_object_or_404(City, pk=pk)
    if request.method == "POST":
        form = CityForm(request.POST, request.FILES, instance=city)
        if form.is_valid():
            city = form.save(commit=False)
            city.save()
            form.save_m2m()
            return redirect('website.views.city_detail', pk=city.pk)
    else:
        form = CityForm(instance=city)
    return render(request, 'website/city_new.html', {'form': form})

def delete_country(request, pk):
    country = get_object_or_404(Country, pk=pk)
    country.delete()
    countries = Country.objects.all().order_by('name')
    return render(request, 'website/all_countries.html', {'countries': countries})

def delete_city(request, pk):
    city = get_object_or_404(City, pk=pk)
    city.delete()
    cities = City.objects.all().order_by('name')
    return render(request, 'website/all_cities.html', {'cities': cities})
