""" Multidimensional vector class 
 AND POLYMORPHISM i.e many forms
v = Vector(5)      			# construction a vector of dimension 5
v[1] = 3					# <0,23,0,0,0> based on use of __setitem__
print(v[4])					# through __getitem__
u = v + v 					# through __add__
TO Do :-> __mul__ method
"""

class Vector:
	"""Represent a multidimensional vector in space"""

	def __init__(self, dimension):
		"""Creates a specified dimension vetor space of 0 element"""
		print(type(dimension))
		
		self.coordinates = [0]*dimension

		# elif type(dimension) is list:
		# # 	self.coordinates = dimension
		# else:	
		# 	self.coordinates=list(dimension)

	def __len__(self):
		"""Returns dimension of vector"""
		return len(self.coordinates)

	def __getitem__(self,i):
		"""Return value of i(th) coordinate"""
		return self.coordinates[i]

	def __setitem__(self,i,value):
		"""Set v[i] = value"""
		self.coordinates[i] = value

	def __add__(self,other):
		""" adding 2 vectors and returning a new vector"""

		if len(self.coordinates) is len(other):
			new_vector=Vector(len(self.coordinates))
			for j in range(len(other)):
				new_vector[j] = self.coordinates[j] + other[j]

			return new_vector
		raise ValueError("Dimension must match")

	def __eq__(self,other):
		""" Sythetic Sugar of =="""

		return self.coordinates == other

	def __ne__(self,other):
		""" Synthetic Sugar of != """

		return not self.coordinates == other

	def __str__(self):
		""" sTRING Representation of vector"""

		return '< '+str(self.coordinates)[1:-1] + '>'

