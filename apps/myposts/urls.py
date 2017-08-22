from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^all.json$', views.all_json, name='all_json'),
    url(r'^all.html$', views.all_html, name='all_html'),
    url(r'^find$', views.find, name='find'),
    url(r'^create$', views.create, name='create'),
]