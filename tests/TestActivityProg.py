import unittest
from context import ActivityProg
from ActivityProg import types, units  

class TestActivityProg(unittest.TestCase):
    
    def test_parser(self):
        activityProg = ActivityProg()
        parser = activityProg.parseArgs(['sleep', 'min'])
        self.assertEqual('sleep',parser.type,"Type not parsed correctly")
        self.assertEqual('min',parser.unit,"Unit not parsed correctly")
        parser = activityProg.parseArgs(['cycle', 'km'])
        self.assertEqual('cycle',parser.type,"Type not parsed correctly")
        self.assertEqual('km',parser.unit,"Unit not parsed correctly")
    
    def test_init(self):
        # test allowed event types and units
        self.assertEqual(types,["cycle","sleep","run"],"Type list is not up to date")
        self.assertEqual(units,["km","min"],"unit list is not up to date")

    def test_startEvent(self):
        activityProg = ActivityProg()
        # test timer and activity event are created correctly
        fail

    def test_endEvent(self):
        activityProg = ActivityProg()
        # test timer and activity event has been cleared
        # test DB is called
        fail

if __name__ == '__main__':                                unittest.main()
