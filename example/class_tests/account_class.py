#creates a class that acts like an account
class Account:

	#init method
	def __init__(self, username, password, information):
		self.username = username
		self.password = password
		self.information = information
		self.loggedin = False

	#method analogous to loging in to an account
	def login(self, username, password):
		if self.username == username:
			if self.password == password:
				self.loggedin = True
		else:
			self.loggedin = False

	#getinformation retrieves information if loggedin
	def getInfo(self):
		if self.loggedin:
			return self.information
		else:
			return "retreval failed"