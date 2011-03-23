from momentum.fatcatmap.handlers import WebHandler


class Index(WebHandler):
	
	def get(self):
		return self.render('dev/index.html')
		
		
class CacheManagement(WebHandler):
	
	def get(self):
		pass
		
		
class RPCConsole(WebHandler):
	
	def get(self):
		return self.render('dev/rpc-console.html')
		
		
class WebShell(WebHandler):
	
	def get(self):
		pass