import pandas as pd
#import plotly.graph_objects as go
import plotly.express as px
#import plotly.io as pio
import plotly as pl 
from .CreateDataFrame import CreateDataFrame as BuildDf
from .DataFrameUtil import DataFrameUtil as dfUtil


class GraficoScatter(): 
    #def __init__(self):
    #    self.dfTimeSeriesCases = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
        
    #    self.dfTimeSeriesRecover = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
        
    #    self.dfTimeSeriesDeath = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
        
    #    url = 'https://covid19.who.int/WHO-COVID-19-global-table-data.csv'
    #    self.dfRegioes = pd.read_csv(url) 

    def PlotGraficoScatterCasos():
        dfFinal = BuildDf.DataFrameTotais()
        fig = px.scatter(dfFinal, x="TotalCases", y="TotalRecovered", color="Name", title='Relação Recuperados x Casos',
                 size='TotalCases', hover_data=['TotalRecovered'], size_max=80,
                 labels={'TotalCases':'Total de Casos', 'Name' : 'País', 'TotalRecovered' : 'Total Recuperado', 'Abr' : '1º Abril'})
        #fig.write_html("app/graph.html")
        #pl.offline.plot(fig, filename = 'app/graph.html')
        return fig

    def PlotGraficoScatterPorcentagemCasos():
        dfFinal = BuildDf.DataFrameTotais()
        perce = dfUtil.RetPorcentagemCasosPopulacao(dfFinal)  #((dfFinal['TotalCases'] / dfFinal['Population']) *100)
        fig = px.scatter(dfFinal, x="Population", y=perce, color="Name", title='Porcentagem de infectados da população',
                 size='TotalCases', hover_data=['TotalRecovered', 'Population'], size_max=80,
                 labels={'TotalCases':'Total de Casos', 'Name' : 'País', 'TotalRecovered' : 'Total Recuperado', 'Abr' : '1º Abril', 'Continent' : 'Região', 'Population' : 'População',
                         'y' : '% de Casos'})
        #fig.write_html("app/graph.html")
        #pl.offline.plot(fig, filename = 'app/graph.html')
        return fig

    def PlotGraficoScatterPorcentagemCasosMortes():
        dfFinal = BuildDf.DataFrameTotais()
        perceCasos = dfUtil.RetPorcentagemCasosPopulacao(dfFinal)  #((dfFinal['TotalCases'] / dfFinal['Population']) *100)
        perceMortes = dfUtil.RetPorcentagemMortesPopulacao(dfFinal)  #((dfFinal['TotalDeaths'] / dfFinal['Population']) *100)
        fig = px.scatter(dfFinal, x=perceMortes, y=perceCasos, color="Name", 
                 size='TotalCases', hover_data=['TotalRecovered', 'Population'], size_max=80,
                 labels={'TotalCases':'Total de Casos', 'Name' : 'País', 'TotalRecovered' : 'Total Recuperado', 'Abr' : '1º Abril', 'Continent' : 'Região', 'Population' : 'População',
                         'y' : '% de Casos', 'x' : '% de Mortos'}, title="Porcentagem de Casos x Mortos da população")
        #fig.write_html("app/graph.html")
        #pl.offline.plot(fig, filename = 'app/graph.html')
        return fig