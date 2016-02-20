from django.conf.urls import url
from django.contrib import admin
from . import views
import os.path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

media_dir = os.path.join(os.path.dirname(__file__),'media')

urlpatterns = [
    url(r'^media/(.*)$','django.views.static.serve',{'document_root': media_dir}),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.all_continents_start_site, name='all_continents_start_site'),
    url(r'^continents$', views.all_continents, name='all_continents'),
    url(r'^countries$', views.all_countries, name='all_countries'),
    url(r'^cities$', views.all_cities, name='all_cities'),
    url(r'^continent/(?P<pk>[%&+ \w]+)/$', views.continent_detail, name='continent_detail'),
    url(r'^country/(?P<pk>[0-9]+)/$', views.country_detail, name='country_detail'),
    url(r'^city/(?P<pk>[0-9]+)/$', views.city_detail, name='city_detail'),
    url(r'^country/new/$', views.country_new, name='country_new'),
    url(r'^city/new/$', views.city_new, name='city_new'),
    url(r'^country/(?P<pk>[0-9]+)/edit/$', views.country_edit, name='country_edit'),
    url(r'^city/(?P<pk>[0-9]+)/edit/$', views.city_edit, name='city_edit'),
    url(r'^country/(?P<pk>[0-9]+)/delete/$', views.delete_country, name='delete_country'),
    url(r'^city/(?P<pk>[0-9]+)/delete/$', views.delete_city, name='delete_city'),
    url(r'^login/$', views.login),
    url(r'^authorized/$', views.auth_view),
    url(r'^logout/$', views.logout),
    url(r'^loggedin/$', views.loggedin),
    url(r'^invalid/$', views.invalid_login),
    url(r'^register/$', views.register_user, name='register_user'),
    url(r'^register_success/$', views.register_success, name='register_success'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^about/$', TemplateView.as_view(template_name='website/about.html')),
]
