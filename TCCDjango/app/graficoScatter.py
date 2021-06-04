import pandas as pd
#import plotly.graph_objects as go
import plotly.express as px
#import plotly.io as pio
import plotly as pl 
from .CreateDataFrame import CreateDataFrame as BuildDf
from .DataFrameUtil import DataFrameUtil as dfUtil


class GraficoScatter():   
    def PlotGraficoScatterCasos():
        dfFinal = BuildDf.DataFrameTotais()
        fig = px.scatter(dfFinal, x="TotalCases", y="TotalRecovered", color="Name", title='Relação Recuperados x Casos',
                 size='TotalCases', hover_data=['TotalRecovered', 'Name','Continent'], size_max=80,
                 labels={'TotalCases':'Total de Casos', 'Name' : 'País', 'TotalRecovered' : 'Total Recuperado', 'Abr' : '1º Abril','Continent' : 'Região'})
        return fig

    def PlotGraficoScatterPorcentagemCasos():
        dfFinal = BuildDf.DataFrameTotais()
        perce = dfUtil.RetPorcentagemCasosPopulacao(dfFinal)  #((dfFinal['TotalCases'] / dfFinal['Population']) *100)
        fig = px.scatter(dfFinal, x="Population", y=perce, color="Name", title='Porcentagem de infectados da população',
                 size='TotalCases', hover_data=['TotalRecovered', 'Population', 'Name','Continent'], size_max=80,
                 labels={'TotalCases':'Total de Casos', 'Name' : 'País', 'TotalRecovered' : 'Total Recuperado', 'Abr' : '1º Abril', 'Continent' : 'Região', 'Population' : 'População',
                         'y' : '% de Casos'})
        return fig

    def PlotGraficoScatterPorcentagemCasosMortes():
        dfFinal = BuildDf.DataFrameTotais()
        perceCasos = dfUtil.RetPorcentagemCasosPopulacao(dfFinal)  #((dfFinal['TotalCases'] / dfFinal['Population']) *100)
        perceMortes = dfUtil.RetPorcentagemMortesPopulacao(dfFinal)  #((dfFinal['TotalDeaths'] / dfFinal['Population']) *100)
        fig = px.scatter(dfFinal, x=perceMortes, y=perceCasos, color="Continent", 
                 size='TotalCases', hover_data=['TotalRecovered', 'Population', 'Name','Continent'], size_max=80,
                 labels={'TotalCases':'Total de Casos', 'Name' : 'País', 'TotalRecovered' : 'Total Recuperado', 'Abr' : '1º Abril', 'Continent' : 'Região', 'Population' : 'População',
                         'y' : '% de Casos', 'x' : '% de Mortos'}, title="Porcentagem de Casos x Mortos da população")
        return fig