import sqlite3
import sys

class Database:
	def __init__(self, name):
		self.name = name
		self.connection = None
		self.cursor = None

	def connect(self):
		self.connection = sqlite3.connect(self.name)
		self.cursor = self.connection.cursor()

	def execute(self, expression):
		self.cursor.execute(expression)

	def commit(self):
		self.connection.commit()

	def disconnect(self):
		self.connection.close()
		self.connection = None
		self.cursor = None