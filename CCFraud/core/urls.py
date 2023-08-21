from django.contrib import admin
from django.urls import path
from . import views
from . views import Landing_Page, About

urlpatterns = [
    path('', Landing_Page.as_view(), name="landing_page"),
    path('about/', About.as_view(), name="about" ),
    path('upload/', views.upload, name="upload" ),
    path('predict/', views.predict, name="predict" ),
    path('result/', views.result, name="result" ),
    
]