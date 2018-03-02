import unittest 
from datetime import datetime
from context import ActivityEvent

class TestActivityEvent(unittest.TestCase):
    
    def test_shouldStoreActivity(self):
        activity = self.createActivityEvent()
        activity.distance = 15.5
        activity.unit = "km"
        activity.type = "cycling"
        self.assertEqual(activity.type, "cycling"," activity type not set correctly")
        self.assertEqual(activity.unit,'km', "unit not set correctly")
        self.assertEqual(activity.distance,15.5,"distance not set cotrectly")

    def createActivityEvent(self):
        types = ["cycling","sleeping","jogging"]
        units = ["km","min"]
        activity = ActivityEvent(types,units)
        return activity

if __name__ == '__main__':     
    unittest.main() 
