from callbacks import Callbacks, on, if_arg_is
from app import App

if __name__ == '__main__':
	try:
		app = App()

		if_arg_is('--').do(lambda: Callbacks.on_existing_db(app))
		if_arg_is('++').do(lambda: Callbacks.on_new_db(app))

		on('add').do(lambda: Callbacks.on_add(app))
		on('repeat').do(lambda: Callbacks.on_repeat(app))
			
	except Exception as e:
		print(e)