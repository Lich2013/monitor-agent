# coding: utf-8
import psutil
import time
import platform
class base:
    def __init__(self):
        self.getOS()
        self.boottime = psutil.boot_time()
        self.cpuArchitecture = platform.machine()
    def getOS(self):
        name = platform.uname()
        self.kernel = name[0] + ' ' + name[2]
        if name[0] == 'Linux':
            dist = platform.dist()
            self.os = dist[0] + ' ' + dist[1] + ' ' + dist[2]
        elif name[0] == 'Darwin':
            osVersion = platform.mac_ver()
            if osVersion[0] >= '10.12':
                self.os = 'MacOS ' + osVersion[0]
            elif osVersion[0] < '10.12':
                self.os = 'OS X ' + osVersion[0]
            else:
                self.os = 'unknown'
        else:
            self.os = 'win'
    def bootTime(self):
        start = psutil.boot_time()
        self.uptime = time.time() - self.boottime
        return start