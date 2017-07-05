"""insertion of an elenent in sorted list in sorted order
	>>>	starting from only element and making a sorted list """

import random

def insert_in_sorted(ele,list):

	
		
	if ele < list[0]:
		list.insert(0,ele)
		
	elif list[len(list)-1] < ele:
		list.append(ele)

	else:	
		for x in range(len(list)):
			if list[x]<= ele <= list[x+1]:
				list.insert(x+1,ele)
				break

		
			

list=[1] 			# coz list=[] gives error 
print('By using random function:')
for _ in range(7):
	foo=random.randrange(-5,21)
	#print(foo)
	insert_in_sorted(foo,list)

	print(foo,'-->',list)



			