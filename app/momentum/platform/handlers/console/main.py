from momentum.platform.handlers.console import ConsoleHandler


class Landing(ConsoleHandler):

	def get(self):
		return self.response('<b>Hello Console!</b>')