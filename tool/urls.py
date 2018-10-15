from django.conf.urls import *
from . import views
from tool.views import *


urlpatterns = [
    url(r'^$', ToolView.as_view(), name='tool'),
    url(r'tests/', views.tests, name='tests'),

]