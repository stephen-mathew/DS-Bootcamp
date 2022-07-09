from test22 import employee
from utils.utils1 import person2 # option 1
# from utils import utils1 # option 2
# import utils.utils1 # options 3

class person1:
    def __init__(self, name, surname, yob):
        self._name = name
        self.__surname = surname
        self.yob = yob


steve = person1("steve","matt",1900)

# print(steve.name) # AttributeError: 'person' object has no attribute 'name'
print(steve._name)
# print(steve.__surname ) # AttributeError: 'person' object has no attribute '__surname'
print(steve._person1__surname )

obj1 = employee()

obj2 = person2("steve2","matt2",1902) # option 1
# obj3 = utils1.person2("steve2","matt2",1902) # option 2
# obj4 = utils.utils1.person2("steve2","matt2",1902) # options 3