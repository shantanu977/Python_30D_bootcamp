# 1. Inheritance → Vehicle, Car, Bike

class Vehicle:
    def start_engine(self):
        print("Engine started")

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

Car().start_engine()
Bike().start_engine()


# 2. Method Overriding → Shape, Circle, Rectangle

class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

print("Circle area:", Circle(3).area())
print("Rectangle area:", Rectangle(4, 5).area())


# 3. Encapsulation → BankAccount

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amt):
        self.__balance += amt

    def withdraw(self, amt):
        if amt <= self.__balance:
            self.__balance -= amt

    def show(self):
        print("Balance:", self.__balance)

acc = BankAccount()
acc.deposit(1000)
acc.withdraw(200)
acc.show()


# 4. Abstract Class → Appliance → Fan, Light


from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class Fan(Appliance):
    def turn_on(self):
        print("Fan ON")

class Light(Appliance):
    def turn_on(self):
        print("Light ON")

Fan().turn_on()
Light().turn_on()


# 5. Polymorphism (same function different output)

class Teacher:
    def speak(self):
        print("Teacher speaks")

class Student:
    def speak(self):
        print("Student speaks")

class Principal:
    def speak(self):
        print("Principal speaks")

for obj in (Teacher(), Student(), Principal()):
    obj.speak()


# 6. Multilevel Inheritance → Employee → Manager → Director

class Employee:
    def work(self):
        print("Employee working")

class Manager(Employee):
    def manage(self):
        print("Manager managing")

class Director(Manager):
    def guide(self):
        print("Director guiding")

d = Director()
d.work()
d.manage()
d.guide()


# 7. Getter & Setter (private age)
  

class Person:
    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

p = Person(18)
print("Age:", p.get_age())
p.set_age(25)
print("Updated age:", p.get_age())
