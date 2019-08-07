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

	def safe_execute(expression)

if __name__ == '__main__':
	db = Database('db.db')

	if sys.argv[1] == 'add':
		try:
			w1 = sys.argv[2].lower()
			w2 = sys.argv[3].lower()

			db.connect()
			db.execute(f"INSERT INTO words (word1, word2, lvl) VALUES (\"{w1}\", \"{w2}\", 1);")
			db.execute(f"INSERT INTO words (word1, word2, lvl) VALUES (\"{w2}\", \"{w1}\", 1);")
			db.commit()
			db.disconnect()

			print("OK")
		except Exception as e:
			print(e)