"""How python works and deep and shallow copy"""

foo=[1,[2,3,4],(5,6,7)]
bar=foo

foo.append(100)
print(foo)
print(bar)
# foo and bar are refrence to [1,[2,3,4],(5,6,7)]
#so both will change

chicken = [12,[22,45,78],(123,432,1993)]
rooster=list(chicken)

chicken.append('fooo&baar')
rooster.append('aneeshjain')
rooster[1] += [34,59]
rooster[2] += (234,236)

print(chicken)
print(rooster)

print('+'*50,'\n','+'*50)



