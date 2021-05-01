import pandas as pd
import plotly.express as px
import plotly as pl 
from .CreateDataFrame import CreateDataFrame as BuildDf
from .DataFrameUtil import DataFrameUtil as dfUtil


class GraficoLT(): 
    def PlotGraphTimeLineBarMensal():
       dfFinal = BuildDf.DataFrameMensal()
       fig = px.bar(dfFinal, x="Regiao", y="Mortos", color="Regiao",
          animation_frame="Mes", animation_group="País", range_y=[0,"Mortos"],
            hover_data=['País', 'Casos', 'Recuperado'],title='Linha de tempo Mortes')
       return fig

    def PlotGraphTimeLineScatterMensal():
        dfFinal = BuildDf.DataFrameMensal()
        fig = px.scatter(dfFinal, x="Mortos", y="Casos", animation_frame="Mes", animation_group="País",
               size="Casos", color="Regiao", hover_name="País",
               log_x=True, size_max=100, title='Linha de tempo Casos x Mortes')
        return fig

    def PlotGraphTimeLineScatterMensalPorcentagemCasosPopulacao():
        dfFinal = BuildDf.DataFrameMensal()
        perceCasos = dfUtil.RetPorcentagemCasosPopulacaoMensal(dfFinal)
        dfFinal['Casos'] = perceCasos
        perceMortos = dfUtil.RetPorcentagemMortosPopulacaoMensal(dfFinal)
        dfFinal['Mortos'] =perceMortos
        fig = px.scatter(dfFinal, x="Mortos", y="Casos", animation_frame="Mes", animation_group="País",
               size="Casos", color="Regiao", hover_name="País", size_max=40 
               , title='Linha de tempo Casos x Mortes')
        return fig