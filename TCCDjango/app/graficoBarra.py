import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly as pl 
from .CreateDataFrame import CreateDataFrame as BuildDf
from .DataFrameUtil import DataFrameUtil as dfUtil


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
        dfFinal = BuildDf.DataFrameTotais()
        dfFinal.query('TotalCases > 1000000', inplace=True)
        fig = go.Figure()  
        for contestant, group in dfFinal.groupby("Continent"):
            fig.add_trace(go.Bar(x=group["Name"], y=group["TotalCases"], name=contestant,
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
        dfFinal = BuildDf.DataFrameTotais()
        dfFinal.query('TotalCases > 1000000', inplace=True)
        fig = px.bar(dfFinal, x='Name', y='TotalRecovered', title='Relação Casos x Recuperados por país',
             hover_data=['TotalCases', 'TotalRecovered'], color='TotalCases',
             labels={'TotalCases':'Total de Casos', 'Name' : 'País', 'TotalRecovered' : 'Total Recuperado', 'Abr' : '1º Abril'}, height=400)
        #fig.write_html("app/graph.html")
        #pl.offline.plot(fig, filename = 'app/graph.html')
        return fig

    def PlotGraficoBarraCalorPorcentagem():
        dfFinal = BuildDf.DataFrameTotais()
        dfFinal.query('TotalCases > 1000000', inplace=True)
        perceCasos = dfUtil.RetPorcentagemCasosPopulacao(dfFinal) #((dfFinal['TotalCases'] / dfFinal['Population']) *100)
        perceMortes = dfUtil.RetPorcentagemMortesPopulacao(dfFinal) #((dfFinal['TotalDeaths'] / dfFinal['Population']) *100)
        perceCurados = dfUtil.RetPorcentagemRecuperadosPopulacao(dfFinal) #((dfFinal['TotalRecovered'] / dfFinal['Population']) *100)
        fig = px.bar(dfFinal, x='Name', y='TotalRecovered', title='Porcentagem de Curados x Mortos',
             hover_data=['TotalCases', 'TotalRecovered'], color=perceMortes,
             labels={'TotalCases':'Total de Casos', 'Name' : 'País', 'TotalRecovered' : 'Total Recuperado', 'Abr' : '1º Abril', 'Continent' : 'Região',
                    'Population' : 'População', 'color' : '% Mortos'}, height=400)
        #fig.write_html("app/graph.html")
        #pl.offline.plot(fig, filename = 'app/graph.html')
        return fig

    def PlotGraficoBarPorcentagemCurados():
        dfFinal = BuildDf.DataFrameTotais()
        dfFinal.sort_values(['TotalRecovered'], inplace=True)
        perce = dfUtil.RetPorcentagemRecuperadoCasos(dfFinal) #((dfFinal['TotalRecovered'] / dfFinal['TotalCases']) *100)
        # print(perce.to_string())

        fig = px.bar(dfFinal, x='Name', y=perce, color='Continent', labels={'y':'% de Curados','TotalCases':'Total de Casos','Name' : 'País', 'TotalRecovered' : 'Total Recuperado'},
             hover_data=['Name'],   title='Porcentagem de Curados x Total de Casos')
        #fig.write_html("app/graph.html")
        #pl.offline.plot(fig, filename = 'app/graph.html')
        return fig

    def PlotGraficoBarPorcentagemMortos():
        dfFinal = BuildDf.DataFrameTotais()
        dfFinal.sort_values(['TotalDeaths'], inplace=True)
        perce = dfUtil.RetPorcentagemMortosCasos(dfFinal) #((dfFinal['TotalDeaths'] / dfFinal['TotalCases']) *100)
        # print(perce.to_string())

        fig = px.bar(dfFinal, x='Name', y=perce, color='Continent', labels={'y':'% de Mortos','TotalCases':'Total de Casos','Name' : 'País', 'TotalDeaths' : 'Total Mortes'},
             hover_data=['Name'], title='Porcentagem de Mortes x Total de Casos')
        #fig.write_html("app/graph.html")
        #pl.offline.plot(fig, filename = 'app/graph.html')
        return fig

    def PlotGraficoBarPorcentagemCasos(): #NÃO USAR, FICOU ESTRANHO EIXO Y
        dfFinal = BuildDf.DataFrameTotais()
        dfFinal.sort_values(['TotalCases'], inplace=True)
        perce = dfUtil.RetPorcentagemCasosPopulacao(dfFinal) #((dfFinal['TotalCases'] / dfFinal['Population']) *100)
        # print(perce.to_string())

        fig = px.bar(dfFinal, x='Continent', y=perce, color='Continent', labels={'y':'% de Casos','TotalCases':'Total de Casos','Continent' : 'Região', 'Population' : 'População'},
             hover_data=['Name'],   title='Porcentagem de Casos x População')
        #fig.write_html("app/graph.html")
        #pl.offline.plot(fig, filename = 'app/graph.html')
        return fig 