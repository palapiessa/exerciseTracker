from datetime import datetime
from numbers import Number

class activityEvent(): 
    units=""
    types=""

    def __init__(self): 
        self.date = datetime.now()
        self.startTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.units = ['km','mi','h']
        self.types = ["cycling","running","sleep"]

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        if value in types:
            self.__type = value
        else:
            raise ValueError("Type is not correct, use " +str(types))
    
    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date
    
    @property
    def startTime(self):
        return self.__startTime

    @startTime.setter
    def startTime(self, date):
        self.__startTime = date

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
        if unit in units:
            self.__unit = unit
        else:
            raise ValueError("Unit is not correct, use "+str(units))
    
