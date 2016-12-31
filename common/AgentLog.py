import logging
import os
from . import currenDir
class AgentLog(logging):
    def __init__(self, logFile='tmp.log'):
        logDir = os.path.join(currenDir, "log")
        if not os.path.isdir(logDir):
            try:
                os.mkdir(logDir, 0755)
            except (OSError) as e:
                raise e
        self.logFile = os.path.join(logDir, logFile)
        self.logging = logging
        self.logger = self.logging.getLogger()
        handler = self.logging.FileHandler(filename=self.logFile)
        format = self.logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
        handler.setFormatter(format)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO) #TODO: 从配置中读取
        self.logger.info("Start log the machine status")
