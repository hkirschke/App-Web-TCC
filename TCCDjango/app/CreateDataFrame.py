import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import plotly as pl
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
                                            "1/31/21", "2/28/21", "3/31/21"]]
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

    def DataFrameLast24h():
        pd.options.display.float_format = '{:.0f}'.format
 
        url = 'https://covid19.who.int/WHO-COVID-19-global-table-data.csv'

        df = pd.read_csv(url) 

        df = df[(df["WHO Region"] != "Global" ) & (df["Cases - cumulative total"] > 0 )]

    def DataFrame():
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
        
        selected_columns = dfWorldMeters[["Country_Other", "TotalCases", "TotalRecovered"]]
        dfWorldMetersNew = selected_columns.copy()  
        dfWorldMetersNew.sort_values(['Country_Other'], inplace=True)
        
        # Renomeando colunas
        dfWiki.rename(columns={'Date': 'Name'}, inplace=True)
        dfWorldMetersNew.rename(columns={'Country_Other': 'Name'}, inplace=True)
        
        dfWiki.rename(columns={'Jan 4': 'Jan'}, inplace=True) 
        dfWiki.rename(columns={'Feb 1': 'Fev'}, inplace=True) 
        dfWiki.rename(columns={'Mar 1': 'Mar'}, inplace=True)
        
        # Merge dataframes
        dfPre = pd.merge(dfWiki, dfRegioesNew, on="Name")
        dfFinal = pd.merge(dfPre, dfWorldMetersNew, on="Name")
        dfFinal.rename(columns={'WHO_Region': 'continent'}, inplace=True)
        
        
        mapping = {dfFinal.columns[0]:'Name', dfFinal.columns[1]: 'FirstCase', dfFinal.columns[2]:'Jan', dfFinal.columns[3]: 'Fev',dfFinal.columns[4]:'Mar', dfFinal.columns[5]: 'Continent',dfFinal.columns[6]: 'TotalCases', dfFinal.columns[7]: 'TotalRecovered'}
        dfFinal = dfFinal.rename(columns=mapping)


    