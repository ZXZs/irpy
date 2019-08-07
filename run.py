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

if __name__ == '__main__':
	if '--' in sys.argv: 
		db = Database(sys.argv[sys.argv.index('--') + 1])
	elif '++' in sys.argv:
		db = Database(sys.argv[sys.argv.index('++') + 1])
		db.connect()
		db.execute("CREATE TABLE `words` ( `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, `word1` TEXT NOT NULL, `word2` TEXT NOT NULL, `lvl` INTEGER NOT NULL )")
		db.commit()
		db.disconnect()

	if sys.argv[1].lower() == 'add':
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