"""  A closure is a inner function that have access to variables  in 
the local scope in which it was created even after outer function has 
finished execution"""

import logging

def outer_func(msg):
	message=msg

	def inner_func():
		print(message)
		print(msg)

	return inner_func	

hello=outer_func('hello')
hello()


logging.basicConfig(filename='example.log',level=logging.INFO)

def logger(function):

	def log_func(*args):
		logging.info('Running "{}" with arguments {}'.format(function.__name__,args))
		print(function(*args))

	return log_func

def add(x,y):
	return x+y

def sub(x,y):
	return x-y
		
add_logger=logger(add)
sub_logger=logger(sub)

add_logger(3,4)
sub_logger(9,10)
sub_logger(33,-99)	
	










