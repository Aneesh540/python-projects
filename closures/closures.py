"""first class function

function which accept other function as argument and return result 
as a function are called higher order function"""

def square(x):
	return x**2


def cube(x):
	return x**3


def my_map(function, arg_list):
	""" this is map(int,input()) wala function takes function as 1st
	argument and iterate all element of list through that function"""

	result=[function(i) for i in arg_list]
	return result

def logger(message):
	"""____________________________"""

	def log_messenger():
		print("Hello %s, i am log_messenger a inside f(x)\n" % (message))	

	return log_messenger

def html_tag(tag):
	"""Takes a html tag"""

	def wrap_text(message):
		#input('enter message: ')
		 print('<{0}> {1} </{0}>'.format(tag,message))

	return wrap_text

if __name__ == '__main__':
	
	f=square	# assigning function to a variable
				#if we put square() it will xecut,so here it'll not xecute

	print(f)
	#print(f(5))    	# aneesh@ldrago~$ 25

	foo=my_map(cube,[1,2,3,4,5])
	print(foo)
	#print(foo())	# TypeError
	print('^'*45,'\n')

	log_ldrago=logger('LDrago')
	log_ldrago()					#this'll execute statement: 
	print('='*50)


	h1_tag=html_tag('h1')
	print(h1_tag)
	h1_tag('Hello World!')

	print('--'*25)		
	print_line=h1_tag('Hello World!eeee')		
