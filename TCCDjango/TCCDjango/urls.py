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
    path('GraficoLTBarMensal/', views.GraficoLTBarMensal, name='GraficoLTBarMensal'),
    path('GraficoLTScatterMensal/', views.GraficoLTScatterMensal, name='GraficoLTScatterMensal'),
    path('GraficoLTBarQuinzenal/', views.GraficoLTBarQuinzenal, name='GraficoLTBarQuinzenal'),
    path('GraficoLTScatterQuinzenal/', views.GraficoLTScatterQuinzenal, name='GraficoLTScatterQuinzenal'), 
    path('GrafigoBarraMortePais/', views.GrafigoBarraMortePais, name='GrafigoBarraMortePais'), 
    path('GrafigoBarraCasosPais/', views.GrafigoBarraCasosPais, name='GrafigoBarraCasosPais'),
    path('GrafigoBarraCalor/', views.GrafigoBarraCalor, name='GrafigoBarraCalor'),
    path('GraficoBarraCalorPorcentagem/', views.GraficoBarraCalorPorcentagem, name='GraficoBarraCalorPorcentagem'),
    path('GrafigoScatterCasos/', views.GrafigoScatterCasos, name='GrafigoScatterCasos'),
    path('GraficoScatterPorcentagemCasos/', views.GraficoScatterPorcentagemCasos, name='GraficoScatterPorcentagemCasos'),
    path('GraficoScatterPorcentagemCasosMortes/', views.GraficoScatterPorcentagemCasosMortes, name='GraficoScatterPorcentagemCasosMortes'),
    path('GrafigoBarraPorcentagemCurados/', views.GrafigoBarraPorcentagemCurados, name='GrafigoBarraPorcentagemCurados'), 
    path('GraficoBarPorcentagemMortos/', views.GraficoBarPorcentagemMortos, name='GraficoBarPorcentagemMortos'),
    path('GrafigoBarraPorcentagemCasos/', views.GrafigoBarraPorcentagemCasos, name='GrafigoBarraPorcentagemCasos'),
    #path('GrafigoBarraPorcentagemCuradosRegiao/', views.GrafigoBarraPorcentagemCuradosRegiao, name='GrafigoBarraPorcentagemCuradosRegiao'), 
    #path('GraficoBarPorcentagemMortosRegiao/', views.GraficoBarPorcentagemMortosRegiao, name='GraficoBarPorcentagemMortosRegiao'),
]