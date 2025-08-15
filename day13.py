# 1. Person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

p1 = Person("Ram", 25)
p1.display_details()

# 2. Car class
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def full_name(self):
        print(f"{self.brand} {self.model} ({self.year})")

c1 = Car("Toyota", "Fortuner", 2023)
c1.full_name()

# 3. Product class
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"Product: {self.name}, Price: ₹{self.price}")

p2 = Product("Pen", 10)
p3 = Product("Notebook", 50)
p2.display()
p3.display()

# 4. Circle class
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

c = Circle(5)
print("Area of circle:", c.area())

# 5. Fruit class with class variable
class Fruit:
    category = "Fruit"   

    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"Category: {Fruit.category}, Name: {self.name}")

f1 = Fruit("Apple")
f2 = Fruit("Banana")
f1.info()
f2.info()


# 6. Movie class
class Movie:
    def __init__(self, title, rating, genre):
        self.title = title
        self.rating = rating
        self.genre = genre

    def show_info(self):
        print(f"{self.title} ({self.genre}) - Rating: {self.rating}/10")

m = Movie("Inception", 9, "Sci-Fi")
m.show_info()


# 7. Laptop class
class Laptop:
    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price

    def compare_price(self, other):
        if self.price > other.price:
            print(f"{self.brand} laptop is costlier than {other.brand}")
        else:
            print(f"{other.brand} laptop is costlier than {self.brand}")

l1 = Laptop("HP", "8GB", 55000)
l2 = Laptop("Dell", "8GB", 47000)
l1.compare_price(l2)


# 8. Employee class
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount
        print(f"{self.name}'s new salary: ₹{self.salary}")

e = Employee("Rahul", "Developer", 30000)
e.give_raise(5000)


# 9. BankAccount class
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. Remaining balance: ₹{self.balance}")
        else:
            print("Insufficient balance!")

acc = BankAccount("Shantanu", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.withdraw(2000)
