"""class for vector *, +, /,- and many others 
    hypot function gives -/x**2 + y**2 i.e. hypotaneous    
"""
from math import hypot,sqrt

class Vector:
    """docstring for Vector class 
        NOTE: len(v) length of vector gives different result 
        i.e. x+y coz here we use different length method
        
    """
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

    def __repr__(self):
        """ instead of <'class' object at 0x7.....>
            it returns this for better user eperience
        """
        return 'Vector(%r,%r)' %(self.x,self.y)

    def __abs__(self):
        return hypot(self.x,self.y)

    def __add__(self,others):
        return Vector(self.x + others.x,self.y+others.y)

    def __mul__(self,scalar):
        return Vector(self.x*scalar,self.y*scalar)

    def __len__(self):
        return (self.x+self.y)

    def __rmul__(self,vector2):
        """vector Multiplication ka magic method
            BUT NOT WORKING """
        return self.x * vector2.x + self.y * vector2.y    

if __name__ == '__main__':
        
    x,y=map(int,input('enter 1st vector v1= ').split())

    v1=Vector(x,y)
    print('\n __repr__',v1) 
    print('__abs__(v1)',abs(v1))
    print('__len__(v1)',len(v1))

    z,w = map(int,input('\n now enter 2st vector v2= ').split())
    v2=Vector(z,w)
    print('v1 +v2',v1+v2)
    #print(v1*v2)
    print('v2 *3 =',v2*3)
    print(abs(v2))
