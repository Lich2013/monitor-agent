import time

class AgentDaemon:
	def __init__(self):
		self.pidfile_path = '/tmp/agent.pid'
		self.stdin_path = '/dev/null'
		self.stdout_path = '/dev/null'
		self.stderr_path = '/dev/stderr'
		self.pidfile_timeout = 5

	def run(self):
		with open('/tmp/d.txt', 'a') as f:
			while True:
				f.write(str(time.time())+"\n")
				f.flush()
				time.sleep(1)