# coding: utf-8
import psutil


class Network():
    def __init__(self):
        self.input = self.inTraffic
        self.output = self.outTraffic
        self.ifAddrs = [x for x in psutil.net_if_stats()]

    def inTraffic(self):
        return psutil.net_io_counters().bytes_recv

    def outTraffic(self):
        return psutil.net_io_counters().bytes_sent

    def detailTraffic(self):
        return psutil.net_io_counters(pernic=True)
