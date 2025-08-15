# Assignment 1
playlist = ["a", "b", "c", "d", "e"]
playlist.append("f")
playlist.append("g")
playlist.insert(1, "x")
playlist.remove("c")
playlist.reverse()
print(playlist)

# Assignment 2
scores = [50, 90, 85, 60, 95, 70, 80]
scores.sort()
print(scores)
scores.sort(reverse=True)
print(scores)
count = 0
for s in scores:
    if s > 80:
        count += 1
print(count)

# Assignment 3
countries = ("India", "Japan", "Italy", "USA", "UK")
c1, c2, c3, c4, c5 = countries
print(c1, c2, c3, c4, c5)

# Assignment 4
employees = ["a", "b", "c"]
employees.extend(["d", "e", "f"])
print(employees.index("e"))
print(employees.pop(2))
print(employees)

# Assignment 5
prices = [10, 20, 30, 40, 50, 60]
print(max(prices))
print(min(prices))
print(sum(prices)/len(prices))
prices.clear()
print(prices)

# Assignment 6
temps = (10, 20, 30, 40, 50, 60, 70)
print(temps[5:7])
print(30 in temps)

# Assignment 7
cart = ["pen", "book", "pencil", "eraser", "scale"]
cart.extend(["bag", "box", "bottle"])
cart.sort()
copy_cart = cart.copy()
cart.clear()
print(copy_cart)
print(cart)
