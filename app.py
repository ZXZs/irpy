from flask import Flask
from flask_cors import CORS
from dt import DateTime	
from database import Database

flask = Flask(__name__)
CORS(flask)

db = None

@flask.route('/db/<name>')
def new_db(name):
	global db

	db = Database(name)

	db.safe_execute("""
		CREATE TABLE IF NOT EXISTS `words` ( 
			`id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
			`word1` TEXT NOT NULL, 
			`word2` TEXT NOT NULL, 
			`lvl` INTEGER NOT NULL, 
			`timestamp` TEXT NOT NULL,
			`theme` TEXT NOT NULL
		)
		""")

	return "OK"

@flask.route('/add/<word1>/<word2>/<theme>')
def add(word1, word2, theme):
	global db

	word1 = word1.lower()
	word2 = word2.lower()
	theme = theme.lower()

	db.safe_execute_many([
		f"INSERT INTO words (word1, word2, lvl, timestamp, theme) VALUES (\"{word1}\", \"{word2}\", 1, \"{DateTime.now().__str__()}\", \"{theme}\");",
		f"INSERT INTO words (word1, word2, lvl, timestamp, theme) VALUES (\"{word2}\", \"{word1}\", 1, \"{DateTime.now().__str__()}\", \"{theme}\");"
	])

	return "OK"

@flask.route('/repeat')
def repeat():
	return "OK"