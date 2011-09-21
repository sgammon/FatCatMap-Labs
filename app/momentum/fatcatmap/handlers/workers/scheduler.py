from momentum.fatcatmap.handlers.workers import Worker


class Main(Worker):
	
	def run(self):
		self.response.write('<b>Scheduler.Main</b>')
	
	
class Tick(Worker):

	def run(self):
		self.response.write('<b>Scheduler.Tick</b>')
	
	
class Callback(Worker):

	def run(self):
		self.response.write('<b>Scheduler.Callback</b>')
	
	
class Next(Worker):

	def run(self):
		self.response.write('<b>Scheduler.Next</b>')
	
	
class Status(Worker):

	def run(self):
		self.response.write('<b>Scheduler.Status</b>')