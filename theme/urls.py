from django.conf.urls import patterns, include, url
from .views import ThemeFormView, ThemeUpdateView

urlpatterns = patterns('',
    url(r'^add/$', ThemeFormView.as_view(), name='theme_add'),
    url(r'^(?P<pk>\d+)/$', ThemeUpdateView.as_view(), name='theme_update'),
)