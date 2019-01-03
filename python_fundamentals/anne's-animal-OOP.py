class Animal:
    def __init__(self, name):
        self.name= name
        self.health = 100
    def walk(self):
        self.health-=1
        return self
    def run(self):
        self.health-=5
        return self
    def displayHealth(self):
        print(self.health)

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.health = 150
    def pet(self):
        self.health+=5
        return self

class Dragon(Animal):
    def __init__(self, name,speed):
        super().__init__(name)
        self.health = 170
        self.speed = speed;
    def fly(self):
        self.health-=10
        return self
    def displayHealth(self):
        super().displayHealth()
        print('I am a Dragon')

test = Dragon("Anne",10000)
test.displayHealth()
print(test.speed)