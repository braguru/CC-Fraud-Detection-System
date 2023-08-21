from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse

# Create your views here.

class Landing_Page(TemplateView):
    template_name = "core/landing_page.html"
    
    
class About(TemplateView):
    template_name = "core/About.html"
    
def upload(request):

    return render(request, 'core/upload.html')

def predict(request):
    return render(request, 'core/prediction.html')

def result(request):
    return render(request, 'core/result.html')