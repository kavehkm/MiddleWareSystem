def middle_a(func):
	def _wrapper(*args, **kwargs):
		print('middleware <a> before core excuted')
		func(*args, **kwargs)
		print('middleware <a> after core excuted')
	return _wrapper


def middle_b(func):
	def _wrapper(*args, **kwargs):
		print('middleware <b> before core excuted')
		func(*args, **kwargs)
		print('middleware <b> after core excuted')
	return _wrapper


def middle_c(func):
	def _wrapper(*args, **kwargs):
		print('middleware <c> before core excuted')
		func(*args, **kwargs)
		print('middleware <c> after core excuted')
	return _wrapper


def middle_d(func):
	def _wrapper(*args, **kwargs):
		print('middleware <d> before core excuted')
		func(*args, **kwargs)
		print('middleware <d> after core excuted')
	return _wrapper
