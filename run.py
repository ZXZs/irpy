from callbacks import Callbacks

import sys

if __name__ == '__main__':
	try:
		if '--' in sys.argv: 
			Callbacks.on_existing_db()
		elif '++' in sys.argv:
			Callbacks.on_new_db()

		if sys.argv[1].lower() == 'add':
			Callbacks.on_add()
			
	except Exception as e:
		print(e)