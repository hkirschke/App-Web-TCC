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
      grouped_and_summed  = grouped_and_summed.reset_index()
      return grouped_and_summed
    
    def RenameCols(Dataframe):
      for col in Dataframe.columns:
        if dateUtil.isDate(col):
          ano = datetime.strptime(col, '%m/%d/%y').year #.dt.year #%m/%d/%Y,
          mes = datetime.strptime(col, '%m/%d/%y').month
          newName =  str(mes) + "/" + str(ano)
          Dataframe.rename(columns={col:newName}, inplace=True)
      return Dataframe 
    
    def MontaDataFrame():
        qs = MyModel.objects.all() 
        df = read_frame(qs)
        return df
    

    