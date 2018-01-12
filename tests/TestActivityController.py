import unittest 
import datetime
from context import activityEvent

class TestActivityController(unittest.TestCase):
    
    def test_ConstructorShouldStoreActivity(self):
        activity = activityEvent
        activity.distance = 15.5
        activity.unit = "km"
        #self.assertEqual(activity.type.description, "cycling"," activity type not set correctly")        self.assertEquals(activity.unit,'km', "unit not set correctly")
        self.assertEqual(activity.distance,15.5,"distance not set cotrectly")
        print("activity start date:" +str(activity().start))
        #print("datetime.date():" + datetime.date())
        #self.assertEquals(activity.date,datetime.date())

if __name__ == '__main__':     
    unittest.main() 
