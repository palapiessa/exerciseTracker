import argparse 

types = ["cycle","sleep","run"] 
units = ["km","min"]

class ActivityProg():

    def parseArgs(self,args):
        parser = argparse.ArgumentParser() 
        parser.add_argument("type",help="type of the activity",choices=types) 
        parser.add_argument("unit",default="min", help="measured unit eg. min",choices=units)
        return parser.parse_args(args)


