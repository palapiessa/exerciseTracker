from numbers import Number

class ActivityEvent(): 
    units=""
    types=""

    def __init__(self, types, units): 
        self.units = units
        self.types = types


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        if value in self.types:
            self.__type = value
        else:
            raise ValueError("Type is not correct, use " +str(types))
    
    @property 
    def distance(self): 
        return self.__distance 
    
    @distance.setter 
    def distance(self, value): 
        if not isinstance(value, Number):
            raise ValueError("Value is not correct, give positive number")
        elif value < 0: 
            raise ValueError("Value is not correct, give positive number")
        else:
            self.__distance = value

    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit):
        if unit in self.units:
            self.__unit = unit
        else:
            raise ValueError("Unit is not correct, use "+str(units))
    
