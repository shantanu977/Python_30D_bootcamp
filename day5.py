# Check Number Positive negetive or zero

# n = int(input("Enter Number: "))

# if(n>0) :
#     print(n," is positive")

# elif(n<0):
#     print(n," is Negetive")
# else:
#     print(n," is zero")


#eligible for license if condition

# age = int(input("Enter Age : "))
# if(age >=18):
#     print("You are Eligible for License")
# else :
#     print("Not Eligible")


#Grade on Marks

# m = int(input("enter marks : "))
# if(m>=90):
#     print("Grade A")
# elif(m>=75 and m<=89):
#     print("Grade B")
# elif(m>=60 and m<=74):
#     print("Grade C")
# else :
#     print("F")
    
#user Login

# is_looged_in = True
# is_admin = False

# if(is_looged_in):
#     if(is_admin):
#         print("Welcome Admin")
    
#     print("Welcome User")
# else:
#     print("Please Login")



# Largest Among 3

# n1 = int(input("Enter n1 : "))
# n2 = int(input("Enter n2 : "))
# n3 = int(input("Enter n3 : "))

# if(n1>n2 and n1>n3):
#     print(n1," is greatest")
# elif(n2>n1 and n2>n3):
#     print(n2," is greatest")
# else:
#     print(n3," is largest")


# even-odd check
# n = int(input("Enter number : "))
# if(n%2==0):
#     print(n," is even")
# else:
#     print(n," is odd")


#login & password check
# pas = str(input("Enter password : "))
# if(pas == "admin123"):
#     print("Access Granted")
# else :
#     print("Access Denied")

#Leap Year Check 

# year = int(input("Enter Year : "))

# if(year % 4 == 0 and year %100 !=0)or (year % 400 == 0):
#     print("Leap Year")
# else:
#     print("Not Leap")


#Temprature Converter

# temp = int(input("Enter Temprature : "))
# unit = str(input("Enter Unit c for celcius & for faranahite : "))

# if(unit == "c"):
#     ans = (temp * 9/5) + 32
#     print(temp," converted into f : ",ans)
# elif(unit == "f"):
#     ans = (temp - 32) * 5/9
#     print(temp," converted into c: ",ans)    
# else:
#     print("Enter Valid Unit !")
    


#rock - papapr - scisor :
# import random

# user = str(input("Enter Your Choice \nrock\npapar\nscisor :"))

# clist = ["rock","papar","scisor"]
# comp = random.choice(clist)

# if((user == "rock" and comp == "scisor") or (user == "papar" and comp == "rock") or (user == "scisor" and comp =="papar")):
#     print("User Wins !")
# elif((comp == "rock" and user == "scisor") or (comp == "papar" and user == "rock") or (comp == "scisor" and user =="papar")):
#     print("Comp Wins")
# elif(user == comp):
#     print("Tiee")
# else :
#     print("Enter Valid Choice !")