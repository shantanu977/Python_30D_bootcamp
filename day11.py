
#Global Counter
count = 0 

def call():
    global count
    count += 1
    print(f"Function called {count} times")

call()
call()


#Update Nested Variable
def out():
    c = 0

    def inner():
        nonlocal c
        c += 1
        print(f"Nested counter: {c}")

    return inner

counter = out()
counter()



# Weather Logger

weather = "sun"  # Global variable

def update(new):
    global weather
    weather = new
    print(f"Weather updated to: {weather}")

update("Cloud")
update("Rain")


#Toggle Dark/Light Theme
theme = "light"

def toggle():
    global theme
    theme = "dark" if theme == "light" else "light"
    print(f"Theme changed to: {theme}")

toggle()
toggle()


# Session Timer 
def session():
    minutes = 0

    def update():
        nonlocal minutes
        minutes += 1
        print(f"Session time: {minutes} minutes")
    
    return update  # Return the inner function


timer = session()

timer()
timer()
timer()

#Task Tracker
done = 0

def add():
    global done
    done += 1
    print(f"Tasks: {done}")

add()
add()

#Wallet System
bal = 1000

def dep(x):
    global bal
    bal += x
    print(f"Bal: {bal}")

def wd(x):
    global bal
    bal = bal - x
    print(f"Bal: {bal}")

dep(2000)
wd(1500)


#Scoreboard Tracker
scr = 0

def add(p):
    global scr
    scr = scr+p
    print(f"Score: {scr}")

add(10)
add(5)

#10. Stock Quantity Manager

stk = {}

def add_s(itm, qty):
    global stk
    stk[itm] = stk.get(itm, 0) + qty

def sell(itm, qty):
    global stk
    if itm in stk and stk[itm] >= qty:
        stk[itm] = stk[itm]- qty

add_s("pen", 10)
sell("pen", 3)
print(stk)
