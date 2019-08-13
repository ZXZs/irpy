from database import Database
from dt import DateTime
import sys

class Event:
	def __init__(self, name, arg):
		self.name  = name
		self.arg = arg

	def do(self, callback):
		if self.name:
			if sys.argv[1].lower() == self.name:
				callback()
		elif self.arg:
			if self.arg in sys.argv:
				callback()

def on(name):
	return Event(name, False)

def if_arg_is(arg):
	return Event(False, arg)

class Callbacks:
	def on_existing_db(app):
		app.db = Database(sys.argv[sys.argv.index('--') + 1])

	def on_new_db(app):
		app.db = Database(sys.argv[sys.argv.index('++') + 1])
		app.db.safe_execute("CREATE TABLE `words` ( `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, `word1` TEXT NOT NULL, `word2` TEXT NOT NULL, `lvl` INTEGER NOT NULL, `timestamp` TEXT NOT NULL )")

	def on_add(app):
		w1 = sys.argv[2].lower()
		w2 = sys.argv[3].lower()

		app.db.safe_execute_many([
			f"INSERT INTO words (word1, word2, lvl, timestamp) VALUES (\"{w1}\", \"{w2}\", 1, \"{DateTime.now().__str__()}\");",
			f"INSERT INTO words (word1, word2, lvl, timestamp) VALUES (\"{w2}\", \"{w1}\", 1, \"{DateTime.now().__str__()}\");"
		])

		print("OK")