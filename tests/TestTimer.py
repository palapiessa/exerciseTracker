import unittest
from datetime import datetime
from context import activityEvent

class TestTimer(unittest.TestCase):

    def test_Start(self):
        testStart = self.getCurrentTime()
        timer = Timer
        self.assertEqual(timer().startTime,testStart, "timer start date:" +timer().startTime+" testStart:"+testStart)

    def test_Stop(self):
        timer = Timer
        testStop = self.getCurrentTime() 
        timer.stop()


#  def test_Duration(self):

if __name__ == '__main__':                           unittest.main()
