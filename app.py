from flask import Flask
from flask_cors import CORS
from dt import DateTime	
from database import Database
from json import dumps

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
	global db
	db.connect()
	for i in db.execute("SELECT * FROM words ORDER BY RANDOM() LIMIT 1"): result = i
	db.disconnect()
	return dumps(list(result))

@flask.route('/level_incr/<id>/<lvl>')
def level_incr(id, lvl):
	db.safe_execute(f"UPDATE words SET lvl = {int(lvl) + 1} WHERE id = {int(id)}")
	return "OK"

@flask.route('/level_drop/<id>')
def level_drop(id):
	db.safe_execute(f"UPDATE words SET lvl = 1 WHERE id = {int(id)}")
	return "OK"

if __name__ == '__main__':
    flask.debug = True
    flask.run(host = '0.0.0.0', port=5000)