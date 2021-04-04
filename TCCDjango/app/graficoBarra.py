import pandas as pd
#import plotly.graph_objects as go
import plotly.express as px
#import plotly.io as pio
import plotly as pl 
from .CreateDataFrame import CreateDataFrame as BuildDf


class GraficoBarra(): 
    #def __init__(self):
    #    self.dfTimeSeriesCases = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
        
    #    self.dfTimeSeriesRecover = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
        
    #    self.dfTimeSeriesDeath = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
        
    #    url = 'https://covid19.who.int/WHO-COVID-19-global-table-data.csv'
    #    self.dfRegioes = pd.read_csv(url)

    def PlotGrafigoBarraMortePais():
       dfFinal = BuildDf.DataFrameLast24h()
       #dfFinal.sort_values(['Mortos'], inplace=True)
        
       fig = go.Figure()  
       for contestant, group in dfFinal.groupby("WHO Region"):
         fig.add_trace(go.Bar(x=group["Name"], y=group["Deaths - newly reported in last 24 hours"], name=contestant,
         hovertemplate="Continentes=%s<br>País=%%{x}<br>Mortes D-1=%%{y}<extra></extra>"% contestant))
        # fig.update_layout(legend_title_text = "WHO Region")
       fig.update_xaxes(title_text="Países")
       fig.update_yaxes(title_text="Mortes D-1")
       #fig.write_html("app/graph.html")
       #pl.offline.plot(fig, filename = 'app/graph.html')
       #fig.show()
       return fig

    def PlotGrafigoBarraCasosPais():
        # GRÁFICO 1.2
        dfFinal = BuildDf.DataFrameCasos()
        fig = go.Figure()  
        for contestant, group in dfFinal.groupby("WHO Region"):
            fig.add_trace(go.Bar(x=group["Name"], y=group["Cases - cumulative total"], name=contestant,
              hovertemplate="Continentes=%s<br>País=%%{x}<br>Total Casos=%%{y}<extra></extra>"% contestant))
        # fig.update_layout(legend_title_text = "WHO Region")
        fig.update_xaxes(title_text="Países")
        fig.update_yaxes(title_text="Total Casos")
        #fig.show()
        #fig.write_html("app/graph.html")
        #pl.offline.plot(fig, filename = 'app/graph.html')
        #pl.offline.plot(fig, include_plotlyjs=False, output_type='div')
        return fig

    def PlotGraficoBarraCalor():
        dfFinal = BuildDf.DataFrameMensal()
        px.scatter(dfFinal, x="Mortos", y="Casos", animation_frame="Mes", animation_group="País",
               size="Casos", color="Regiao", hover_name="País",
               log_x=True, size_max=80, range_x=[1000,1000000], range_y=[10000,40000000])
        #fig.write_html("app/graph.html")
        #pl.offline.plot(fig, filename = 'app/graph.html')
        return fig

    def PlotGraficoBarPorcentagemCurados():
        dfFinal = BuildDf.DataFrameCasos()
        perce = ((dfFinal['TotalRecovered'] / dfFinal['TotalCases']) *100)
        # print(perce.to_string())

        fig = px.bar(dfFinal, x='Name', y=perce, color='Continent', labels={'y':'% de Curados','TotalCases':'Total de Casos','Name' : 'País', 'TotalRecovered' : 'Total Recuperado'},
             hover_data=['Name'],   title='Porcentagem de curados x Total de casos')
        #fig.write_html("app/graph.html")
        #pl.offline.plot(fig, filename = 'app/graph.html')
        return fig

    def PlotGraficoScatterCasos():

        fig = px.scatter(dfFinal, x="TotalCases", y="TotalRecovered", color="Name",
                 size='TotalCases', hover_data=['TotalRecovered'],
                 labels={'TotalCases':'Total de Casos', 'Name' : 'País', 'TotalRecovered' : 'Total Recuperado', 'Mar' : '1º Março'})
        #fig.write_html("app/graph.html")
        #pl.offline.plot(fig, filename = 'app/graph.html')
        return fig