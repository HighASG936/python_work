# Name: Aurelio Siordia
# Date: 06/04/23
import time

# 7-4 Pizza Toppings
active = True
while active:
    topping = input('Enter a topping for your pizza: ')
    if topping == 'quit':
        active = False
    else:
        print(f"We'll add {topping} for your pizza\n")
print()

# 7-5  Movie Tickets
active = True
while active:
    age = input('Enter your age: ')
    if age == 'quit':
        active = False
    else:
        age = int(age)        
        if age < 3:
            price = 0
        elif age <= 12:
            price = 10
        elif age > 12:
            price = 15    
        if price == 0:
            print("You haven't to pay for your ticket, it's FREE\n")
        else:
            print(f'Price for your Ticket: {price}$\n')    

# 7-6 Three Exits
topping=''
while topping != 'quit':
    topping = input('Enter a topping for your pizza: ')
    if topping != 'quit':
        print(f"We'll add {topping} for your pizza\n")
print()

while True:
    age = input('Enter your age: ')
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            price = 0
        elif age <= 12:
            price = 10
        elif age > 12:
            price = 15    
        if price == 0:
            print("You haven't to pay for your ticket, it's FREE\n")
        else:
            print(f'Price for your Ticket: {price}$\n')    

# 7-7 Infinity
times=0
while True:
    print(f'Attemp: {times}')
    time.sleep(1)
    times+=1


    
    