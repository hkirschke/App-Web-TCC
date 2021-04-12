import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import plotly as pl
import re
import requests
from .DataFrameUtil import DataFrameUtil as dfUtil


class CreateDataFrame(): 
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
                      'Jul', 'Ago','Set','Out','Nov', 'Dez',
                      'Jan 21', 'Fev 21', 'Mar 21']
      
      dfTimeSeriesCases.drop(['Province/State', 'Lat','Long'], axis=1,inplace=True) 
      dfTimeSeriesRecover.drop(['Province/State', 'Lat','Long'], axis=1,inplace=True)
      dfTimeSeriesDeath.drop(['Province/State', 'Lat','Long'], axis=1,inplace=True) 
      
      
      selected_columns = dfTimeSeriesCases[dfUtil.SelectColumnsMensal()]
      dfTimeSeriesCases = selected_columns.copy()
      
      
      selected_columns = dfTimeSeriesRecover[dfUtil.SelectColumnsMensal()]
      dfTimeSeriesRecover = selected_columns.copy()
      
      
      selected_columns = dfTimeSeriesDeath[dfUtil.SelectColumnsMensal()]
      dfTimeSeriesDeath = selected_columns.copy()
      
      
      dfTimeSeriesCases = dfUtil.RenameColsMesAno(dfTimeSeriesCases)
      dfTimeSeriesRecover = dfUtil.RenameColsMesAno(dfTimeSeriesRecover)
      dfTimeSeriesDeath = dfUtil.RenameColsMesAno(dfTimeSeriesDeath)
      
      
      # # Renomeando colunas
      dfRegioesNew.rename(columns={'WHO_Region':'Regiao'}, inplace=True) 
      
      dfAux = dfTimeSeriesCases 
      mapping = dfUtil.CreateMappingMensal(dfTimeSeriesCases)
      dfTimeSeriesCases = dfAux.rename(columns=mapping)
      
      dfAux = dfTimeSeriesRecover 
      mapping = dfUtil.CreateMappingMensal(dfTimeSeriesRecover)
      dfTimeSeriesRecover = dfAux.rename(columns=mapping)
      
      dfAux = dfTimeSeriesDeath 
      mapping = dfUtil.CreateMappingMensal(dfTimeSeriesDeath)
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

    def DataFrameQuinzenal():
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
      
      
      listMonth = ['1 Jan', '2 Jan', '1 Fev','2 Fev', '1 Mar','2 Mar', '1 Abr','2 Abr',
                   '1 Mai','2 Mai','1 Jun','2 Jun','1 Jul','2 Jul', '1 Ago', '2 Ago', 
                   '1 Set','2 Set','1 Out','2 Out','1 Nov','2 Nov', '1 Dez','2 Dez',
                   '1 Jan 21', '2 Jan 21','1 Fev 21','2 Fev 21', '1 Mar 21','2 Mar 21']
      
      dfTimeSeriesCases.drop(['Province/State', 'Lat','Long'], axis=1,inplace=True) 
      dfTimeSeriesRecover.drop(['Province/State', 'Lat','Long'], axis=1,inplace=True)
      dfTimeSeriesDeath.drop(['Province/State', 'Lat','Long'], axis=1,inplace=True) 
      
      
      selected_columns = dfTimeSeriesCases[dfUtil.SelectColumnsQuinzena()]
      dfTimeSeriesCases = selected_columns.copy()
      
      
      selected_columns = dfTimeSeriesRecover[dfUtil.SelectColumnsQuinzena()]
      dfTimeSeriesRecover = selected_columns.copy()
      
      
      selected_columns = dfTimeSeriesDeath[dfUtil.SelectColumnsQuinzena()]
      dfTimeSeriesDeath = selected_columns.copy()
      
      
      dfTimeSeriesCases = dfUtil.RenameColsMesQuinzena(dfTimeSeriesCases)
      dfTimeSeriesRecover = dfUtil.RenameColsMesQuinzena(dfTimeSeriesRecover)
      dfTimeSeriesDeath = dfUtil.RenameColsMesQuinzena(dfTimeSeriesDeath)
      
      
      # # Renomeando colunas
      dfRegioesNew.rename(columns={'WHO_Region':'Regiao'}, inplace=True) 
      
      dfAux = dfTimeSeriesCases 
      mapping = dfUtil.CreateMappingQuinzenal(dfTimeSeriesCases)
      dfTimeSeriesCases = dfAux.rename(columns=mapping)
      
      dfAux = dfTimeSeriesRecover 
      mapping = dfUtil.CreateMappingQuinzenal(dfTimeSeriesRecover)
      dfTimeSeriesRecover = dfAux.rename(columns=mapping)
      
      dfAux = dfTimeSeriesDeath 
      mapping = dfUtil.CreateMappingQuinzenal(dfTimeSeriesDeath)
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

    def DataFrameLast24h():
        pd.options.display.float_format = '{:.0f}'.format
 
        url = 'https://covid19.who.int/WHO-COVID-19-global-table-data.csv'

        df = pd.read_csv(url) 

        df = df[(df["WHO Region"] != "Global" ) & (df["Cases - cumulative total"] > 0 )]
        df = df[(df["WHO Region"] != "Global" ) & (df["Deaths - newly reported in last 24 hours"] > 100)  & (df["Cases - cumulative total"] > 0 )]
        return df

    def DataFrameTotais():
        url = 'https://covid19.who.int/WHO-COVID-19-global-table-data.csv'
        dfRegioes = pd.read_csv(url)
        
        table_MN = pd.read_html('https://en.wikipedia.org/wiki/COVID-19_pandemic_cases', match='Cumulative COVID-19 cases at start of each month')
        dfWiki = table_MN[1]
        
        html_source = requests.get("https://www.worldometers.info/coronavirus/").text
        html_source = re.sub(r'<.*?>', lambda g: g.group(0).upper(), html_source)
        
        table_MN2 = pd.read_html(html_source)
        dfWorldMeters = table_MN2[0]
        
        # Filtrando Dataframes 
        dfRegioes.columns =[column.replace(" ", "_").replace("-","") for column in dfRegioes.columns]
        dfWorldMeters.columns = [column.replace(" ", "_").replace(",", "_").replace("-","").replace("__","_") for column in dfWorldMeters.columns]
        
        dfWiki.query('Date != "World" and Date != "Days to double" and Date != "Countries and territories" ', inplace=True)
        dfRegioes.query('Name != "Global" and Cases__cumulative_total > 0 ',  inplace=True)
        dfWorldMeters.query('Country_Other != "Total: " and   Country_Other != "World" and  Country_Other != "North America" and Country_Other != "South America" and Country_Other != "Asia" and Country_Other != "Europe" and Country_Other != "Africa" and Country_Other != "Oceania"',  inplace=True)
        
        dfRegioes.loc[0,'Name'] = 'World'
        
        # Ordenando Dataframes 
        dfWiki.sort_values(['Date'], inplace=True)
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
        dfWiki.rename(columns={'Date': 'Name'}, inplace=True)
        dfWorldMetersNew.rename(columns={'Country_Other': 'Name'}, inplace=True)
        
        dfWiki.rename(columns={'Jan 4': 'Jan'}, inplace=True) 
        dfWiki.rename(columns={'Feb 1': 'Fev'}, inplace=True) 
        dfWiki.rename(columns={'Mar 1': 'Mar'}, inplace=True)
        dfWiki.rename(columns={'Apr 1': 'Abr'}, inplace=True)
        
        # Merge dataframes
        dfPre = pd.merge(dfWiki, dfRegioesNew, on="Name")
        dfFinal = pd.merge(dfPre, dfWorldMetersNew, on="Name")
        dfFinal.rename(columns={'WHO_Region': 'continent'}, inplace=True)
        
        
        mapping = {dfFinal.columns[0]:'Name', dfFinal.columns[1]: 'FirstCase', dfFinal.columns[2]:'Jan', dfFinal.columns[3]: 'Fev',dfFinal.columns[4]:'Mar', 
                   dfFinal.columns[5]:'Abr', dfFinal.columns[6]: 'Continent',dfFinal.columns[7]: 'TotalCases', dfFinal.columns[8]: 'TotalRecovered',dfFinal.columns[9]: "TotalDeaths",dfFinal.columns[10]: "Population"}
        dfFinal = dfFinal.rename(columns=mapping)
        return dfFinal