import unittest
from context import ActivityProg

class TestActivityProg(unittest.TestCase):
    
    def test_parser(self):
        activityProg = ActivityProg()
        parser = activityProg.parseArgs(['sleep', 'min'])
        self.assertEqual('sleep',parser.type,"Type not parsed correctly")
        self.assertEqual('min',parser.unit,"Unit not parsed correctly")
        parser = activityProg.parseArgs(['cycle', 'km'])
        self.assertEqual('cycle',parser.type,"Type not parsed correctly")
        self.assertEqual('km',parser.unit,"Unit not parsed correctly")
        
if __name__ == '__main__':                                unittest.main()
