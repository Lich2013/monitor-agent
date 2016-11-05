# coding: utf-8
import psutil


class CPU():
    def __init__(self):
        self.__interval = 1  # todo 从配置读取间隔时间
        self.cpuLogicalCount = psutil.cpu_count()
        self.cpuPhysicalCount = psutil.cpu_count(logical=False)  # 子机热扩容获取到的没更新怎么搞?
        self.cpuUsageTotal = self.cpuUsagePercent

    def cpuUsagePercent(self, interval=None):
        interval = interval if interval is not None else self.__interval
        self.cpuUsageDetail = psutil.cpu_percent(interval=interval, percpu=True)
        return sum(self.cpuUsageDetail)

    def cpuTimesPerCent(self, percpu=False):
        return psutil.cpu_times_percent(percpu=percpu)
