# Assignment 1
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1 & set2)
print(set1 - set2)
print(set1 | set2)

# Assignment 2
phonebook = {"A": "111", "B": "222"}
phonebook["C"] = "333"
phonebook["A"] = "999"
del phonebook["B"]
name = input("Enter name: ")
print(phonebook.get(name, "Not found"))

# Assignment 3
ops = {
    "add": lambda x, y: x + y,
    "sub": lambda x, y: x - y,
    "mul": lambda x, y: x * y,
    "div": lambda x, y: x / y
}
o = input("Operation: ")
a = float(input("A: "))
b = float(input("B: "))
print(ops[o](a, b))

# Assignment 4
text = input("Enter paragraph: ")
words = text.split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
print(sorted_freq)

# Assignment 5
capitals = {"India": "New Delhi", "USA": "Washington", "Japan": "Tokyo"}
country = input("Country: ")
if country in capitals:
    print(capitals[country])
else:
    cap = input("Enter capital: ")
    capitals[country] = cap
print(capitals)

# Assignment 6
my_friends = {"A", "B", "C", "D"}
your_friends = {"C", "D", "E", "F"}
print(my_friends & your_friends)
print(my_friends - your_friends)
print(your_friends - my_friends)

# Assignment 7
def add():
    print("Item Added")
def view():
    print("Viewing Items")
def exit_program():
    print("Exiting")

menu = {1: add, 2: view, 3: exit_program}
choice = int(input("1:Add 2:View 3:Exit : "))
menu[choice]()
