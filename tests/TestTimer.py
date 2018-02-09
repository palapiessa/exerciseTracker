import unittest
from datetime import datetime
from context import Timer

class TestTimer(unittest.TestCase):

    def test_Start(self):
        testStart = self.getCurrentTime()
        timer = Timer
        self.assertEqual(timer().startTime,testStart, "timer start date:" +timer().startTime+" testStart:"+testStart)

    def test_Stop(self):
        timer =Timer
        testStop = self.getCurrentTime() 
        timer.stop()
        self.assertEqual(timer().stopTime,testStop, "timer stop date:" +timer().stopTime+" testStop:"+testStop)

    def test_Duration(self):
        duration = self.getDuration(testStart,testStop)
        self.assertEqual(timer().duration,duration, "timer duration:" +timer().duration+" testDuration:"+duration)
        
    def getCurrentTime(self):
        currentTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return currentTime
    
    def getDuration(self, testStart, testEnd):
        start= datetime.strptime(testStart,"%Y-%m-%d %H:%M:%S")
        end= datetime.strptime(testEnd,"%Y-%m-%d %H:%M:%S")
        elapsed = end - start
        return divmod(elapsed.days * 86400 + elapsed.seconds, 60)

       
if __name__ == '__main__':                           unittest.main()
