 
 # To understand the difference 
def outer(msg):

	def inner():
		print('inner function xecution %s' % msg)

	return inner

def another_outer(msg):
	
	def another_inner():
		print('inner function xecution %s' %msg)

	return another_inner(),msg
	
print(outer('aneesh jain'))
one=outer('LDrago')

print('pythonastia ___________________________________')

one()

print('_________________________________________________')

another_outer('Hello world')
print(another_outer('foo $ bar'))
# first another_outer('foo $ bar') is xecuted then return None 
natural=another_outer('chinu taple') 

print('{0} ** {1}'.format('natural',natural))

#-----------------------------------------------------------------------
#_____________________________________________________________________

def decorator(func):
	
	def inner():
		bar=func()
		return bar

	return inner
	


def display():
	eggs=input('enter string:')
	return eggs

foo=decorator(display)
print(foo.__name__)
spam=foo()
print(spam)

@decorator
def info(name,age):
	print('your name is-> {0} and age is-> {1}'.format(name,age))

# if we run below statement TypeError is raised  as 
#TypeError: inner() takes 0 positional arguments but 2 were given

#info('aneesh',19)		

# so to overcome above problem we use *args and **kwargs in code
# 2 EXAMLES class decorator and functional decorator

def functional_decorator(original_func):

	def inner_wrapper(*args,**kwargs):
		

		print('inner_wrapper xecuted b4 {}'.format(original_func.__name__))

		return original_func(*args,**kwargs)

	return inner_wrapper	

class class_decorator():
	"""similar to functional_decorator just class representation of decorator"""
	def __init__(self, original_func):
		self.original_func = original_func
		
	def __call__(self,*args,**kwargs):

		print('inner_wrapper(class wala) xecuted b4 {}'.format(self.original_func.__name__))

		return self.original_func(*args,**kwargs)


@functional_decorator
def porifera(ex1,ex2):
		print('I have body full of pores ::{} & {}'.format(ex1,ex2))

@class_decorator
def coelenterata(ex1,ex2):
	print('I have hollow body :: {} & {}'.format(ex1,ex2))

porifera('hylonema','sponge')
coelenterata('portuguese man of war','jelly fish')	

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#NEW!!  NEW!!  NEW!!  NEW!!  NEW!!  NEW!!  NEW!!  NEW!!  NEW!!  NEW!!  

#NEW!!  NEW!!  NEW!!  NEW!!  NEW!!  NEW!!  NEW!!  NEW!!  NEW!!  NEW!!  
	
def execution_timer(original_func):
	import time
	
	def wrapper(*args,**kwargs):
		t1=time.time()
		result=original_func(*args,**kwargs)
		t2=time.time() -t1
		
		print('{} run in: {} sec'.format(original_func,t2))

		return result

	return wrapper


import time

# This is how rank info is added functionality of timer 
# without affecting it's code
@execution_timer
def rank_info(usrname,rank):
	time.sleep(2)
	# keep waiting for 2 seconds
	print('stone paper %s,%s' % (usrname,rank))

rank_info('LDrago','1234')	
