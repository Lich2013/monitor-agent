#! /usr/bin/env python
# encoding:utf-8
from daemon import runner
from common.AgentDaemon import AgentDaemon

if __name__ == "__main__":
    d = AgentDaemon()
    dd = runner.DaemonRunner(d)
    dd.do_action()
