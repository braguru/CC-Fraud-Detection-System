from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, TemplateView

# Create your views here.

class Landing_Page(TemplateView):
    template_name = "core/landing_page.html"
    
    
class About(TemplateView):
    template_name = "core/About.html"
    