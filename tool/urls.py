from django.conf.urls import *
from . import views
from tool.views import *


urlpatterns = [
    url(r'^$', views.tool, name='index'),
    url(r'tests/$', views.tests, name='tests'),
    url(r'convert/$', views.convert, name='convert'),
]