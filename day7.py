#Create a tuple of 5 favorite movies and print each one using a loop.

favorite_movies = ("Dangal", "3 Idiots", "PK", "Bajrangi Bhaijaan", "Bajirao-Mastani")

for movie in favorite_movies:
    print(movie)



#Create a list of fruits and print each fruit with its index.
fruits = ["apple", "banana", "mango", "orange", "grapes"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")


#Create a dictionary of 3 students and their grades. Print: “Student: Grade” format.
students = {
    "Ram": "A",
    "Om": "B+",
    "Prem": "A-"
}

for name, grade in students.items():
    print(f"{name}: {grade}")




#Create a dictionary with countries as keys and capitals as values. Print only the capitals.
countries = {
    "India": "Delhi",
    "France": "Paris",
    "Japan": "Tokyo",
}

for capital in countries.values():
    print(capital)



#Create a set of animal names and print each one.
animals = {"lion", "tiger", "elephant", "giraffe", "zebra"}

for a in animals:
    print(a)


# Create a dictionary of products and their prices. Print only the product names

products = {"Pen": 10, "Notebook": 40, "Eraser": 5}

for name in products.keys():
    print(name)


#Print the first 10 even numbers using a loop and range().

for i in range(0,11,2):
    print(i)
    

#Create a dictionary of students where each value is another dictionary with details (age and grade). Print each student's name and grade.

students = {
    "Ram": {"age": 14, "grade": "A"},
    "Om": {"age": 15, "grade": "B+"},
    "Prem": {"age": 13, "grade": "A-"}
}

for name, details in students.items():
    print(f"{name}: {details['grade']}")


#Take a user input string and print each character on a new line.
text = input("Enter a string: ")

for ch in text:
    print(ch)

#Display a menu of food items with numbering for user selection.

menu = ["Pizza", "Burger", "Pasta", "Salad"]

for index,food in enumerate(menu):
    print(f"{index} : {food}")