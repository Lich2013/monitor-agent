# coding: utf-8
import psutil


class Disk():
    def __init__(self):
        self.__partitionsList()

    def partitionsList(self):
        return self.partitions

    def partitionsUsage(self):
        for x in self.partitions:
            usage = psutil.disk_usage(x.mountpoint)
            x['total'] = usage.total
            x['used'] = usage.used
            x['free'] = usage.free
            x['percent'] = usage.percent
        return self.partitions

    def partitionsIO(self, perdisk=False):
        self.io = psutil.disk_io_counters(perdisk=perdisk)
        return self.io

    def __partitionsList(self):
        self.partitions = []
        for x in psutil.disk_partitions():
            self.partitions.append({
                'mountpoint': x.mountpoint,
                'device': x.device
            })
