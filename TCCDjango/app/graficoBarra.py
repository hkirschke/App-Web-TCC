import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly as pl 
from .CreateDataFrame import CreateDataFrame as BuildDf
from .DataFrameUtil import DataFrameUtil as dfUtil


class GraficoBarra():
    def PlotGrafigoBarraMortePais24h():
       dfFinal = BuildDf.DataFrameLast24h()
       dfFinal = dfFinal[(dfFinal["Mortes"] > 100)]
       dfFinal.sort_values(['Mortes'], inplace=True)
       fig = px.bar(dfFinal, x="Name", y='Mortes', color='Name',#color='Regiao', hover_data=['Name']
                    hover_data=['Name','Regiao'], labels={'Mortes':'Mortos 24h','Name' : 'País' },title='Mortes por país ultimas 24 horas')
       return fig

    def PlotGrafigoBarraCasosPais24h():
       dfFinal = BuildDf.DataFrameLast24h()
       dfFinal = dfFinal[(dfFinal["Casos"] > 100)]
       dfFinal.sort_values(['Casos'], inplace=True)
       fig = px.bar(dfFinal, x="Name", y='Casos', color='Name',
                    hover_data=['Name','Regiao'], labels={'Casos':'Casos 24h','Name' : 'País' },title='Casos por país ultimas 24 horas')
       return fig

    def PlotGrafigoBarraCasosPais():
        dfFinal = BuildDf.DataFrameTotais()
        dfFinal.query('TotalCases > 500000', inplace=True)
        dfFinal.sort_values(['TotalCases'], inplace=True)
        fig = px.bar(dfFinal, x="Name", y='TotalCases', color='Name',
                    hover_data=['Name','Continent'], labels={'Casos':'Casos 24h','Name' : 'País', 'Continent' : 'Regiao'},title='Casos totais por país')
        return fig

    def PlotGraficoBarraCalor():
        dfFinal = BuildDf.DataFrameTotais()
        dfFinal.query('TotalCases > 1000000', inplace=True)
        dfFinal.sort_values(['TotalRecovered'], inplace=True)
        fig = px.bar(dfFinal, x='Name', y='TotalRecovered', title='Relação Recuperados x Casos por País',
             hover_data=['TotalCases', 'TotalRecovered'], color='TotalCases',
             labels={'TotalCases':'Total de Casos', 'Name' : 'País', 'TotalRecovered' : 'Total Recuperado', 'Abr' : '1º Abril', 'Continent' : 'Região'})
        return fig

    def PlotGraficoBarraCalorPorcentagem():
        dfFinal = BuildDf.DataFrameTotais()
        dfFinal.query('TotalCases > 1000000 and TotalRecovered > 0' , inplace=True)
        perceCasos = dfUtil.RetPorcentagemCasosPopulacao(dfFinal) #((dfFinal['TotalCases'] / dfFinal['Population']) *100)
        perceMortes = dfUtil.RetPorcentagemMortesPopulacao(dfFinal) #((dfFinal['TotalDeaths'] / dfFinal['Population']) *100)
        perceCurados = dfUtil.RetPorcentagemRecuperadosPopulacao(dfFinal) #((dfFinal['TotalRecovered'] / dfFinal['Population']) *100)
        dfFinal['TotalRecovered'] = perceCurados
        dfFinal['TotalDeaths'] = perceMortes
        dfFinal.sort_values(['TotalRecovered'], inplace=True)

        fig = px.bar(dfFinal, x='Name', y="TotalRecovered", title='Porcentagem de Curados x Mortos',
             hover_data=['TotalCases', 'TotalRecovered'], color="TotalRecovered",
             labels={'TotalCases':'Total de Casos', 'Name' : 'País', 'TotalRecovered' : 'Total Recuperado', 
                     'TotalDeaths' : 'Total Mortes', 'Abr' : '1º Abril', 'Continent' : 'Região',
                    'Population' : 'População', 'color' : '% Mortos'})
        return fig

    def PlotGraficoBarPorcentagemCurados():
        dfFinal = BuildDf.DataFrameTotais() 
        perce = dfUtil.RetPorcentagemRecuperadoCasos(dfFinal) #((dfFinal['TotalRecovered'] / dfFinal['TotalCases']) *100) 
        dfFinal['TotalRecovered'] = perce;
        dfFinal.sort_values(['TotalRecovered'], inplace=True)
        fig = px.bar(dfFinal, x='Name', y='TotalRecovered', color='Name', 
                     labels={'y':'% de Curados','TotalCases':'Total de Casos','Name' : 'País',
                            'TotalDeaths' : 'Total Mortes', 'TotalRecovered' : 'Total Recuperado', 'Continent' : 'Regiao'},
             hover_data=['Name','Population', 'TotalCases', 'TotalDeaths', 'TotalRecovered','Continent'],   title='Porcentagem de Curados x Total de Casos')
        return fig

    def PlotGraficoBarPorcentagemCuradosPopulacao():
        dfFinal = BuildDf.DataFrameTotais() 
        perce = dfUtil.RetPorcentagemRecuperadosPopulacao(dfFinal) #((dfFinal['TotalRecovered'] / dfFinal['TotalCases']) *100)
        dfFinal['TotalRecovered'] = perce;
        dfFinal.sort_values(['TotalRecovered'], inplace=True)
        fig = px.bar(dfFinal, x='Name', y="TotalRecovered", color='Name', labels={'y':'% de Curados',
                                                                                  'TotalDeaths' : 'Total Mortes','TotalCases':'Total de Casos','Name' : 'País', 'TotalRecovered' : 'Total Recuperado','Continent' : 'Regiao'},
             hover_data=['Name','Population', 'TotalCases', 'TotalDeaths', 'TotalRecovered','Continent'],   title='Porcentagem de Curados x Total de População') 
        return fig

    def PlotGraficoBarPorcentagemMortosCasos():
        dfFinal = BuildDf.DataFrameTotais() 
        perce = dfUtil.RetPorcentagemMortosCasos(dfFinal) #((dfFinal['TotalDeaths'] / dfFinal['TotalCases']) *100)
        dfFinal['TotalDeaths'] = perce
        dfFinal.sort_values(['TotalDeaths'], inplace=True)
        fig = px.bar(dfFinal, x='Name', y="TotalDeaths", color='Name', labels={'y':'% de Mortos','TotalCases':'Total de Casos','Name' : 'País', 'TotalDeaths' : 'Total Mortes','Continent' : 'Regiao'},
             hover_data=['Name','Population', 'TotalCases', 'TotalDeaths', 'TotalRecovered','Continent'], title='Porcentagem de Mortes x Total de Casos')
        return fig

    def PlotGraficoBarPorcentagemMortosPopulacao():
        dfFinal = BuildDf.DataFrameTotais()
        perce = dfUtil.RetPorcentagemMortesPopulacao(dfFinal) #((dfFinal['TotalDeaths'] / dfFinal['TotalCases']) *100) 
        dfFinal['TotalDeaths'] = perce 
        dfFinal.query('TotalDeaths > 0.009', inplace=True)
        dfFinal.sort_values(['TotalDeaths'], inplace=True)
        fig = px.bar(dfFinal, x='Name', y='TotalDeaths', color='Name', labels={'y':'% de Mortos','TotalCases':'Total de Casos','Name' : 'País'
                                                                              ,'Continent' : 'Regiao','TotalDeaths' : '% Mortes', 'Population' : 'População','TotalRecovered' : 'Total Recuperado'},
             hover_data=['Name','Population', 'TotalCases', 'TotalDeaths', 'TotalRecovered','Continent'], title='Porcentagem de Mortes x População') 
        return fig

    def PlotGraficoBarPorcentagemCasos(): #NÃO USAR, FICOU ESTR
        dfFinal = BuildDf.DataFrameTotais() 
        perce = dfUtil.RetPorcentagemCasosPopulacao(dfFinal) #((dfFinal['TotalCases'] / dfFinal['Population']) *100)
        dfFinal['TotalCases'] = perce
        dfFinal.sort_values(['TotalCases'], inplace=True)
        fig = px.bar(dfFinal, x='Continent', y="TotalCases", color='Name', labels={'y':'% de Casos','TotalRecovered' : 'Total Recuperado',
                                                                                   'TotalDeaths' : 'Total Mortes','TotalCases':'Total de Casos','Continent' : 'Região', 'Population' : 'População'},
              hover_data=['Name','Population', 'TotalCases', 'TotalDeaths', 'TotalRecovered','Continent'],   title='Porcentagem de Casos x População')
        return fig 