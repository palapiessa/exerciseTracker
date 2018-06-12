import argparse 
import sys
from cmd import Cmd

this = sys.modules[__name__]
this.types = ["cycle","sleep","run"] 
this.units = ["km","min"]


class ActivityProg(Cmd):

    def parseArgs(self,args):
        parser = argparse.ArgumentParser() 
        parser.add_argument("type",help="type of the activity",choices=this.types) 
        parser.add_argument("unit",default="min", help="measured unit eg. min",choices=this.units)
        return parser.parse_args(args)

    def do_start(self, args):
        """Start an activity. Give activity type as argument. Only one activity can be started per time."""
        print("start")

    def do_stop(self, args):
        """Stop current activity and save activity data."""
        print("stop")

    def do_quit(self, args):
        """Quits the program.""" 
        print("Quitting.")
        raise SystemExit
 
if __name__ == '__main__':
    prompt = ActivityProg()
    prompt.prompt = '> '
    prompt.cmdloop("Starting activity logging")
