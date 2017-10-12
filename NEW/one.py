""" 1) implementing __call__ method in BingoCage class
    which gives it a function like properties"""


import random


words = ['pandas', 'numpy', 'matplotlib', 'seaborn', 'Tenserflow', 'Theano']


def reverse(x):
    """Reverse a letter"""
    return x[::-1]


def key_len(x):
    """Sorting a list by their length"""
    return sorted(x, key=len)


def key_reverse(x):
    """Sorting a list by reverse spelling here reverse() f(x) is defined by us
    and key should be a function without execution"""
    return sorted(x, key=reverse)


print(key_reverse(words))
print(sorted(words, key = lambda y:y[::-1]))


# EVEN CLASS INSTANCE CAN BE TREATED AS FUNCTION BY IMPLEMENTING __call__ METHOD
class BingoCage:
    """Giving a random element"""

    def __init__(self, items):
        self.item = list(items)
        random.shuffle(self.item)

    def pick(self):
        try:
            return self.item.pop()
        except:
            raise LookupError("Picking from empty")

    def __call__(self, *args, **kwargs):
        return self.pick()

if __name__ == '__main__':

    foo = BingoCage(range(2, 20, 2))
    print(foo)
    print("see that foo() and foo.pick() act in similar manner")
    print(foo.pick())
    print(foo())
