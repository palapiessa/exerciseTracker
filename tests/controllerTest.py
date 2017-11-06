import unittest 

class ValueTest(unittest.TestCase):

    def testConstructorShouldStoreValue(self):         
        activityItem = ActivityItem()
        self.assertEquals(value.value, 6,             "value attribute not set correctl")

if __name__ == '__main__':    
    unittest.main()
