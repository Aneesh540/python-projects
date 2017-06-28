"""How to extract data from Fraction class(is is not callable) but 
	__mul__ method is defined 

>>> Fractions(1,2)*Fractions(3,4)
>>> Fractions(3,8)	
>>> print(Fraction(6,8))
>>> 3/4
>>> t=Fraction(1,2)
>>> t.numerator
>>> 1
>>> t.denominator
>>> 2
"""


from fractions import Fraction
from functools import reduce

def product(fracs):
    t=reduce(lambda x,y:x*y , fracs)
# now t is a instance of Fraction bcoz recude'll return a single class
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))

    print(fracs)
    
    result = product(fracs)

    print(*result)
    # x=1,2,3,4
    # print(*x) prints all value in one line
    # 1 2 3 4 
