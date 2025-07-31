
#Contact form With Optional Fields
def submit_form(name,email, phone = None):
    print(f"Name : {name}")
    print(f"Email : {email}")
    print(f"Phone : {phone}")

submit_form("Ram","ram@gmail.com")
submit_form("Om","ome@gmail.com",1234567890)


#Shopping cart Total with *args
def calculate_prices(*prices):
    return sum(prices)

print(calculate_prices(200,300,300,100,50,50))



#Display book info with **kwargs
def book_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
book_info(title = "Book 1", author = "auth 1", price = 300)



#Multi - Items Billing
price1=100
price2 = 300
price3 = 100
def print_bill(*items):
    return sum(items)

print(print_bill(price1,price2,price3))


#User Setting Handeler
def save_settings(*options):
    for index,setting in enumerate(options):
        for key,value in setting.items():
            print(f"{key} : {value}")
        

save_settings({"theme" : "Dark", "language" : "Englsih"}, {"theme" : "Light", "language" : "French"});