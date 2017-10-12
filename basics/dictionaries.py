""" example from book automate-boring-stuff 

dict() is used to convert into dictionary
basic dictionaries command keys(),get('.',default),values()
1. dictonaries are not iterable i.e. you cannot traverse through it
"""

distros_version={
	"ubuntu":17.04,
	"fedora": 26,
	"debian":9,
	"redhat":7,
	"suse linux":12,
}

print(distros_version)

flavour=input("enter distros whose version is to find:")

if flavour in distros_version:
	print(distros_version[flavour])

else:
	print("version is not in database")
	print("enter version")

	distros_version[flavour]=float(input())

print(distros_version)	

# keys() and values() of dictionaries(modified)
print(*distros_version.keys(),sep=", ")
print(*distros_version.values(),sep=", ")

# printing new modified dictionary
print(distros_version)

print('\nlatest version of input({}):'.format(flavour)\
,distros_version.get(flavour,' :( not is db'))

# setdefault() method and sonal gigi word counting question
# in new file setdefaultPP.py
