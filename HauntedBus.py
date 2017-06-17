""" Bus, HauntedBus, TwilightBus 

	This module is frm fluent-python chapter 8
"""


class Bus():
	""" a Bus that picks and drops passenger"""
	def __init__(self,passengers=None):
		if passengers is None:
			self.passengers=[]

		else:
			self.passengers=list(passengers)	
	def pick(self,name):
		""" Picks a passenger"""
		self.passengers.append(name)

	def drop(self,name):
		""" Drops a passenger"""
		try:
			self.passengers.remove(name)
		except:
			print('BUS IS EMPTY')	
	
	def __str__(self):
		return '%s' %(self.passengers)	


class HauntedBus(Bus):
	""" Bus haunted by ghost passengers"""
	def __init__(self,passengers=[]):
		self.passengers=passengers



class TwilightBus(Bus):
	""" a bus that makes passenger vanish"""
	def __init__(self,passengers=None):
		if passengers is None:
			self.passengers=[]
		else:
			self.passengers=passengers			

if __name__ == '__main__':

	print('basic difference bw/n Haunted and Twilight Buses\n')

	haunted_bus1=HauntedBus(['python','java','javascript','ruby'])
	haunted_bus2=HauntedBus()
	haunted_bus3=HauntedBus()
	
	haunted_bus2.pick('golang')
	haunted_bus2.pick('exilir')

	print(haunted_bus2.passengers)
	print(haunted_bus3.passengers)

	haunted_bus3.drop('golang')

	print(haunted_bus2.passengers)
	print(haunted_bus3.passengers)

	print(haunted_bus1)			#to implement __str__ method

	print('this happen bcoz haunted_bus 2&3 share \
	refrence to same list i.e. []\n')

	twilight_bus1=TwilightBus(['python','java','javascript','ruby'])
	twilight_bus2=TwilightBus()
	twilight_bus3=TwilightBus()
	
	twilight_bus2.pick('golang')
	twilight_bus2.pick('exilir')

	print(twilight_bus2.passengers)
	print(twilight_bus3.passengers)

	haunted_bus3.drop('golang')

	print(twilight_bus2.passengers)
	print(twilight_bus3.passengers)

	print('\n >>>>>debugging 2.x<<<<<\n')
	# why all 3 Bus class is deleting members from list 
	# Bus() creates list of passengers then also ISSUE RAISED:::
# for more info go to fluent-python.pdf page 234(b4 garbage colection) 

	foo=Bus(['react js','angular js','vue js'])
	bar=HauntedBus(['backbone js','ember js','express js'])
	spam=TwilightBus(['node js','polymer js','aurelia js'])
	print(foo)
	print(bar)
	print(spam)
	print('\n')
	foo.drop('angular js')
	print(foo)

	bar.drop('ember js')
	print(bar)

	spam.drop('node js')
	print(spam)