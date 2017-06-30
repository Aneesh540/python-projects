""" dict(**kwargs) to initialize dictionaries

setdefault() takes 2 argument 
1st is key to check for :(values) 
2nd is (:value) to set at that (key:) if (key:) does not exist
CAUTION!! setdefault() is only execute if key is not present in dictionary

Example#2:: frequency counter && word counter"""

special={
	"python":"BitTorrent",
	"java":"Cassandra",
	"go":"Docker",
	"ruby":"Github",
}

# print(special)
print(*special.keys())

inp=input("enter language:")

if inp not in special.keys():
	spe=input("enter technologies abt it:")
	special.setdefault(inp,spe)


print(special.keys(),special.values(),sep='\n')	

print('\n____________example#2__________________\n')

string="""This is a text string for frequency word counter by
aneesh jain 203 aka LDrago location indore time 8-30-42 pm
now this is a suff text string"""

li=string.split()

# print(li)
# string='aneesh'

counter={}

for x in string:
	
	counter.setdefault(x,0)
	# if x in counter.keys(): no need of this statement
	counter[x] += 1

#counter.sort(key=counter.keys())		
# AttributeError has occured 

print(counter)
print('\n\n')

word_counter={}

for x in li:
	word_counter.setdefault(x,0)
	word_counter[x] += 1

print(word_counter)	
