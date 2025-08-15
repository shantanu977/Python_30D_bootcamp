# Assignment 1
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"{self.title} by {self.author}"
    def __repr__(self):
        return f"Book('{self.title}','{self.author}')"

b1 = Book("A", "X")
b2 = Book("B", "Y")
l = [b1, b2]
print(b1)
print(l)


# Assignment 2
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __str__(self):
        return f"({self.x},{self.y})"

v1 = Vector(1,2)
v2 = Vector(3,4)
v3 = v1 + v2
print(v3)


# Assignment 3
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __gt__(self, other):
        return self.salary > other.salary

e1 = Employee("A",20000)
e2 = Employee("B",15000)
print(e1 > e2)



# Assignment 4
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return f"{self.name}-{self.price}"

class Cart:
    def __init__(self):
        self.items = []
    def __add__(self, item):
        self.items.append(item)
        return self
    def __len__(self):
        return len(self.items)
    def __str__(self):
        return "\n".join(str(i) for i in self.items)

c = Cart()
c = c + Item("Pen",10)
c = c + Item("Book",50)
print(len(c))
print(c)
