#Age Validator

class Person:
    def __init__(self):
        self.age = None

    def set_age(self, age):
        if age < 0 or age > 130:
            raise ValueError("Invalid age !")
        self.age = age
        print(f"Age set to {self.age}")

p1 = Person()

try:
    age_input = int(input("Enter age: "))
    p1.set_age(age_input)
except ValueError as e:
    print(f"Error: {e}")


#Assignment 2: Bank Account Withdrawal
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Not enough balance!")
        self.balance -= amount


account = BankAccount(5000)

try:
    account.deposit(1000)
    print("Balance :", account.balance)

    account.withdraw(7000)  
    print("Balance :", account.balance)

except ValueError as e:
    print("Error:", e)


#Assignment 3: Student Grade Input
class Student:
    def __init__(self, marks):
        for m in marks.values():
            if m < 0 or m > 100:
                raise ValueError("Marks must be between 0 and 100")
        self.marks = marks

try:
    s = Student({"Math": 90, "Science": 110})  # Invalid marks
    print(s.marks)
except ValueError as e:
    print("Error:", e)


#Assignment 4: Custom Exception Class
class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if self.balance - amount < 100:
            raise InsufficientBalanceError("Balance below ₹100!")
        self.balance -= amount

try:
    acc = BankAccount(500)
    acc.withdraw(450)
except InsufficientBalanceError as e:
    print("Error:", e)




# # Assignment 5: File Reader Class with Exception Handling

# class FileReader:
#     def read_file(self, filename):
#         try:
#             f = open(filename, 'r')
#             print(f.read())
#             f.close()
#         except FileNotFoundError:
#             print("File not found!")


# fr = FileReader()
# fr.read_file("test.txt")


#Assignment 6: Password Validator
class User:
    def set_password(self, password):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in password):
            raise ValueError("Password must contain at least one number.")
        self.password = password
        print("Password set successfully.")

# Main program
try:
    user = User()
    user.set_password(input("Enter your password: "))
except ValueError as e:
    print("Error:", e)


#Assignment 7: Temperature Converter with Validation
# class Temperature:
#     def __init__(self, celsius):
#         if celsius < -273.15:
#             raise ValueError("Temperature can't be below -273.15°C (absolute zero).")
#         self.celsius = celsius

# try:
#     temp = float(input("Enter temperature in Celsius: "))
#     t = Temperature(temp)
#     print("Temperature is valid:", t.celsius, "°C")
# except ValueError as e:
#     print("Error:", e)




#Assignment 8: Shopping Cart Quantity Check
class ShoppingCart:
    def _init_(self, stock):
        self.stock = stock
    def add_item(self, quantity):
        if quantity > self.stock:
            raise Exception("Quantity exceeds stock")
        print("Item added to cart")

try:
    cart = ShoppingCart(5)
    cart.add_item(10)
except Exception as e:
    print(e)
 



#Assignment 9: Exam Hall Allocation
# class ExamHall:
#     def __init__(self, max_capacity):
#         self.max_capacity = max_capacity
#         self.allocated = 0

#     def allocate_students(self, number):
#         if self.allocated + number > self.max_capacity:
#             raise ValueError(f"Not Enough Space")
#         self.allocated += number
#         print(f"{number} students allocated.\n Total : {self.allocated}")

# try:
#     hall = ExamHall(50)
#     hall.allocate_students(30)
#     hall.allocate_students(25)  
# except ValueError as e:
#     print("Error:", e)


#Assignment 10: Flight Booking Validation

class InvalidAgeError(Exception):
    pass

class FlightBooking:
    def __init__(self, name, age):
        if age < 0 or age > 100:
            raise InvalidAgeError(f"Invalid age: {age}")
        self.name = name
        self.age = age
        print(f"Booking successful")


try:
    booking1 = FlightBooking("Ram", 25)  
    booking2 = FlightBooking("Om", 105)  
except InvalidAgeError as e:
    print("Error:", e)
