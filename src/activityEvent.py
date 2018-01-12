from datetime import datetime
from numbers import Number

class activityEvent(): 
    units=""

    def __init__(self): 
        self.date = datetime.now()
        self.start = datetime.now().strftime('%m/%d/%Y')
        self.units = ['km','mi','h']
    
    @property
    def date(self):                                      return self.__date

    @date.setter
    def date(self, date):
        self.__date = date
    
    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, date):
        self.__start = date

    @property 
    def distance(self): 
        return self.__distance 
    
    @distance.setter 
    def distance(self, distance): 
        if not isinstance(distance, Number):
            raise ValueError("Value is not correct, give positive number")
        if distance < 0: 
            raise ValueError("Value is not correct, give positive number")

    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit):
        if unit in units:                                    self.__unit = unit
        else:
            raise ValueError("Unit is not correct, use km, mi or h.")
    
