import time
import datetime

from plugins.cpu import CPU
from plugins.mem import Mem


class AgentDaemon:
    def __init__(self):
        self.pidfile_path = '/tmp/agent.pid'
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/null'
        self.stderr_path = '/dev/stderr'
        self.pidfile_timeout = 5

    def run(self):
        cpu = CPU()
        mem = Mem()
        with open('/tmp/log.txt', 'a') as f:
            while True:
                log = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") +' [info] '
                log +=  ' cpu: ' + str(cpu.cpuUsagePercent()) + '%'
                log +=  ' mem used percent: ' + str(mem.memPercent) + '%'
                f.write( log + "\n")
                f.flush()
                time.sleep(1)
