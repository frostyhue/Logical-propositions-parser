# The libraries that are used for the engine of the application.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from tool.classes.Interpreter import *
from tool.classes.SimplifiedTT import *
from django.views.generic import *
from tool.classes.TreeVisualizer import *
from django.shortcuts import *
import os

# Function used by the url file to redirect to the index's page.
def main(request):
    return render(request, 'Main.html')
