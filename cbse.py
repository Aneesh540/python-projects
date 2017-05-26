class Mobile:

	price=0
	model='Lumia 1600'

	def __init__(self,price,model):
		
		self.price=int(input('enter price:'))
		self.model=input('enter model:')
		self.price += 5

	def __str__(self):
		print('object is :')	
	def display(self):
		print('{}!model:{}'.format(self.price,self.model))
		
foo=Mobile(35,'lumia 1600')
foo.height='in metres'
foo.display()
z=vars(foo)   	  #disply all attributes
print(z)
del(foo.price)    #delete the attribute price
print(z)
print(Mobile.__init__)
print(Mobile.__doc__)
print(foo)