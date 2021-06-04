import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import plotly as pl
import re
import requests
from .DataFrameUtil import DataFrameUtil as dfUtil


class CreateDataFrame():
    """Classe de serviços para a criação de dataframes utilizados para a construção dos gráficos"""
    def __init__(self):
        self.dfTimeSeriesCases = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
        
        self.dfTimeSeriesRecover = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
        
        self.dfTimeSeriesDeath = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
        
        url = 'https://covid19.who.int/WHO-COVID-19-global-table-data.csv'
        self.dfRegioes = pd.read_csv(url)

    def DataFrameMensal():
      pd.options.display.float_format = '{:.0f}'.format # Sem Virgula 
    
      # Motando Dataframes
      # Coletando dados através de arquivos CSV, disponibilizados online.
      url = 'https://covid19.who.int/WHO-COVID-19-global-table-data.csv'
      dfRegioes = pd.read_csv(url)
      
      dfTimeSeriesCases = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
      
      dfTimeSeriesRecover = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
      
      dfTimeSeriesDeath = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
      
      # Coletando dados através de web scrapping
      html_source = requests.get("https://www.worldometers.info/coronavirus/").text
      html_source = re.sub(r'<.*?>', lambda g: g.group(0).upper(), html_source)
        
      table_MN2 = pd.read_html(html_source)
      dfWorldMeters = table_MN2[0] 
      dfWorldMeters.columns = [column.replace(" ", "_").replace(",", "_").replace("-","").replace("__","_") for column in dfWorldMeters.columns]
        
      # Renomeando colunas, padronização
      dfTimeSeriesCases.rename(columns={'Country/Region':'Name'}, inplace=True) 
      dfTimeSeriesRecover.rename(columns={'Country/Region':'Name'}, inplace=True) 
      dfTimeSeriesDeath.rename(columns={'Country/Region':'Name'}, inplace=True) 
      
      # Normalização de nome de países
      dfTimeSeriesCases.loc[249,'Name'] = "United States of America"
      dfTimeSeriesRecover.loc[249,'Name'] = "United States of America"
      dfTimeSeriesDeath.loc[249,'Name'] = "United States of America"
      dfWorldMeters.loc[8, 'Country_Other']= "United States of America"
      dfWorldMeters.loc[13, 'Country_Other']= "United Kingdom"
      dfRegioes.loc[6, 'Name'] ="United Kingdom"

      
      # Filtrando Dataframes 
      dfRegioes.columns =[column.replace(" ", "_").replace("-","") for column in dfRegioes.columns]
      dfRegioes.query('Name != "Global" and Name != "World" and Cases__cumulative_total > 0 and WHO_Region != "NaN"',  inplace=True) 
      dfWorldMeters.query('Country_Other != "Total: " and  Country_Other != "World" and  ' +
                      ' Country_Other != "North America" and Country_Other != "South America" and Country_Other != "Asia" and Country_Other != "Europe" ' +
                    'and Country_Other != "Africa" and Country_Other != "Oceania" and Country_Other != "Total:" and Country_Other != "NaN" and Population != "nan" and Population != "NaN"',  inplace=True)
      
      
      # Ordenando Dataframes 
      dfRegioes.sort_values(['Name'], inplace=True)
      dfWorldMeters.sort_values(['Country_Other'], inplace=True)
      
      # Criando novos dataframes manipulados
      selected_columns = dfRegioes[["Name", "WHO_Region"]]
      dfRegioesNew = selected_columns.copy()
      dfRegioesNew.sort_values(['Name'], inplace=True)
      
      
      listMonth = ['Jan', 'Fev', 'Mar', 'Abr','Mai','Jun',
                      'Jul', 'Ago','Set','Out','Nov', 'Dez',
                      'Jan 21', 'Fev 21', 'Mar 21', 'Abr 21']
      
      dfTimeSeriesCases.drop(['Province/State', 'Lat','Long'], axis=1,inplace=True) 
      dfTimeSeriesRecover.drop(['Province/State', 'Lat','Long'], axis=1,inplace=True)
      dfTimeSeriesDeath.drop(['Province/State', 'Lat','Long'], axis=1,inplace=True) 
      
      
      selected_columns = dfTimeSeriesCases[dfUtil.SelectColumnsMensal()]
      dfTimeSeriesCases = selected_columns.copy()
      
      
      selected_columns = dfTimeSeriesRecover[dfUtil.SelectColumnsMensal()]
      dfTimeSeriesRecover = selected_columns.copy()
      
      
      selected_columns = dfTimeSeriesDeath[dfUtil.SelectColumnsMensal()]
      dfTimeSeriesDeath = selected_columns.copy()

      selected_columns = dfWorldMeters[["Country_Other", "Population"]]
      dfWorldMetersNew = selected_columns.copy()  
      dfWorldMetersNew.sort_values(['Country_Other'], inplace=True)
      
      
      dfTimeSeriesCases = dfUtil.RenameColsMesAno(dfTimeSeriesCases)
      dfTimeSeriesRecover = dfUtil.RenameColsMesAno(dfTimeSeriesRecover)
      dfTimeSeriesDeath = dfUtil.RenameColsMesAno(dfTimeSeriesDeath)
      
      
      # Renomeando colunas, padronização para merge final dos dataframes
      dfRegioesNew.rename(columns={'WHO_Region':'Regiao'}, inplace=True) 
      dfWorldMetersNew.rename(columns={'Country_Other': 'Name'}, inplace=True)
      dfWorldMetersNew.rename(columns={'Population': 'Populacao'}, inplace=True)
      
      dfAux = dfTimeSeriesCases 
      mapping = dfUtil.CreateMappingMensal(dfTimeSeriesCases)
      dfTimeSeriesCases = dfAux.rename(columns=mapping)
      
      dfAux = dfTimeSeriesRecover 
      mapping = dfUtil.CreateMappingMensal(dfTimeSeriesRecover)
      dfTimeSeriesRecover = dfAux.rename(columns=mapping)
      
      dfAux = dfTimeSeriesDeath 
      mapping = dfUtil.CreateMappingMensal(dfTimeSeriesDeath)
      dfTimeSeriesDeath = dfAux.rename(columns=mapping)
      
      #Somando resultados montados através das linhas do Dataframe
      dfTimeSeriesCasesSomado = dfUtil.SumRows(dfTimeSeriesCases)
      dfTimeSeriesRecoverSomado = dfUtil.SumRows(dfTimeSeriesRecover) 
      dfTimeSeriesDeathSomado = dfUtil.SumRows(dfTimeSeriesDeath) 

      # Resetando index dos dataframes
      dfRegioesNew.reset_index(drop=True)
      dfWorldMetersNew.reset_index(drop=True)
      dfTimeSeriesCasesSomado.reset_index(drop=True)
      dfTimeSeriesRecoverSomado.reset_index(drop=True)
      dfTimeSeriesDeathSomado.reset_index(drop=True)
       

      dfTimeSeriesCasesSomado.sort_values(['Name'], inplace=True)
      dfTimeSeriesRecoverSomado.sort_values(['Name'], inplace=True)
      dfTimeSeriesDeathSomado.sort_values(['Name'], inplace=True)
      dfRegioesNew.sort_values(['Name'], inplace=True)
      dfWorldMetersNew.sort_values(['Name'], inplace=True) 
      
      # Merge dataframe
      dfFinalCases = pd.merge(dfTimeSeriesCasesSomado, dfRegioesNew, on="Name") 
      dfFinalCases.rename(columns={'WHO_Region': 'Regiao'}, inplace=True)
      
      dfFinalRecover = pd.merge(dfTimeSeriesRecoverSomado, dfRegioesNew, on="Name") 
      dfFinalRecover.rename(columns={'WHO_Region': 'Regiao'}, inplace=True)
      
      dfFinalDeath = pd.merge(dfTimeSeriesDeathSomado, dfRegioesNew, on="Name") 
      dfFinalDeath.rename(columns={'WHO_Region': 'Regiao'}, inplace=True)
      
      #MONTANDO NOVO DATAFRAME 2
      
      d = {'Name': []  ,'Mes': []   ,'Recuperado': []}
      DataFrameRecover = pd.DataFrame(data=d)
      
      # print(dfFinalRecover.to_string())
      
      # # for index, row in dfFinalRecover.query('Name == "United States of America"').iterrows():    #PARA CADA PAÍS
      for index, row in dfFinalRecover.iterrows():    #PARA CADA PAÍS
        for mes in listMonth: #PERCORRER POR MÊS
          DataFrameRecover = DataFrameRecover.append({'Name': dfFinalRecover.loc[index,'Name']
                                                        ,'Mes': mes
                                                        #,'Casos':dfFinalCases.loc[index,mes]
                                                        ,'Recuperado': dfFinalRecover.loc[index,mes]
                                                        #,'Mortos' : dfFinalDeath.loc[index,mes]
                                                        }, ignore_index = True) 
          
      
      d = {'Name': []
           ,'Mes': []
           ,'Casos': []
           }
      DataFrameCasos = pd.DataFrame(data=d)
      
      for index, row in dfFinalCases.iterrows():    #PARA CADA PAÍS
        for mes in listMonth: #PERCORRER POR MÊS
          DataFrameCasos = DataFrameCasos.append({'Name': dfFinalCases.loc[index,'Name']
                                                        ,'Mes': mes
                                                        ,'Casos':dfFinalCases.loc[index,mes]
                                                        }, ignore_index = True)
          
      
      d = {'Name': []
           ,'Mes': []
           ,'Mortos': []
           }
      DataFrameDeath = pd.DataFrame(data=d)
      
      for index, row in dfFinalDeath.iterrows():    #PARA CADA PAÍS
        for mes in listMonth: #PERCORRER POR MÊS
          DataFrameDeath = DataFrameDeath.append({'Name': dfFinalDeath.loc[index,'Name']
                                                        ,'Mes': mes
                                                        ,'Mortos':dfFinalDeath.loc[index,mes]
                                                        }, ignore_index = True)
      
      dtTimeline = pd.merge(DataFrameCasos, DataFrameDeath,  on=['Name','Mes'])
      DataFrameTimeline = pd.merge(dtTimeline, DataFrameRecover,  on=['Name','Mes']) 

      dfPre = pd.merge(DataFrameTimeline, dfRegioesNew, on="Name")
      dfFinal = pd.merge(dfPre, dfWorldMetersNew, on="Name") 
      dfFinal.query('Casos != "nan" and Casos != "NaN" and Populacao != "nan" and Populacao != "NaN" and Mortos != "nan" and Mortos != "NaN" ', inplace=True)
      dfFinal.rename(columns={'Name':'País'}, inplace=True)
     
      return dfFinal

    def DataFrameLast24h():
        # Motando Dataframe
        # Coletando dados através de arquivos CSV, disponibilizados online.
        pd.options.display.float_format = '{:.0f}'.format
 
        url = 'https://covid19.who.int/WHO-COVID-19-global-table-data.csv'

        df = pd.read_csv(url) 
        # Filtros dos dados
        df = df[(df["WHO Region"] != "Global" ) & (df["Cases - cumulative total"] > 0 )]
        # Padronização nome das colunas
        df.columns = [column.replace(" ", "_").replace(",", "_").replace("-","").replace("__","_") for column in df.columns]
        # Filtros dos dados
        df.query('Name != "Global" and Name != "World" and Cases_cumulative_total > 0 and WHO_Region != "NaN"',  inplace=True)
        # Alteração dos nomes para dataframe final utilizado
        df.rename(columns={'WHO_Region':'Regiao'}, inplace=True) 
        df.rename(columns={'Deaths_newly_reported_in_last_24_hours':'Mortes'}, inplace=True)
        df.rename(columns={'Cases_newly_reported_in_last_24_hours':'Casos'}, inplace=True)
        # Reset dos index, para casos que será feita alguma ordenação
        df.reset_index(drop=True)
        return df

    def DataFrameTotais():
        url = 'https://covid19.who.int/WHO-COVID-19-global-table-data.csv'
        dfRegioes = pd.read_csv(url)
        
        html_source = requests.get("https://www.worldometers.info/coronavirus/").text
        html_source = re.sub(r'<.*?>', lambda g: g.group(0).upper(), html_source)
        
        table_MN2 = pd.read_html(html_source)
        dfWorldMeters = table_MN2[0]
        
        # Filtrando Dataframes 
        dfRegioes.columns =[column.replace(" ", "_").replace("-","") for column in dfRegioes.columns]
        dfWorldMeters.columns = [column.replace(" ", "_").replace(",", "_").replace("-","").replace("__","_") for column in dfWorldMeters.columns]
        
       # dfWiki.query('Date != "World" and Date != "Days to double" and Date != "Countries and territories" ', inplace=True)
        dfRegioes.query('Name != "Global" and Cases__cumulative_total > 0 and Name != "Global" ',  inplace=True)
        dfWorldMeters.query('Country_Other != "Total: " and  Country_Other != "World" and  ' +
                      ' Country_Other != "North America" and Country_Other != "South America" and Country_Other != "Asia" and Country_Other != "Europe" ' +
                    'and Country_Other != "Africa" and Country_Other != "Oceania" and Country_Other != "Total:" and Country_Other != "NaN" and Population != "nan" ',  inplace=True)
        
        # Normalização de nome de países
        dfWorldMeters.loc[8, 'Country_Other']= "United States of America"
        dfWorldMeters.loc[13, 'Country_Other']= "United Kingdom"
        dfRegioes.loc[6, 'Name'] ="United Kingdom"

        
        # Ordenando Dataframes
        dfRegioes.sort_values(['Name'], inplace=True)
        dfWorldMeters.sort_values(['Country_Other'], inplace=True)
        
        # Criando novos dataframes manipulados
        selected_columns = dfRegioes[["Name", "WHO_Region"]]
        dfRegioesNew = selected_columns.copy()
        dfRegioesNew.sort_values(['Name'], inplace=True)
        
        selected_columns = dfWorldMeters[["Country_Other", "TotalCases", "TotalRecovered","TotalDeaths", "Population"]]
        dfWorldMetersNew = selected_columns.copy()  
        dfWorldMetersNew.sort_values(['Country_Other'], inplace=True)
        
        # Renomeando colunas
        dfWorldMetersNew.rename(columns={'Country_Other': 'Name'}, inplace=True)

        # Resetando index, para casos que será feita alguma ordenação
        dfRegioesNew.reset_index(drop=True) 
        dfWorldMetersNew.reset_index(drop=True)
        
        # Merge dataframes
        dfFinal = pd.merge(dfRegioesNew, dfWorldMetersNew, on="Name")
        dfFinal.rename(columns={'WHO_Region': 'Continent'}, inplace=True)
        
        
        mapping = {dfFinal.columns[0]:'Name', dfFinal.columns[1]: 'Continent',dfFinal.columns[2]: 'TotalCases', dfFinal.columns[3]: 'TotalRecovered',dfFinal.columns[4]: "TotalDeaths",dfFinal.columns[5]: "Population"}
        dfFinal = dfFinal.rename(columns=mapping)
        return dfFinal