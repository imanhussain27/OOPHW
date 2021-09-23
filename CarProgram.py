import CarClass

year_model=input("Please enter your car's model year here: ")

make=input("Please enter your car's make here: ")

car=CarClass.Car(year_model, make)

number=5

for n in range(number):
    car.accelerate()
    print("Acceleration Speed: ",car.get_speed())

for x in range(number):
    car.brake()
    print("Brake Speed: ",car.get_speed())

