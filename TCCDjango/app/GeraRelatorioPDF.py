import pandas as pd
#import plotly.graph_objects as go
import plotly.express as px
#import plotly.io as pio
import plotly as pl 
from .CreateDataFrame import CreateDataFrame as BuildDf
from .graficoLinhaTempo import GraficoLT as graphLT
from .graficoBarra import GraficoBarra as graphBar
from .graficoScatter import GraficoScatter as grapScatter


class GeraRelatorio(): 
    #def __init__(self):
    #    self.dfTimeSeriesCases = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
        
    #    self.dfTimeSeriesRecover = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
        
    #    self.dfTimeSeriesDeath = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
        
    #    url = 'https://covid19.who.int/WHO-COVID-19-global-table-data.csv'
    #    self.dfRegioes = pd.read_csv(url) 

    def GeraRelatorioPDF():
        fig = graphLT.PlotGraphTimeLineScatter()
        html = pl.offline.plot(fig, include_plotlyjs=False, output_type='div')
        pl.offline.plot(fig, filename = 'app/graph.html')