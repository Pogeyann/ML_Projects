class vehicle:
    def vehicle_info(self):
        print("inside vehicle class")

class car(vehicle):
    def car_info(self):
        print("inside car class")

cr=car()
cr.car_info()
cr.vehicle_info()