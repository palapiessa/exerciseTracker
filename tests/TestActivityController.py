import unittest 
from datetime import datetime
from context import activityEvent

class TestActivityController(unittest.TestCase):
    
    def test_ConstructorShouldStoreActivity(self):
        testStart = self.getCurrentTime()
        activity = activityEvent
        activity.distance = 15.5
        activity.unit = "km"
        activity.type = "cycling"
        self.assertEqual(activity.type, "cycling"," activity type not set correctly")
        self.assertEqual(activity.unit,'km', "unit not set correctly")
        self.assertEqual(activity.distance,15.5,"distance not set cotrectly")
        self.assertEqual(activity().startTime,testStart, "activity start date:" +activity().startTime+" testStart:"+testStart)
    
    def getCurrentTime(self):
        currentTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return currentTime

if __name__ == '__main__':     
    unittest.main() 
