class Test:

	Weight=89
	Blood_group='B+'
	__BP=None				# Private member
	def __init__(self):
		self.__BP='Hidden attribute'

	def display(self):
		return self.__BP	#only method(known) to print private member 
							#is defining a method like this'''

foo=Test()	

print(foo.Weight)
print(foo.Blood_group)
print(foo.display())	