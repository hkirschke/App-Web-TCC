from dateutil.parser import parse
from datetime import datetime
from .DateUtil import DateUtil as dateUtil

class DataFrameUtil():
    """description of class"""
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

    def RenameColsMesQuinzena(Dataframe):
      for col in Dataframe.columns:
        if dateUtil.isDate(col):
          ano = datetime.strptime(col, '%m/%d/%y').year #.dt.year #%m/%d/%Y,
          mes = datetime.strptime(col, '%m/%d/%y').month
          dia = datetime.strptime(col, '%m/%d/%y').day
          newName = str(dia) + "/" + str(mes) + "/" + str(ano)
          Dataframe.rename(columns={col:newName}, inplace=True)
      return Dataframe 
    
    def CreateMappingQuinzenal(DataFrame):
        mapping = {DataFrame.columns[0]:'Name', DataFrame.columns[1]: '1 Jan', DataFrame.columns[2]: '2 Jan', DataFrame.columns[3]: '1 Fev',
                   DataFrame.columns[4]: '2 Fev', DataFrame.columns[5]: '1 Mar', DataFrame.columns[6]: '2 Mar', DataFrame.columns[7]: '1 Abr', 
                   DataFrame.columns[8]: '2 Abr', DataFrame.columns[9]: '1 Mai', DataFrame.columns[10]: '2 Mai', DataFrame.columns[11]: '1 Jun',
                   DataFrame.columns[12]: '2 Jun', DataFrame.columns[13]: '1 Jul', DataFrame.columns[14]: '2 Jul', DataFrame.columns[15]: '1 Ago', 
                   DataFrame.columns[16]: '2 Ago', DataFrame.columns[17]: '1 Set', DataFrame.columns[18]: '2 Set', DataFrame.columns[19]: '1 Out', 
                   DataFrame.columns[20]: '2 Out', DataFrame.columns[21]: '1 Nov', DataFrame.columns[22]: '2 Nov', DataFrame.columns[23]: '1 Dez',
                   DataFrame.columns[24]: '2 Dez', DataFrame.columns[25]: '1 Jan 21', DataFrame.columns[26]: '2 Jan 21', DataFrame.columns[27]: '1 Fev 21', 
                   DataFrame.columns[28]: '2 Fev 21', DataFrame.columns[29]: '1 Mar 21', DataFrame.columns[30]: '2 Mar 21'}
        #mapping = {DataFrame.columns[0]:'Name', 
        #DataFrame.columns[1]: '1 Jan', DataFrame.columns[2]: '1 Fev', DataFrame.columns[3]: '1 Mar', DataFrame.columns[4]: '1 Abr', 
        #DataFrame.columns[5]: '1 Mai',DataFrame.columns[6]: '1 Jun', DataFrame.columns[7]: '1 Jul', DataFrame.columns[8]: '1 Ago', 
        #DataFrame.columns[9]: '1 Set', DataFrame.columns[10]: '1 Out', DataFrame.columns[11]: '1 Nov', DataFrame.columns[12]: '1 Dez',
        #DataFrame.columns[13]: '1 Jan 21',DataFrame.columns[14]: '1 Fev 21', DataFrame.columns[15]: '1 Mar 21', DataFrame.columns[16]: '2 Jan',
        #DataFrame.columns[17]: '2 Fev', DataFrame.columns[18]: '2 Mar', DataFrame.columns[19]: '2 Abr', DataFrame.columns[20]: '2 Mai', DataFrame.columns[21]: '2 Jun', 
        #DataFrame.columns[22]: '2 Jul', DataFrame.columns[23]: '2 Ago', DataFrame.columns[24]: '2 Set', DataFrame.columns[25]: '2 Out', DataFrame.columns[26]: '2 Nov', 
        #DataFrame.columns[27]: '2 Dez', DataFrame.columns[28]: '2 Jan 21', DataFrame.columns[29]: '2 Fev 21', DataFrame.columns[30]: '2 Mar 21'}
        return mapping

    def CreateMappingMensal(DataFrame):
         mapping = {DataFrame.columns[0]:'Name', DataFrame.columns[1]: 'Jan',DataFrame.columns[2]: 'Fev', 
                 DataFrame.columns[3]: 'Mar',DataFrame.columns[4]: 'Abr', DataFrame.columns[5]: 'Mai',
                 DataFrame.columns[6]: 'Jun', DataFrame.columns[7]: 'Jul', DataFrame.columns[8]: 'Ago', 
                 DataFrame.columns[9]: 'Set', DataFrame.columns[10]: 'Out', DataFrame.columns[11]: 'Nov', 
                 DataFrame.columns[12]: 'Dez',DataFrame.columns[13]: 'Jan 21',DataFrame.columns[14]: 'Fev 21', 
                 DataFrame.columns[15]: 'Mar 21', DataFrame.columns[16]: 'Abr 21'}
         return mapping

    def SelectColumnsQuinzena():
         obj = ["Name", "1/22/20", "1/31/20","2/15/20","2/29/20","3/15/20", "3/31/20","4/15/20", "4/30/20", 
                                            "5/15/20","5/31/20","6/15/20","6/30/20", "7/15/20","7/31/20","8/15/20", "8/31/20", 
                                            "9/15/20","9/30/20", "10/15/20","10/31/20","11/15/20","11/30/20","12/15/20","12/31/20",
                                            "1/15/21","1/31/21","2/15/21", "2/28/21","3/15/21", "3/31/21"]
         return obj

    def SelectColumnsMensal():
        #current_day = datetime.date.today()
        #ano = datetime.strptime(current_day, '%m/%d/%y').year #.dt.year #%m/%d/%Y,
        #mes = datetime.strptime(current_day, '%m/%d/%y').month
        #dia = datetime.strptime(current_day, '%m/%d/%y').day
        #current_dayFormat = str(dia) + "/" + str(mes) + "/" + str(ano)
        obj = ["Name", "1/31/20","2/29/20","3/31/20","4/30/20", "5/31/20",
                                            "6/30/20", "7/31/20", "8/31/20", "9/30/20", "10/31/20","11/30/20","12/31/20",
                                            "1/31/21", "2/28/21", "3/31/21", "4/10/21"]

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
    

    