from dateutil.parser import parse
from datetime import datetime

class DateUtil():
    """description of class"""
    def isDate(string, fuzzy=False): 
        try: 
            parse(string, fuzzy=fuzzy)
            return True
    
        except ValueError:
            return False