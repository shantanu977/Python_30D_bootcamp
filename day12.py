# # Safe Calculator

# n1 = int(input("Enter Number 1 : "))
# n2 = int(input("Enter Number 2 : "))

# try:
#     ans = n1/n2
#     print(ans)
# except ValueError :
#     print("Somwthing Went Wrong")
# except ZeroDivisionError:
#     print("Zero Division")
# finally:
#     print("Division Done")
    
# # File Reader with Exception

# file = str(input("Enter File Name : "))
# try :
#     f = open(file,"r")
#     content = f.read()
# except FileNotFoundError :
#     print("Not Found")



# # 3. Student Marks Entry

# try :
#     m = int(input("Enter Marks for Student : "))
#     if m>100 or m<0:
#         raise ValueError("Invalid Marks")
#     print(f"Entered Marks : {m}")
# except ValueError as e:
#     print(e)


# # 4. Login Attempt Checker

# users = {
#     "shantanu": "123",
#     "ram": "012",
# }

# username = input("Enter your username: ")
# password = input("Enter your password: ")

# try:
#     if users[username] == password:
#         print("Login successful!")
#     else:
#         print("Incorrect password.")
# except KeyError:
#     print("Username not found. Please check or register.")


# 5. Bank Withdrawal Program

# bal = 10000

# try :
#     m = int(input("Enter amount to wathdraw : "))
#     if m >bal :
#         raise ValueError("Invaid Amount !")
#     else :
#         bal = bal -m
#         print(f"Balance : {bal}")
# except ValueError as e :
#     print(e)




# 6. List Index Access

colors =["red","green","blue","yellow"]

print("Colous : ",colors)

try :
    index = int(input("Enter Index To Display Element : "))
    print(f"Elemnet at {index} : {colors[index]}")
except IndexError:
    print("Invaild Index")
    

# 7. Division with Finally Block

n1 = int(input("Enter Number 1 : "))
n2 = int(input("Enter Number 2 : "))

try:
    ans = n1/n2
    print(ans)
except ValueError :
    print("Somwthing Went Wrong")
except ZeroDivisionError:
    print("Zero Division")
finally:
    print("Thanks For Using Calculator")                        
