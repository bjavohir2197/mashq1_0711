class Vehicle:
    def start(self):
        print("Vehicle ishga tushdi")

    def stop(self):
        print("Vehicle to‘xtadi")


class Car(Vehicle):
    def start(self):
        print("Car ishga tushmoqda...")
        super().start() 

    def stop(self):
        print("Car to‘xtamoqda...")
        super().stop() 


my_car = Car()
my_car.start()
my_car.stop()
