from callbacks import Callbacks, on, if_arg_is

import sys

if __name__ == '__main__':
	try:
		if_arg_is('--').do(Callbacks.on_existing_db)
		if_arg_is('++').do(Callbacks.on_new_db)

		on('add').do(Callbacks.on_add)
			
	except Exception as e:
		print(e)