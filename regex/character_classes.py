""" 
Part-1: character-classes
Part-2:Caret and Dollar sing
"""

import re

foo=re.compile(r"\d+\s\w+")
# match that which has one or more word, a whitespace, one or more word
bar=foo.findall("2 a ,and,aneesh,333\taneesh , 1\nfoo,917 p ")
print(bar)
#  o/p == ['2 a', '333\taneesh', '1\nfoo', '917 p']


# MAKING UR OWN CHAARACTER CLASS

spam=re.compile(r"[aeiouAEIOU]")
eggs=spam.findall('Robocaps eat human EMPLOYNMENT')
print(eggs)
# o/p ==  ['o', 'o', 'a', 'e', 'a', 'u', 'a', 'E', 'O', 'E']


aneesh=re.compile(r"[0-4.]")
jain=aneesh.findall("1. 2. 3. 4 5 6 78 9 .")
print(jain)
# o/p ==['1', '.', '2', '.', '3', '.', '4', '.']

spam=re.compile(r"[^aeiouAEIOU]")
eggs=spam.findall('Robocaps eat human EMPLOYNMENT')



print(eggs)
print('\n')
print('*'*30,'END OF PART ONE',"*"*30)
print("\n")

# ====================================================================

# r"hello aneesh" matches string that starts with hello aneesh

hello = re.compile(r"^hello aneesh")
world = hello.findall("hello aneesh jain world \nhello aneesh LDrago")
print(world)
# print(world.group())
print('>>>>>>>>>>>>>>>')

# r"\d$" matches string that ends with number

python=re.compile(r"\d$")
golang=python.search("\n4abp 19\n")
print(golang)
print(golang.group())

# r"^\d$" all in string must be decimal



print('*'*30,'END OF PART TWO',"*"*30)
# wildcard(.) character match any thing except new-line
