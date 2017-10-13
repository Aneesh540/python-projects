""" Container data types """

import collections

"""
Defaultdict()

Unlike dict, with defaultdict you do not need to check
whether a key is present or not
"""
sentence = "the quick brown fox jumps over the lazy dog."
words = sentence.split(' ')

d = collections.defaultdict(int)
for word in words:
    d[word] += 1

print(d)


"""
OrderedDict()

OrderedDict keeps its entries sorted as
they are initially inserted.
"""
alphabets = collections.OrderedDict([("A", 65), ("D", 68), ("X", 88)])
for key, value in alphabets.items():
    print(key, value)


"""
Counter()

A counter stores elements as dictionary keys,
and their counts are stored as dictionary values
"""
colors = ['blue', 'black', 'green', 'blue', 'pink', 'black',
          'green', 'white', 'black', 'white', 'pink', 'green', 'black']
print(collections.Counter(colors))


"""
Namedtuple()

Namedtuple() creates tuple-like objects
that have fields accessible by attribute lookup
as well as being indexable and iterable
"""
student = collections.namedtuple('Student', ['first', 'last', 'grade'])
student_1 = student('Harry', 'Potter', 'A')
print(student_1.first)
print(student_1.grade)
