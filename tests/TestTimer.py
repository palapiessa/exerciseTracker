import unittest
from datetime import datetime
from context import Timer
import time 

class TestTimer(unittest.TestCase):

    def test_Start(self):
        timer = Timer()
        startTime = self.getCurrentTime()
        self.assertEqual(timer.startTime,startTime, "timer start date:" +timer.startTime+" testStart:"+startTime)

    def test_Stop(self):
        timer = Timer()
        time.sleep(2.0)
        stopTime = self.getCurrentTime() 
        timer.stop()
        self.assertEqual(timer.stopTime, stopTime , "timer stop date:" +timer.stopTime+" testStop:"+stopTime) 

    def test_Duration(self):
        timer2 = Timer()
        time.sleep(3.0)
        timer2.stop()
        duration= (0,3)
        self.assertEqual(timer2.duration()[0],duration[0])
        self.assertEqual(timer2.duration()[1],duration[1])

    def getCurrentTime(self):
        currentTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return currentTime
    
if __name__ == '__main__':
    unittest.main()
