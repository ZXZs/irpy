from database import Database

import sys

class Callbacks:
	def on_existing_db():
		global db
		db = Database(sys.argv[sys.argv.index('--') + 1])

	def on_new_db():
		global db
		db = Database(sys.argv[sys.argv.index('++') + 1])
		db.safe_execute("CREATE TABLE `words` ( `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, `word1` TEXT NOT NULL, `word2` TEXT NOT NULL, `lvl` INTEGER NOT NULL )")

	def on_add():
		global db

		w1 = sys.argv[2].lower()
		w2 = sys.argv[3].lower()

		db.safe_execute_many([
			f"INSERT INTO words (word1, word2, lvl) VALUES (\"{w1}\", \"{w2}\", 1);",
			f"INSERT INTO words (word1, word2, lvl) VALUES (\"{w2}\", \"{w1}\", 1);"
		])

		print("OK")