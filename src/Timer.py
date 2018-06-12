from datetime import datetime
from numbers import Number

class Timer():
    
    def __init__(self):
        self.startTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     
    def stop(self):
        self.stopTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           
    @property
    def startTime(self):
        return self.__startTime
    
    @startTime.setter
    def startTime(self, date):
        self.__startTime = date

    @property
    def stopTime(self):
        return self.__stopTime
    
    @stopTime.setter
    def stopTime(self, date):
        self.__stopTime = date

    # this will return in format (minutes, seconds)
    def duration(self):
        start= datetime.strptime(self.startTime,"%Y-%m-%d %H:%M:%S")
        end= datetime.strptime(self.stopTime,"%Y-%m-%d %H:%M:%S")
        elapsed = end - start
        return divmod(elapsed.days * 86400 + elapsed.seconds, 60)
