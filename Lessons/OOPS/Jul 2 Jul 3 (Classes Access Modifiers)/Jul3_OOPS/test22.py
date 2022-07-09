

class person:
    _name = "steve"
    __surname = "matt"
    yob = 2000

    def _age(self,current_year):
        return current_year-self.yob #if self is not used with yob, it will thrown an Attribute error
    def __age1(self,current_year):
        return current_year-self.yob

class employee(person):
    _name = "steve1"
    __surname = "matt1"
    yob = 2001

obj1 = employee()

