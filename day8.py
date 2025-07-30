# Assignments

# 1. Create a function greet_teacher (name) that greets the teacher by name.

def greet_teacher(name):
    print("Teacher name is",name)
greet_teacher('Rupali')  

# 2. Write a function multiply(a, b) that returns the product.

def multiply(n1,n2):
    return n1 *n2
print("Multiply :",multiply(10,10))

# 3. Write a function to calculate the total price after tax.
def total_price(price, rate):
    tax = price * rate
    total = price + tax
    print("Total Price :",total)
total_price(2000,0.14)

# 4. Define a function to print employee details (name, position, salary).
def student_info(name,position,salary):
    print("Empolyee Name :",name)
    print("Empolyee position :",position)
    print("Empolyee salary :",salary)
student_info('Ram','designer',60000)    


# 5. Write a function to convert Celsius to Fahrenheit.

def converter(temp,unit):
 if(unit == "c"):
    ans = (temp * 9/5) + 32
    print(temp," converted into f : ",ans)
 elif(unit == "f"):
    ans = (temp - 32) * 5/9
    print(temp," converted into c: ",ans)    
 else:
    print("Enter Valid Unit !")

t = int(input("Enter Temprature : "))
u = str(input("Enter Unit c for celcius & for faranahite : "))
converter(t,u)

# 6. Create a function that returns the square of a number.


def square(n1):
    return n1 *n1
n=int(input("Enter the number :"))
print("square:",square(n))

# 7. Write a function that calculates simple interest.

#simple interest
def SI(p,r,t):
    print("simple intrest :",((p*r*t)/100))
SI(100,20,2)  

# 8. Create a function to print a birthday message with name and age.

def birthday(name,age):
    print(f"Happy bithday {name} you are now {age} year old ! " )
birthday('Rupali',19)  

# 9. Write a function to split a bill among friends.
  
def split(total, friends):
    if friends == 0:
        return "Number of friends must be more than 0."
    return total / friends
print("each friend must be pay ",split(2000,4))


# 10. Create a function that converts hours into minutes and seconds.

def convert_hours(hours):
    minutes = hours * 60
    seconds = hours * 3600
    return minutes, seconds
minutes,second =convert_hours(2)

print(f"2 hours is {minutes} minutes or {second} seconds.")