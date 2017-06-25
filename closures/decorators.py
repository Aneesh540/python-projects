""" Decorators are used to add functionality to functions without changing them
in this module we'll be using functional decorators   """

# Example 1
def decorator_function(original_func):

	def wrapper_function():
		"""return original function with execution"""
		print('wrapper xecte this before {}'.format(original_func))
		return original_func()

	return wrapper_function	


def display():
	print('display function() is running')

decorateddisplay=decorator_function(display)
print('___________________________________\n')
decorateddisplay()
print(decorateddisplay.__name__)
print('+++++++++++++++++++++++++++++++++++')

# Example 2/3	

def taple_func():
	print(" I'am chinu taple")

taple_func=decorator_function(taple_func)
taple_func()
print('________________________________________________________')
taple_func()
print(taple_func.__name__)	

@decorator_function
def foo_n_bar():
	print('wrapper statment xecuteb4 ME bcoz of @decorator_function')	

foo_n_bar()
print(foo_n_bar.__name__)	

#>>>>>>>>>>>>>>>>>> THE CONCLUSION <<<<<<<<<<<<<<<<<<<<<
# adding @decorator_function above a function is equal to 
# function = decorator_function(function)
# see deco-2.py for more info