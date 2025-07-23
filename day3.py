#Create variables to store your name, age, and whether you're a student (bool).

name = str(input("Enter Name : "))
age = int(input("Enter Age : "))
isStudent = bool(input("State True if You Are A student else false :"))

print("Name : ",name)
print("Age : ",age)
print("Student Or Not : ",isStudent)



#Print out the type of each variable.

name = "Ram"
age = 20
isStudent = False
percentage = 90.45
marks = {"physics" : 98, "maths" : 92, "Chemistry " : 91}
print(type(name))
print(type(age))
print(type(isStudent))
print(type(percentage))
print(type(marks))


# Convert a string number (e.g., "45") to an integer and add 10.

s = input("Enter a number: ") 
result = int(s) + 10
print("Result:", result)


# Try converting a float to an integer and print the result.
f = float(input("Enter Float : "))
print("You Entered : ",f)

num = int(f)
print("After Conversion in Integer : ",num)

#Use **type()** to check the type of a variable after type conversion.

value = input("Enter value : ")

try :
    i = int(value)
    print("After Converting Integer : ",i)
    print(type(i))
except :
    print("Can't Converted into Integer")

try :
    f = float(value)
    print("After Converting Float : ",f)
    print(type(f))
except :
    print("Can't Converted into Float")
    
    
s = str(value)
print("After Converting String : ",s)
print(type(s))
