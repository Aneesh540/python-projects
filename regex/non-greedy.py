"""
"foo{3,5}" WILL MATCH LONGEST POSSIBLE STRING BCOZ PYTHON REGEX ARE
GREEDY BY DEFAULT
"""
import re

# GREEDY REGEX
foo=re.compile(r'foo{3,5}')
bar=foo.search('fooooofoofoofoo')
print(bar.group())

# NON-GREEDY REGEX this'll match only 3 

protozoa=re.compile(r"(mollusca-){3,5}?")
porifera=protozoa.search("mollusca-mollusca-mollusca-mollusca-mollusca-")
print(porifera.group())

# findall() willl return a list of all matching
spam=re.compile(r"\d{3}-\d{3}-\d{4}")
eggs=spam.findall("office 211-123-3333 and work:is 999-888-7777")
print(eggs)

# findall() with parenthesis

# BUG BUG BUG BUG BUG BUG BUG BUG 
# why second number is not in cephalochordate list :(

uro_chordate=re.compile(r"(\d{3})?-(\d{3}-\d{4})")
cephalochordate=uro_chordate.findall('121-333-5555 snd 123-9898')
print(cephalochordate)
