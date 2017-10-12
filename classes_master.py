"""use of copy() and deepcopy() for handling previous commit anomoly"""
import copy

class Bus:
    """School Bus which pick and drops passenger in route"""
    def __init__(self,passenger=[]):
        self.passenger=list(passenger)

    def pick(self,name):
        self.passenger.append(name)

    def drop(self,name):
        self.passenger.remove(name)
    
    def __str__(self):
         return '{}'.format(self.passenger)   

def main():
    bus1=Bus(['angular js','React js','Node js','Grunt js'])
    print('bus1:',bus1,'\n')
    bus2=copy.copy(bus1)
    bus3=copy.deepcopy(bus1)

    dopel=bus1

    print('bus1-id:%s\nbus2-id:%s\nbus3-id:%s\nbus4-id:%s' %(id(bus1),id(bus2),id(bus3),id(dopel)))
    print('\nnow removing angular js from bus 1\n')
    bus1.drop('angular js')
    print('bus1:',bus1)
    print('bus2:',bus2)
    print('bus3:',bus3)
    print('dopel:',dopel)

    print('\npicking aurelia js in bus3\n')
    bus3.pick('aurelia js')
    print('bus1:',bus1)
    print('bus2:',bus2)
    print('bus3:',bus3)
    print('dopel:',dopel)

if __name__ == '__main__':
        main()    