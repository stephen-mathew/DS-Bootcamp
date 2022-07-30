class ineuron:
    __students = "data science"
    __students1 = "data analytics"

    def students(self):
        print("print the class of students",ineuron.__students)
        print("print the class of students", self.__students1)

i = ineuron()
i.students()
print(i._ineuron__students)


list()