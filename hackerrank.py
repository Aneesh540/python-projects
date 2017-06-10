""" prblem set: string->sWAP cASE"""

def swap_case(s):
    list(s)
    foo=[]
    for x in list(s):
        if x.isupper():
        	foo.append(x.lower())
        elif x.islower():
        	foo.append(x.upper())	
        else:
        	pass
    print(foo)
    result ''.join(foo)
                 
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
