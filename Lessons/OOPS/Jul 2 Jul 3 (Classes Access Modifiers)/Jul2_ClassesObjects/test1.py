class Person :
    # pass
    def __init__(self, name, surname):
        self.name=name
        self.surname=surname

    def __init__(self, name, surname, emaildid, year_of_birth):
        self.name=name
        self.surname=surname
        self.email=emaildid
        self.yob=year_of_birth




    def age(self_var,current_year):
        return current_year-self_var.yob

anuj_var = Person('anuj','bhandari','anuj@gmail.com',1994)
print(anuj_var.name)
print(anuj_var.surname)
print(anuj_var.yob)
print(anuj_var.email)
steve_var = Person('steve','mathew','sm@domain.com',10)
print(steve_var.email)
print(type(steve_var))
print(anuj_var.age(2022))