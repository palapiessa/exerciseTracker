import unittest 

class activityControllerTest(unittest.TestCase):
    def testConstructorShouldStoreActivity(self):         
        activity = Activity('20170101',1,1,24.5)
        self.assertEquals(activity.type.description, 'cycling'," activity type not set correctly") 
        self.assertEquals(activity.unit,'km', "unit not set correctly")
        self.assertEquals(activity.distance,24.5,"distance not set cotrectly")
        self.assertEquals(activity.date,
    if __name__ == '__main__':     
        unittest.main() 
