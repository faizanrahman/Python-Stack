# Create a class called Car

class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax()

    def tax(self):
        if (self.price > 10000):
            self.tax =  0.15
        else:
            self.tax = 0.12
        return self.tax
        
        

    def display_all(self):
        print(self.price)
        print(self.speed)
        print(self.fuel)
        print(self.mileage)
        print(self.tax)


car1 = Car(2000, "100mph", "Not Full", "15mpg")
#car1.tax()
car2 = Car(5000, "110mph", "Full", "20mpg")
car3 = Car(8000, "120mph", "Not Full", "25mpg")
car4 = Car(11000, "130mph", "Full", "30mpg")
car5 = Car(13000, "140mph", "Not Full", "35mpg")
car6 = Car(30000, "150mph", "Full", "40mpg")
#print(car1.tax)
#print(car1.price)
car1.display_all()
#car2.display_all()
#car3.display_all()
#car4.display_all()
#car5.display_all()
#car6.display_all()