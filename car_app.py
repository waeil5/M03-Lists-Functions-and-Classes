"""
name: Waeil Mikhaeil
Program: Choose car
Date: 4/9/2023
"""

class Vehicle: #create class for vehicle type, contains the types
    def __init__(self,car, truck, plan, boat, broomstick):
        self.car=car
        self.truck = truck
        self.plan=plan
        self.boat=boat
        
class Automobile(Vehicle): # this class will inherit the data of Vehicle class, and also contains the attributes of the car.
    def __init__ (self, year, make, model, doors, roof):
        self.year=year
        self.make=make
        self.model=model
        self.door=doors 
        self.roof=roof

car1 = Automobile("car", "truck", "plan", "boat", "broomstick")
while True: # while loop in case if the user entered an invalid input  will ask him again to enter a valid value.
    print("Enter the type of the car")
    car_type= input("(car, truck, plane, boat, or a broomstick): ")
    if car_type =="car":
        car1.car=car_type
        break
    elif car_type =="truck":
        car1.truck=car_type
        break
    elif car_type =="plan":
        car1.plan=car_type
        break
    elif car_type =="boat":
        car1.boat=car_type
        break
    elif car_type =="broomstick":
        car1.broomstick=car_type
        break
    else:
        print("INVALID Input")
        print()
#will ask the use to enter the attributes of the car
ch=Automobile("year", "make", "model", "door", "roof")
ch.year=input("Enter the year please: ")
ch.make=input("Enter the make please: ")
ch.model=input("Enter the model please: ")
ch.door=input("Do you want (2 or 4) doors?: ")
ch.roof=input("Do you want solid or sun roof?: ")

# after the program gets the values from the user, will print the saved values 
print("Vehicle type: "+ car_type)
print("Year: "+ch.year)
print("Make: "+ch.make)
print("Model: "+ch.model)
print("Number of doors: "+ch.door)
print("Type of roof: "+ch.roof)
