""" Operator and functools"""

from operator import mul,itemgetter
from functools import reduce


def factorial(n):
     print(reduce(lambda x,y:x*y, range(1,n+1)))


def fact(n):
    print(reduce(mul,range(1,n+1)))


analysis = [
    ('Shundi_BKL', 8.7, 'Rawat','16ucs083'),
    ('Gaurang', 5.9, 'Kota', '16ucs066'),
    ('Aneesh', 7.5, "Kota", '16ucs036'),
    ('Paritosh', 7, "Gurgaon",'16ucs124')
]

def star(n):
    return (sorted(analysis, key=itemgetter(n)))

print(*star(1), sep=' || ')
print(*star(3), sep=' || ')
