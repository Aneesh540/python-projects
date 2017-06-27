""" Python > Basic Data Types > Find Second Largest

To print second largest element in given input (2 -2 2 2 :o/p=-2)
"""
input()
print('enter element in one line')


arr=set(map(int,input().split()))
lists=list(arr)
print(lists)
print(arr)
try:
	print(arr[-1])
	print(arr[-2])

except:
	print('TypeError: set is just a type in python you cannot iterate\n')

lists.sort()
if len(lists) is 1:
	print('second largest is',lists[-1])	
else:	
	print('second largest is',lists[-2])	

