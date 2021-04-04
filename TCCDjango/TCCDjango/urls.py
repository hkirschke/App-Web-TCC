"""
Definition of urls for TCCDjango.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('GraficoLTBar/', views.GraficoLTBar, name='GraficoLTBar'),
    path('GraficoLTScatter/', views.GraficoLTScatter, name='GraficoLTScatter'), 
    path('GrafigoBarraMortePais/', views.GrafigoBarraMortePais, name='GrafigoBarraMortePais'), 
    path('GrafigoBarraCasosPais/', views.GrafigoBarraCasosPais, name='GrafigoBarraCasosPais'), 
    path('GrafigoBarraPorcentagemCurados/', views.GrafigoBarraPorcentagemCurados, name='GrafigoBarraPorcentagemCurados'), 
    path('GrafigoBarraCalor/', views.GrafigoBarraCalor, name='GrafigoBarraCalor'),
    path('GrafigoScatterCasos/', views.GrafigoScatterCasos, name='GrafigoScatterCasos'),
]