import psutil
from config.config import Config

class ProcessWatcher():
    def __init__(self):
        self.processList = Config.config['processes']

    def checkProcessSurvive(self):
        for x in psutil.process_iter():
            if x.name() in self.processList:
                self.processList.remove(x.name())
        if len(self.processList) > 0 :
            return self.processList
        return True
