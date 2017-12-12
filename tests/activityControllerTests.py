import unittest 
import datetime
from .context import activityEvent

class activityControllerTest(unittest.TestCase):
    def testConstructorShouldStoreActivity(self):         
        activity = activityEvent()
        activity.distance = 15.5
        activity.unit = "km"

        self.assertEquals(activity.type.description, 'cycling'," activity type not set correctly") 
        self.assertEquals(activity.unit,'km', "unit not set correctly")
        self.assertEquals(activity.distance,15.5,"distance not set cotrectly")
        self.assertEquals(activity.date,datetime.date())

    if __name__ == '__main__':     
        unittest.main() 
