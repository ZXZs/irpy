from flask import Flask, render_template
from dt import DateTime	
from database import Database

flask = Flask(__name__)

db = None

@flask.route('/')
def index():
	return render_template('index.html')

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
			`timestamp` TEXT NOT NULL 
		)
		""")

	return "OK"

@flask.route('/add/<word1>/<word2>')
def add(word1, word2):
	global db

	word1 = word1.lower()
	word2 = word2.lower()

	db.safe_execute_many([
		f"INSERT INTO words (word1, word2, lvl, timestamp) VALUES (\"{word1}\", \"{word2}\", 1, \"{DateTime.now().__str__()}\");",
		f"INSERT INTO words (word1, word2, lvl, timestamp) VALUES (\"{word2}\", \"{word1}\", 1, \"{DateTime.now().__str__()}\");"
	])

	return "OK"

@flask.route('/repeat')
def repeat():
	return "OK"