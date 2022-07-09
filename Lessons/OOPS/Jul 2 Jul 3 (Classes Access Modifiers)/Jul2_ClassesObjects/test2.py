class Person:
    # pass
    def age(self, current_year, year_of_birth):
        return current_year-year_of_birth

    def email_id_input(self,email_id):
        print("Email ID is: ",email_id)

    def ask_name(self):
        name=input("Input is your name: ")
        return name

    def ask_dob(self):
        dob=input("Input your date of birth: ")
        return dob

steve = Person()
anuj = Person()
sudh = Person()

steve.email_id_input("steve@domain.com")
print(steve.ask_name())

print(anuj.ask_dob())