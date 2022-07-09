import test1

class person:
    _name = "steve"
    __surname = "matt"
    yob = 2000

    def _age(self,current_year):
        return current_year-self.yob #if self is not used with yob, it will thrown an Attribute error
    def __age1(self,current_year):
        return current_year-self.yob

obj = person()
print(obj)
print(obj._name)
print(obj._age(2022))
print(obj._person__age1(2022))

class employee(person):
    _name = "steve1"
    __surname = "matt1"
    yob = 2001

obj1 = employee()
print(obj1)
print(obj1.yob)
print(obj1._name)
print(obj1._person__surname)
print(obj1._employee__surname) # will throw error unless defined in the child class

print(obj1._age(2022)) # will used the employee class's yob value
print(obj1._person__age1(2022)) # will used the employee class's yob value

# Using code from another file
steve = test1.person1("steve","matt",1900)
print(steve._name)
print(steve._person1__surname )