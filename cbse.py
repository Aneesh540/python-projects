""" a static method in pyhton is a method that does not obey
	the usual convection in which self, an instance of the class 
	is first argument to the method

	it is just like any other method of class but canbe called without
	creating the instance of the class
	@staticmethod is convection for using it."""

class Test:
	@staticmethod
	def display(x):
		return x*x

bar=Test()
print(bar.display(5))

