from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.views import View
#from datetime import date
# from .models import Post

# Create your views here.

class StartingPageView(TemplateView):
    template_name = "converter/index.html"