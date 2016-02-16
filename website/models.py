from __future__ import unicode_literals

from django.db import models

class Continent(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    about = models.TextField()
    photo = models.ImageField(upload_to='images/photos/')

    class Meta:
        verbose_name = 'Kontynent'
        verbose_name_plural = 'Kontynenty'

    def __unicode__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True)
    about = models.TextField(default='Country', max_length=1000)
    photo = models.ImageField(upload_to='images/photos', blank=True)
    continent = models.ForeignKey('Continent')

    class Meta:
        verbose_name = 'Kraj'
        verbose_name_plural = 'Kraje'

    def __unicode__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True)
    about = models.TextField(default='City', max_length=1000)
    photo = models.ImageField(upload_to='images/photos', blank=True)
    country = models.ForeignKey('Country')

    class Meta:
        verbose_name = 'Miasto'
        verbose_name_plural = 'Miasta'

    def __unicode__(self):
        return self.name

