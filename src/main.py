import sys
from cliff.app import App
from cliff.commandmanager import CommandManager

class ActivityApp(App):

    def __init__(self):
        super(ActivityApp, self).__init__(description="activity tracker app", version="0.1", command_manager=CommandManager("activity.tracker"), deferred_help=True,)

    def initialize_app(self, argv):
        self.LOG.debug("initialize app")
        
    def prepare_to_run_command(self, cmd):
        self.LOG.debug('prepare_to_run_command %s', cmd.__class__.__name__)
    
    def clean_up(self, cmd, result, err):
        self.LOG.debug('clean_up %s', cmd.__class__.__name__)
        if err:
            self.LOG.debug('got an error: %s', err)
            
def main(argv=sys.argv[1:]):
        myapp = ActivityApp()
        return myapp.run(argv) 
    
if __name__ == '__main__': 
    sys.exit(main(sys.argv[1:]))
