class car:
    def __init__(self, body,engine,tyre):
        self.body=body
        self.engine=engine
        self.tyre=tyre

    def mileage(self):
        print('Mileage of this car')

class tata(car):
    pass

c = car("solid","v6","radial")
print(c)

t = tata("solid","v8","radial")
print(t)

print(t.mileage())
