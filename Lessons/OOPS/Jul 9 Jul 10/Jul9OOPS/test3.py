class ineuron:
    def student(self):
        print("print details of all students")

    def achievers(self):
        print("print list of all achievers")

    def hall_of_fame(self):
        print("print list of hall of famers")

class ineuron2:
    def student(self):
        print("print details of all students - 2")

class ineuron_vision(ineuron, ineuron2):
    def student(self):
        print("these are filtered student list")

iv = ineuron_vision()
iv.student()