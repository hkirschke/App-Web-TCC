from dateutil.parser import parse
from datetime import datetime
from .DateUtil import DateUtil as dateUtil

class DataFrameUtil():
    """Classe de utilitários para a manipulações e tratamento de dados e dataframes"""
    def isDate(string, fuzzy=False): 
        try: 
            parse(string, fuzzy=fuzzy)
            return True
    
        except ValueError:
            return False

    def SumRows(Dataframe):
      grouped_df = Dataframe.groupby(["Name"])
    
      grouped_and_summed = grouped_df.sum()
      grouped_and_summed = grouped_and_summed.reset_index()
      return grouped_and_summed
    
    def RenameColsMesAno(Dataframe):
      for col in Dataframe.columns:
        if dateUtil.isDate(col):
          ano = datetime.strptime(col, '%m/%d/%y').year #.dt.year #%m/%d/%Y,
          mes = datetime.strptime(col, '%m/%d/%y').month
          newName =  str(mes) + "/" + str(ano)
          Dataframe.rename(columns={col:newName}, inplace=True)
      return Dataframe
    
    def CreateMappingMensal(DataFrame):
         mapping = {DataFrame.columns[0]:'Name', DataFrame.columns[1]: 'Jan',DataFrame.columns[2]: 'Fev', 
                 DataFrame.columns[3]: 'Mar',DataFrame.columns[4]: 'Abr', DataFrame.columns[5]: 'Mai',
                 DataFrame.columns[6]: 'Jun', DataFrame.columns[7]: 'Jul', DataFrame.columns[8]: 'Ago', 
                 DataFrame.columns[9]: 'Set', DataFrame.columns[10]: 'Out', DataFrame.columns[11]: 'Nov', 
                 DataFrame.columns[12]: 'Dez',DataFrame.columns[13]: 'Jan 21',DataFrame.columns[14]: 'Fev 21', 
                 DataFrame.columns[15]: 'Mar 21', DataFrame.columns[16]: 'Abr 21'}
         return mapping 

    def SelectColumnsMensal():
        obj = ["Name", "1/31/20","2/29/20","3/31/20","4/30/20", "5/31/20",
                                            "6/30/20", "7/31/20", "8/31/20", "9/30/20", "10/31/20","11/30/20","12/31/20",
                                            "1/31/21", "2/28/21", "3/31/21", "4/30/21"]

        return obj

    def RetPorcentagemRecuperadoCasos(Dataframe):
       return round((Dataframe['TotalRecovered'] / Dataframe['TotalCases']) *100,2)

    def RetPorcentagemMortosCasos(Dataframe):
       return round((Dataframe['TotalDeaths'] / Dataframe['TotalCases']) *100,2) 

    def RetPorcentagemCasosPopulacao(Dataframe):
     return round((Dataframe['TotalCases'] / Dataframe['Population']) *100,2)

    def RetPorcentagemCasosPopulacaoMensal(Dataframe):
     return round((Dataframe['Casos'] / Dataframe['Populacao']) *100,2)

    def RetPorcentagemMortosPopulacaoMensal(Dataframe):
     return round((Dataframe['Mortos'] / Dataframe['Populacao']) *100,2)

    def RetPorcentagemMortesPopulacao(Dataframe):
        return round((Dataframe['TotalDeaths'] / Dataframe['Population']) *100,2)

    def RetPorcentagemRecuperadosPopulacao(Dataframe):
        return round((Dataframe['TotalRecovered'] / Dataframe['Population']) *100,2)

    def MontaDataFrame():
        qs = MyModel.objects.all() 
        df = read_frame(qs)
        return df
    

    