""" 
NOTE!!: using () in regualr expression (in re.compile(r"") )
enables .groups() method which gives us tuple of .....

A) pipe (yes|no) symbol this or that matching it match "yes" or "no"

B) optional matching with ( ? )  0 or 1 time occurence

C) matching 0 or more same thing with star 

D) matching 1 or more with ( + )
"""

import re

osRegex=re.compile(r"ubuntu|fedora")
osUbuntu=osRegex.search("ubuntu is more popular then fedora")
osFedora=osRegex.search('fedora is less popular then ubuntu')

# which occur first is returned

print(osUbuntu,osUbuntu.group())
print(osFedora,osFedora.group())
print('\n')
# ======================================================================

# if u want to search a word which have sone commmon string
# this could bone with parenthesis

py=re.compile(r"(IronPy|CPy|PyPi|Jy)thon")
mode=py.search("IronPython is .net python version")
print(mode.group())
print(mode.group(1))

mode=py.search("JVM running python is Jython ")
print(mode.group())
print(mode.group(1))

# ==================================================================
# Using ? (occure 0 or 1 time)

foo=re.compile(r"(\d{3}-)?\d{3}-\d{4}")
#() will extract 121- type of string && that we can use.group(1) to see it

bar=foo.search("my phone number is 203-1313")
print(bar.group())

bar=foo.search("my phone number is 121-111-2222")
print(bar.group())
print(bar.group(1))
print(bar.groups())
# if we use r"(\d{3}-)?(\d{3}-\d{4})" 
# then 2nd bracket of tuple is also filled

# ==================================================================

spam=re.compile(r"ubuntu (16.04\*)* version")

eggs=spam.search("I'am using ubuntu version in my computer")
print(eggs is None )

eggs=spam.search("I'am using ubuntu 16.04* version in my computer")
print(eggs.group(),eggs.group(1))

eggs=spam.search("I'am using ubuntu 16.04*16.04*16.04* versioncomputer")
print(eggs.group())
print(eggs.group(1))

# =================================================================
# matches 1 or more gives error if beek does not appear

tuna=re.compile(r"buk(beek)+buk")
fish=tuna.search("beast bukbeekbuk in harry potter")
print(fish.group())

fish=tuna.search("beast 'bukbeekbeekbuk' in harry potter")
print(fish.group())
