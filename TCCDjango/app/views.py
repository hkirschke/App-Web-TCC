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
 

def GraficoLTBarMensal(request):
  assert isinstance(request, HttpRequest)
  fig = graphLT.PlotGraphTimeLineBarMensal()
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

def GraficoLTScatterMensal(request):
  assert isinstance(request, HttpRequest)
  fig = graphLT.PlotGraphTimeLineScatterMensal()
  pl.offline.plot(fig, filename = 'app/graph.html')
  return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def GraficoLTScatterMensalPorcentagemCasosPopulacao(request):
  assert isinstance(request, HttpRequest)
  fig = graphLT.PlotGraphTimeLineScatterMensalPorcentagemCasosPopulacao()
  pl.offline.plot(fig, filename = 'app/graph.html')
  return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def GraficoLTBarQuinzenal(request):
  assert isinstance(request, HttpRequest)
  fig = graphLT.PlotGraphTimeLineBarQuinzenal()
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

def GraficoLTScatterQuinzenal(request):
  assert isinstance(request, HttpRequest)
  fig = graphLT.PlotGraphTimeLineScatterQuinzenal()
  pl.offline.plot(fig, filename = 'app/graph.html')
  return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def GrafigoBarraMortePais24h(request):
  assert isinstance(request, HttpRequest)
  fig = graphBar.PlotGrafigoBarraMortePais24h()
  pl.offline.plot(fig, filename = 'app/graph.html')
  return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def GrafigoBarraCasosPais24h(request):
  assert isinstance(request, HttpRequest)
  fig = graphBar.PlotGrafigoBarraCasosPais24h()
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
  fig = graphBar.PlotGrafigoBarraCasosPais()
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
  fig = graphBar.PlotGraficoBarraCalor()
  pl.offline.plot(fig, filename = 'app/graph.html')
  return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def GraficoBarraCalorPorcentagem(request):
  assert isinstance(request, HttpRequest)
  fig = graphBar.PlotGraficoBarraCalorPorcentagem()
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
  fig = grapScatter.PlotGraficoScatterCasos()
  pl.offline.plot(fig, filename = 'app/graph.html')
  return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

#def GrafigoScatterCasos(request):
#  assert isinstance(request, HttpRequest)
#  fig = grapScatter.PlotGraficoScatterCasos()
#  pl.offline.plot(fig, filename = 'app/graph.html')
#  return render(
#        request,
#        'app/index.html',
#        {
#            'title':'Home Page',
#            'year':datetime.now().year,
#        }
#    )


def GraficoScatterPorcentagemCasos(request):
  assert isinstance(request, HttpRequest)
  fig = grapScatter.PlotGraficoScatterPorcentagemCasos()
  pl.offline.plot(fig, filename = 'app/graph.html')
  return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def GraficoScatterPorcentagemCasosMortes(request):
  assert isinstance(request, HttpRequest)
  fig = grapScatter.PlotGraficoScatterPorcentagemCasosMortes()
  pl.offline.plot(fig, filename = 'app/graph.html')
  return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def GraficoBarPorcentagemMortosCasos(request):
  assert isinstance(request, HttpRequest)
  fig = graphBar.PlotGraficoBarPorcentagemMortosCasos()
  pl.offline.plot(fig, filename = 'app/graph.html')
  return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def GraficoBarPorcentagemMortosPopulacao(request):
  assert isinstance(request, HttpRequest)
  fig = graphBar.PlotGraficoBarPorcentagemMortosPopulacao()
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
  fig = graphBar.PlotGraficoBarPorcentagemCurados()
  pl.offline.plot(fig, filename = 'app/graph.html')
  return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def GrafigoBarraPorcentagemCuradosPopulacao(request):
  assert isinstance(request, HttpRequest)
  fig = graphBar.PlotGraficoBarPorcentagemCuradosPopulacao()
  pl.offline.plot(fig, filename = 'app/graph.html')
  return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def GrafigoBarraPorcentagemCasos(request):
  assert isinstance(request, HttpRequest)
  fig = graphBar.PlotGraficoBarPorcentagemCasos()
  pl.offline.plot(fig, filename = 'app/graph.html')
  return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )




#def GraficoBarPorcentagemMortosRegiao(request):
#  assert isinstance(request, HttpRequest)
#  fig = graphBar.PlotGraficoBarPorcentagemMortosRegiao()
#  pl.offline.plot(fig, filename = 'app/graph.html')
#  return render(
#        request,
#        'app/index.html',
#        {
#            'title':'Home Page',
#            'year':datetime.now().year,
#        }
#    )

#def GrafigoBarraPorcentagemCuradosRegiao(request):
#  assert isinstance(request, HttpRequest)
#  fig = graphBar.PlotGraficoBarPorcentagemCuradosRegiao()
#  pl.offline.plot(fig, filename = 'app/graph.html')
#  return render(
#        request,
#        'app/index.html',
#        {
#            'title':'Home Page',
#            'year':datetime.now().year,
#        }
#    )

