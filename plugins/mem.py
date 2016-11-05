# coding: utf-8
import psutil


class Mem():
    def __init__(self):
        self.mem = psutil.virtual_memory  # 字节
        self.memSize = self.mem().total
        self.memFree = self.mem().free
        self.memAvailable = self.mem().available  # windows中free == available
        self.memUsed = self.mem().used
        self.memPercent = self.mem().percent
        self.swap = psutil.swap_memory
        self.swapSize = self.swap().total
        self.swapFree = self.swap().free
        self.swapUsed = self.swap().used
        self.swapPercent = self.swap().percent
        self.swapInput = self.swap().sin
        self.swapOutput = self.swap().sout
