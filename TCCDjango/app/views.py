"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .graficoLinhaTempo import GraficoLT as graphLT
from .graficoBarra import GraficoBarra as graphBar
from .graficoScatter import GraficoScatter as grapScatter
import plotly as pl 


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
 

def GraficoLTBar(request):
  assert isinstance(request, HttpRequest)
  fig = graphLT.PlotGraphTimeLineBar()
  fig.write_html("app/graph.html")
  pl.offline.plot(fig, filename = 'app/graph.html')
  return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def GraficoLTScatter(request):
  assert isinstance(request, HttpRequest)
  fig = graphLT.PlotGraphTimeLineScatter()
  pl.offline.plot(fig, filename = 'app/graph.html')
  return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def GrafigoBarraMortePais(request):
  assert isinstance(request, HttpRequest)
  fig = graphBar.PlotGrafigoBarraMortePais();
  pl.offline.plot(fig, filename = 'app/graph.html')
  return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def GrafigoBarraCasosPais(request):
  assert isinstance(request, HttpRequest)
  fig = graphBar.PlotGrafigoBarraCasosPais();
  pl.offline.plot(fig, filename = 'app/graph.html')
  return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def GrafigoBarraPorcentagemCurados(request):
  assert isinstance(request, HttpRequest)
  fig = graphBar.PlotGraficoBarPorcentagemCurados();
  pl.offline.plot(fig, filename = 'app/graph.html')
  return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )


def GrafigoBarraCalor(request):
  assert isinstance(request, HttpRequest)
  fig = graphBar.PlotGraficoBarraCalor();
  pl.offline.plot(fig, filename = 'app/graph.html')
  return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def GrafigoScatterCasos(request):
  assert isinstance(request, HttpRequest)
  fig = grapScatter.PlotGraficoScatterCasos();
  pl.offline.plot(fig, filename = 'app/graph.html')
  return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )
