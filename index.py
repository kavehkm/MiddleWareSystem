# standard
from importlib import import_module
# internal
import settings



def core_func(*args, **kwargs):
	print('core_func executed with args={} + kwargs={}'.format(args, kwargs))



def set_middlewares(func):
	for middleware in reversed(settings.MIDDLEWARES):
		p, m = middleware.rsplit('.', 1)
		mod = import_module(p)
		met = getattr(mod, m)
		func = met(func)
	return func


if __name__ == '__main__':
	args = (1, 2, 3)
	kwargs = {
		'a': 'x',
		'b': 'y',
		'c': 'z'
	}
	set_middlewares(core_func)(*args, **kwargs)
