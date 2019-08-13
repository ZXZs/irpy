import sqlite3

class Database:
	def __init__(self, name):
		self.name = name
		self.connection = None
		self.cursor = None

	def connect(self):
		self.connection = sqlite3.connect(self.name)
		self.cursor = self.connection.cursor()

	def execute(self, expression):
		return self.cursor.execute(expression)

	def commit(self):
		self.connection.commit()

	def disconnect(self):
		self.connection.close()
		self.connection = None
		self.cursor = None

	def execute_many(self, expressions):
		for expression in expressions:
			self.execute(expression)

	def safe_execute_many(self, expressions):
		self.connect()
		self.execute_many(expressions)
		self.commit()
		self.disconnect()

	def safe_execute(self, expression):
		self.connect()
		self.execute(expression)
		self.commit()
		self.disconnect()