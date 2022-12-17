import time

print("Hello! I am Bob, the Breakfast Bot.")
time.sleep(2)
print("Today we have two breakfasts available.")
time.sleep(2)
print("The first is waffles with strawberries and whipped cream.")
time.sleep(2)
print("The second is sweet potato pancakes with butter and syrup.")
time.sleep(2)

while True:
    while True:
        response = input("Please place your order. Would you like waffles or pancakes?\n").lower()
        if "waffles" in response:
            print("Waffles it is!")
            time.sleep(2)
            break
        elif "pancakes" in response:
            print("Pancakes it is!")
            time.sleep(2)
            break
        else:
            print("Sorry, I don't understand.")
            time.sleep(2)
            
    print("Your order will be ready shortly.")
    time.sleep(1)
    
    while True:
        order_more = input("Would you like to place another order? Please say 'yes' or 'no'.\n").lower()
        if "no" in order_more:
            print("Ok, goodbye!")
            time.sleep(2)
            break
        elif "yes" in order_more:
            print("Very good, I'm happy to take another order!")
            break
        else: 
            print("Sorry, I don't understand")  
    if "no" in order_more:    
        break

