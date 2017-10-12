class Person(object):
    """
    A simple class to explain the 
    __setattr__ and __getattr__
    """
    def __init__(self):
        self.name = 'Mark'
        self.age = '35'
        self.address = {'State': 'California', 'City': 'Los Angeles',
                        'Postal': '90002'}

    def __setattr__(self, k, v):
        """
        Automatically called when an attribute assignment
        is attempted
        """
        self.__dict__[k] = v

    def __getattr__(self, attr):
        """
        Automatically called when the attribute name isaccessed
        and when the object has no such attribute
        """
        if attr == 'details':
            for x,y in self.__dict__.iteritems():
                print x,y
        else:
            raise AttributeError


if __name__ == '__main__':
    person = Person()
    print "Name", person.name
    print "Age", person.age
    try:
        print person.occupation # will throw an attribute error
    except:
        import traceback
        print traceback.format_exc()
    person.occupation = 'Musician'
    print "Address", person.address
    print "Occupation", person.occupation # no error will be thrown
