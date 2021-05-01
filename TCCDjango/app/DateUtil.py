from dateutil.parser import parse
from datetime import datetime

class DateUtil():
    """Classe para funções para manipular e tratar dados relacionados a data"""
    def isDate(string, fuzzy=False): 
        try: 
            parse(string, fuzzy=fuzzy)
            return True
    
        except ValueError:
            return False