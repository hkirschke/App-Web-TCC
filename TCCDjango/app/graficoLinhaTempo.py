import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import plotly as pl
from .DataFrameUtil import DataFrameUtil as dfUtil


class GraficoLT(): 
    def __init__(self):
        self.dfTimeSeriesCases = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
        
        self.dfTimeSeriesRecover = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
        
        self.dfTimeSeriesDeath = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
        
        url = 'https://covid19.who.int/WHO-COVID-19-global-table-data.csv'
        self.dfRegioes = pd.read_csv(url)

    def DataFrameMensal():
      pd.options.display.float_format = '{:.0f}'.format # Sem Virgula 
    
      # Motando Dataframes
      url = 'https://covid19.who.int/WHO-COVID-19-global-table-data.csv'
      dfRegioes = pd.read_csv(url)
      
      dfTimeSeriesCases = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
      
      dfTimeSeriesRecover = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
      
      dfTimeSeriesDeath = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
      
      dfTimeSeriesCases.rename(columns={'Country/Region':'Name'}, inplace=True) 
      dfTimeSeriesRecover.rename(columns={'Country/Region':'Name'}, inplace=True) 
      dfTimeSeriesDeath.rename(columns={'Country/Region':'Name'}, inplace=True) 
      
      dfTimeSeriesCases.loc[249,'Name'] = "United States of America"
      dfTimeSeriesRecover.loc[249,'Name'] = "United States of America"
      dfTimeSeriesDeath.loc[249,'Name'] = "United States of America"
      
      # Filtrando Dataframes 
      dfRegioes.columns =[column.replace(" ", "_").replace("-","") for column in dfRegioes.columns]
      dfRegioes.query('Name != "Global" and Cases__cumulative_total > 0 ',  inplace=True)
      dfRegioes.loc[0,'Name'] = 'World'
      
      # Ordenando Dataframes 
      dfRegioes.sort_values(['Name'], inplace=True)
      
      # Criando novos dataframes manipulados
      selected_columns = dfRegioes[["Name", "WHO_Region"]]
      dfRegioesNew = selected_columns.copy()
      dfRegioesNew.sort_values(['Name'], inplace=True)
      
      
      listMonth = ['Jan', 'Fev', 'Mar', 'Abr','Mai','Jun',
                      'Jul','Ago','Set','Out','Nov', 'Dez',
                      'Jan 21', 'Fev 21', 'Mar 21']
      
      dfTimeSeriesCases.drop(['Province/State', 'Lat','Long'], axis=1,inplace=True) 
      dfTimeSeriesRecover.drop(['Province/State', 'Lat','Long'], axis=1,inplace=True)
      dfTimeSeriesDeath.drop(['Province/State', 'Lat','Long'], axis=1,inplace=True) 
      
      
      selected_columns = dfTimeSeriesCases[["Name", "1/31/20","2/29/20","3/31/20","4/30/20", "5/31/20",
                                            "6/30/20", "7/31/20", "8/31/20", "9/30/20", "10/31/20","11/30/20","12/31/20",
                                            "1/31/21", "2/28/21", "3/15/21"]]
      dfTimeSeriesCases = selected_columns.copy()
      
      
      selected_columns = dfTimeSeriesRecover[["Name", "1/31/20","2/29/20","3/31/20","4/30/20", "5/31/20",
                                            "6/30/20", "7/31/20", "8/31/20", "9/30/20", "10/31/20","11/30/20","12/31/20",
                                            "1/31/21", "2/28/21", "3/15/21"]]
      dfTimeSeriesRecover = selected_columns.copy()
      
      
      selected_columns = dfTimeSeriesDeath[["Name", "1/31/20","2/29/20","3/31/20","4/30/20", "5/31/20",
                                            "6/30/20", "7/31/20", "8/31/20", "9/30/20", "10/31/20","11/30/20","12/31/20",
                                            "1/31/21", "2/28/21", "3/15/21"]]
      dfTimeSeriesDeath = selected_columns.copy()
      
      
      dfTimeSeriesCases = dfUtil.RenameCols(dfTimeSeriesCases)
      dfTimeSeriesRecover = dfUtil.RenameCols(dfTimeSeriesRecover)
      dfTimeSeriesDeath = dfUtil.RenameCols(dfTimeSeriesDeath)
      
      
      # # Renomeando colunas
      dfRegioesNew.rename(columns={'WHO_Region':'Regiao'}, inplace=True) 
      
      dfAux = dfTimeSeriesCases
      
      mapping = {dfAux.columns[0]:'Name', dfAux.columns[1]: 'Jan',dfAux.columns[2]:'Fev', 
                 dfAux.columns[3]: 'Mar',dfAux.columns[4]:'Abr', dfAux.columns[5]: 'Mai',
                 dfAux.columns[6]:'Jun', dfAux.columns[7]: 'Jul', dfAux.columns[8]: 'Ago', 
                 dfAux.columns[9]: 'Set', dfAux.columns[10]: 'Out', dfAux.columns[11]: 'Nov', 
                 dfAux.columns[12]: 'Dez',dfAux.columns[13]: 'Jan 21',dfAux.columns[14]:'Fev 21', 
                 dfAux.columns[15]: 'Mar 21'}
      dfTimeSeriesCases = dfAux.rename(columns=mapping)
      
      dfAux = dfTimeSeriesRecover 
      mapping = {dfAux.columns[0]:'Name', dfAux.columns[1]: 'Jan',dfAux.columns[2]:'Fev', 
                 dfAux.columns[3]: 'Mar',dfAux.columns[4]:'Abr', dfAux.columns[5]: 'Mai',
                 dfAux.columns[6]:'Jun', dfAux.columns[7]: 'Jul', dfAux.columns[8]: 'Ago', 
                 dfAux.columns[9]: 'Set', dfAux.columns[10]: 'Out', dfAux.columns[11]: 'Nov', 
                 dfAux.columns[12]: 'Dez',dfAux.columns[13]: 'Jan 21',dfAux.columns[14]:'Fev 21', 
                 dfAux.columns[15]: 'Mar 21'}
      dfTimeSeriesRecover = dfAux.rename(columns=mapping)
      
      dfAux = dfTimeSeriesDeath 
      mapping = {dfAux.columns[0]:'Name', dfAux.columns[1]: 'Jan',dfAux.columns[2]:'Fev', 
                 dfAux.columns[3]: 'Mar',dfAux.columns[4]:'Abr', dfAux.columns[5]: 'Mai',
                 dfAux.columns[6]:'Jun', dfAux.columns[7]: 'Jul', dfAux.columns[8]: 'Ago', 
                 dfAux.columns[9]: 'Set', dfAux.columns[10]: 'Out', dfAux.columns[11]: 'Nov', 
                 dfAux.columns[12]: 'Dez',dfAux.columns[13]: 'Jan 21',dfAux.columns[14]:'Fev 21', 
                 dfAux.columns[15]: 'Mar 21'}
      dfTimeSeriesDeath = dfAux.rename(columns=mapping)
      
      
      dfTimeSeriesCasesSomado = dfUtil.SumRows(dfTimeSeriesCases)
      dfTimeSeriesRecoverSomado = dfUtil.SumRows(dfTimeSeriesRecover) 
      dfTimeSeriesDeathSomado = dfUtil.SumRows(dfTimeSeriesDeath)
      
      # Merge dataframe
      dfFinalCases = pd.merge(dfTimeSeriesCasesSomado, dfRegioesNew, on="Name") 
      dfFinalCases.rename(columns={'WHO_Region': 'Regiao'}, inplace=True)
      
      dfFinalRecover = pd.merge(dfTimeSeriesRecoverSomado, dfRegioesNew, on="Name") 
      dfFinalRecover.rename(columns={'WHO_Region': 'Regiao'}, inplace=True)
      
      dfFinalDeath = pd.merge(dfTimeSeriesDeathSomado, dfRegioesNew, on="Name") 
      dfFinalDeath.rename(columns={'WHO_Region': 'Regiao'}, inplace=True)
      
      #MONTANDO NOVO DATAFRAME 2
      
      d = {'Name': [], 'Mes': [],'Casos': [], 'Recuperado': [], 'Mortos': [] }
      DataFrameTimeline = pd.DataFrame(data=d)
      
      # for index, row in dfFinalRecover.query('Name == "United States of America"').iterrows():    #PARA CADA PAÍS
      for index, row in dfFinalRecover.iterrows():    #PARA CADA PAÍS
        for mes in listMonth: #VOU PERCORRER POR MÊS
          DataFrameTimeline = DataFrameTimeline.append({'Name': row['Name'], 'Mes': mes, 'Casos':dfFinalCases.loc[index,mes], 
                                                          'Recuperado': dfFinalRecover.loc[index,mes], 'Mortos' : dfFinalDeath.loc[index,mes]}, ignore_index = True)

      dfFinal = pd.merge(DataFrameTimeline, dfRegioesNew, on="Name")
      dfFinal.rename(columns={'Name':'País'}, inplace=True)  
      return dfFinal

    def PlotGraphTimeLineBar():
       dfFinal = DataFrameMensal()
       dfFinal.sort_values(['Mortos'], inplace=True)
        
       fig = px.bar(dfFinal, x="Regiao", y="Mortos", color="Regiao",
          animation_frame="Mes", animation_group="País", range_y=[0,1200000],
            hover_data=['País', 'Casos', 'Recuperado'])
       fig.write_html("app/graph.html")
       pl.offline.plot(fig, filename = 'app/graph.html')
       #pl.offline.plot(fig, include_plotlyjs=False, output_type='div')

    def PlotGraphTimeLineScatter():
        dfFinal = DataFrameMensal()
        px.scatter(dfFinal, x="Mortos", y="Casos", animation_frame="Mes", animation_group="País",
               size="Casos", color="Regiao", hover_name="País",
               log_x=True, size_max=80, range_x=[1000,1000000], range_y=[10000,40000000])
    