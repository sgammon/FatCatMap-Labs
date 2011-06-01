from momentum.fatcatmap.handlers import WebHandler


class Landing(WebHandler):
	
	def get(self):
		return self.render('')
		
		
class AskQuestion(WebHandler):
	
	def get(self):
		return self.render('')


class FAQ(WebHandler):
	
	def get(self):
		return self.render('')
		

class ListTopics(WebHandler):
	
	def get(self):
		return self.render('')
		

class ViewTopic(WebHandler):
	
	def get(self, key):
		return self.render('')
		

class ReportBug(WebHandler):
	
	def get(self):
		return self.render('')