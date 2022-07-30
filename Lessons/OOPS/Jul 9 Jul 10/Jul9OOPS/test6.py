class ineuron:
    def students(self):
        print('print student details')

class class_type:
    def students(self):
        print('print class type of students')

def test(a,b):
    return a+b

print(test(3,4))
print(test("steve","matt"))

def ineuron_external(a):
    a.students()

i = ineuron()
j=class_type()
ineuron_external(i)
ineuron_external(j)