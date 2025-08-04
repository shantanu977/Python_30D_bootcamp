from functools import reduce

#Capitalize User Name
name = ["john","alice","bob"]
capital = list(map(lambda n : n.upper(), name))
print(capital)



#Filter_valid Email Address
emails = ["abc@gmail.com", "xyz@yahoo.com", "admin@gmail.com"]
ans = list(filter(lambda mail: "@gmail.com" in mail, emails))
print(ans);




#callculate final price after discount
prices = [100,200,300]
ans = list(map(lambda price : price-(0.10 * price), prices))
print(ans)



#full Name Of Employee
emloyees = [('John' ,'Doe'),('Alice','Smith')]
ans = list(map(lambda name : name[0]+" "+name[1], emloyees))
print(ans);




#prices above 1000
prices = [850,1200,999,1600]
ans = list(filter(lambda price : price > 1000, prices))
print(ans)




#total Marks Of Student
marks = [78,85,90,88]
total = reduce(lambda a,b : a+b, marks)
print("Total : ",total)




#Sort List Of Students By Age
students = [{'name' : 'Meera' , 'age' : 22},{'name' : 'Radha' , 'age' : 20}]
ans = sorted(students, key= lambda student : student['age'])
print(ans)

