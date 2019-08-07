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

if __name__ == '__main__':
	try:
		if '--' in sys.argv: 
			db = Database(sys.argv[sys.argv.index('--') + 1])
		elif '++' in sys.argv:
			db = Database(sys.argv[sys.argv.index('++') + 1])
			db.safe_execute("CREATE TABLE `words` ( `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, `word1` TEXT NOT NULL, `word2` TEXT NOT NULL, `lvl` INTEGER NOT NULL )")

		if sys.argv[1].lower() == 'add':
			w1 = sys.argv[2].lower()
			w2 = sys.argv[3].lower()

			db.safe_execute_many([
				f"INSERT INTO words (word1, word2, lvl) VALUES (\"{w1}\", \"{w2}\", 1);",
				f"INSERT INTO words (word1, word2, lvl) VALUES (\"{w2}\", \"{w1}\", 1);"
			])

			print("OK")
	except Exception as e:
		print(e)