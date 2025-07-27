# Ask the user to enter two numbers and an operation (+, -, *, /)
# Perform the operation and print the result

# n1 = int(input("Enter num 1 : "))
# n2 = int(input("Enter num 1 : "))

# print(f"{n1} + {n2} : {n1+n2}")
# print(f"{n1} - {n2} : {n1-n2}")
# print(f"{n1} * {n2} : {n1*n2}")
# print(f"{n1} / {n2} : {n1/n2}")


# Take two numbers from the user
# Compare them using all comparison operators and show results

# n1 = int(input("Enter num 1 : "))
# n2 = int(input("Enter num 1 : "))

# print(f"{n1} > {n2} : {n1>n2}")
# print(f"{n1} < {n2} : {n1<n2}")
# print(f"{n1} >= {n2} : {n1>=n2}")
# print(f"{n1} <= {n2} : {n1<=n2}")
# print(f"{n1} == {n2} : {n1==n2}")
# print(f"{n1} != {n2} : {n1!=2}")

                                                   

# Input age and country from the user
# Use and / or to check eligibility (e.g., age > 18 and country == "India")

# age = int(input("Enter Age : "))
# country = str(input("Enter Country : "))

# if(country == "india" and age >=18):
#     print("You are indian citizen & you can vote !")
 
# else :
#     print("you can't vote")



# Assignment 4: Membership Game
# Create a list of favorite colors
# Ask the user to input a color
# Check if it's in the list

# colors = ["red","yellow","green","blue","black","white"]

# color = str(input("Enter Your favourite color : "))

# print("Is your color present in list : ",color in colors)


# Try bitwise operations on small numbers and print their binary representations using bin()

# n1 =  3
# n2 = 2

# print(f"{n1} & {n2} : {bin(n1 & n2)}")
# print(f"{n1} | {n2} : {bin(n1 | n2)}")
# print(f"{n1} ^ {n2} : {bin(n1 ^ n2)}")
# print(f"~{n2} : {bin(~n2)}")
# print(f"{n1} >> 1 : {bin(n1>>1)}")
# print(f"{n1} << 1 : {bin(n1<<1)}")


# Ask the user for a number.
# Use the modulus operator (%) to find out if it's even or odd.
# If number % 2 == 0, it's even; else, it's odd.

# n = int(input("Enter A Number : "))

# if(n%2==0):
#     print(f"{n} is Even")
# else :
#     print(f"{n} is Odd")


# Take two numbers from the user: a and b.
# Swap their values using arithmetic operators (+, -).
# Display the new values of a and b.

# a = int(input("Enter value of a : "))
# b = int(input("Enter value of b : "))

# a = a ^ b
# b = a ^ b
# a = a ^ b

# print("a After Swapping : ",a)
# print("b After Swapping : ",b)


# Take user’s age and citizenship status.
# Use comparison (>=) and logical (and) operators.
# Print whether the user is eligible to vote (age >= 18 and citizen = "yes").

# age = int(input("Enter Age : "))
# citizenship = bool(input("Statetrue or false you are citizen of india or not : "))

# if(age >=18 and citizenship == True):
#     print("you can vote ")
# else :
#     print("You can't vote !")

# Create two lists with the same values and compare them using:
# == (checks if values are equal),
# is (checks if both refer to the same object).
# Show how they can be different.

# list1 = [1,2,3,4,5]
# list2 = [1,2,3,4,5]

# print("list1 == list2 : ",list1 == list2) # true because values are same 
# print("list1 is list2 : ",list1 is list2) # Flase Because they don't belong to same memory location



# Start with a number.
# Apply various assignment operators step-by-step:
# +=, -=, *=, /=, %=
# Print the result after each operation to observe the changes.

# base = int(input("Enter Base Number : "))
# n = int(input("Enter Number for Opeartions  : "))

# print("Base number : ",base)

# base+=n
# print(base," += ",n," : ",base)
# base-=n
# print(base," -= ",n," : ",base)
# base*=n
# print(base," *= ",n," : ",base)
# base/=n
# print(base," /= ",n," : ",base)
# base%=n
# print(base," %= ",n," : ",base)