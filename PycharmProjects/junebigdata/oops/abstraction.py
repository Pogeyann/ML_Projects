#TO hide irrelevent data/class in order to reduce the complexity
#it enhances application efficiency
class car():
    def mileage(self):
        pass
class tesla(car):
    def mileage(self):
        print("the mileage is 25kmph")
class duster(car):
    def mileage(self):
        print("the mileage is 24kmph")
class renault(car):
    def mileage(self):
        print('the mileage is 27kmph')

t=tesla()
t.mileage()

d=duster()
t.mileage()