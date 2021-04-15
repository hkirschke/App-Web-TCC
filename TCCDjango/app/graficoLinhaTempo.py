import pandas as pd
#import plotly.graph_objects as go
import plotly.express as px
#import plotly.io as pio
import plotly as pl 
from .CreateDataFrame import CreateDataFrame as BuildDf
from .DataFrameUtil import DataFrameUtil as dfUtil


class GraficoLT(): 
    #def __init__(self):
    #    self.dfTimeSeriesCases = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
        
    #    self.dfTimeSeriesRecover = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
        
    #    self.dfTimeSeriesDeath = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
        
    #    url = 'https://covid19.who.int/WHO-COVID-19-global-table-data.csv'
    #    self.dfRegioes = pd.read_csv(url)

    def PlotGraphTimeLineBarMensal():
       dfFinal = BuildDf.DataFrameMensal()
       fig = px.bar(dfFinal, x="Regiao", y="Mortos", color="Regiao",
          animation_frame="Mes", animation_group="País", range_y=[0,"Mortos"],
            hover_data=['País', 'Casos', 'Recuperado'],title='Linha de tempo Mortes')
       #fig.write_html("app/graph.html")
       #pl.offline.plot(fig, filename = 'app/graph.html')
       #pl.offline.plot(fig, include_plotlyjs=False, output_type='div')
       return fig

    def PlotGraphTimeLineScatterMensal():
        dfFinal = BuildDf.DataFrameMensal()
        fig = px.scatter(dfFinal, x="Mortos", y="Casos", animation_frame="Mes", animation_group="País",
               size="Casos", color="Regiao", hover_name="País",
               log_x=True, size_max=80, title='Linha de tempo Casos x Mortes')
        return fig

    def PlotGraphTimeLineScatterMensalPorcentagemCasosPopulacao():
        dfFinal = BuildDf.DataFrameMensal()
        perceCasos = dfUtil.RetPorcentagemCasosPopulacaoMensal(dfFinal)
        dfFinal['Casos'] = perceCasos
        perceMortos = dfUtil.RetPorcentagemMortosPopulacaoMensal(dfFinal)
        dfFinal['Mortos'] =perceMortos
        fig = px.scatter(dfFinal, x="Mortos", y="Casos", animation_frame="Mes", animation_group="País",
               size="Casos", color="Regiao", hover_name="País", size_max=40 , range_x=[0.01,0.3], range_y=[1,18]
               , title='Linha de tempo Casos x Mortes')
        return fig

    def PlotGraphTimeLineBarQuinzenal():
       dfFinal = BuildDf.DataFrameQuinzenal()
       dfFinal.sort_values(['Mortos'], inplace=True)
        
       fig = px.bar(dfFinal, x="Regiao", y="Mortos", color="Regiao",
          animation_frame="Mes", animation_group="País", range_y=[0,1200000],
            hover_data=['País', 'Casos', 'Recuperado'],title='Timeline Mortes por Região')
       #fig.write_html("app/graph.html")
       #pl.offline.plot(fig, filename = 'app/graph.html')
       #pl.offline.plot(fig, include_plotlyjs=False, output_type='div')
       return fig

    def PlotGraphTimeLineScatterQuinzenal():
        dfFinal = BuildDf.DataFrameQuinzenal()
        fig = px.scatter(dfFinal, x="Mortos", y="Casos", animation_frame="Mes", animation_group="País",
               size="Casos", color="Regiao", hover_name="País",
               log_x=True, size_max=80, range_x=[1000,1000000], range_y=[10000,35000000], title='Timeline Casos x Mortes por Região')
        return fig