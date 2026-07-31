class Animal:
    name = " "
    def ran(self):
        print("I can ran")
class Dog(Animal):
    def display(self):
        print("my name is ", self.name)

ch1=Dog()

ch1.name="german Shephard"

ch1.ran()

ch1.display()