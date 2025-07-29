cart = {
    "apple" : 3,
    "banana" : 2,
    "watermelon" : 4
}

prices = {
    "watermelon" : 40,
    "apple" : 20,
    "banana" : 10,
}

total=0
for name,item in cart.items():
    total =total + prices[name] * item

print(total)