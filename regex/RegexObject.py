"""Examples from automate the boring stuff book.pdf

p=re.compile() gives a regex object here p is RegexObject
mo=p.search() here a is MatchObject """

# checking telephone number 0731-2553412
import re

RegexObject=re.compile(r"\d{3}-\d{4}")

string="Hello my phone number is 123-4321267"

MatchObject=RegexObject.search(string)
print(MatchObject.group())
print('\n')

# grouping with parenthesis to detail extract

RegexObject2=re.compile(r"(\d{3})-(\d{3}-\d{4})")

string2="phone no is 073-123-4141 in this string."
MatchObject2=RegexObject2.search(string2)
print(MatchObject2.group(1))
print(MatchObject2.group(2))
print(MatchObject2.group())

print('\n')
# mo.groups() example
print(MatchObject2.groups())

# parenthesis extractction in regex not detailed

foo=re.compile(r"\(\d{3}\)-\d{3}-\d{4}")
bar=foo.search("my ph no with area code id (098)-123-3214")
print(bar.group())

# parenthesis extraction in regex with parenthesis detailed-extraction

foo=re.compile(r"(\(\d{3}\))-(\d{3}-\d{4})")
bar=foo.search("my ph no with area code id (098)-123-3214")

print("{}----->{}".format(bar.group(1),bar.group(2)))
