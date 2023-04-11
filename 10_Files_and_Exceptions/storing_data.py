#Name: Aurelio Siordia
#Date: 11/04/23
import json

#10-11 Favorite Number
filename = 'favorite_number.json'
number = input("What's you favorite number? ")
with open(filename, 'w') as f:
    json.dump(number, f)
#Execute favorite_number.py


#10-12 Favorite Number Remembered
filename = 'favorite_number.json'
try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("What's you favorite number? ")
    with open(filename, 'w') as f:
        json.dump(number, f)
else:
    print(f"Your favorite number is {number}")


#10-13 Verify User
def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name"""
    username = get_stored_username()
    if username:
        reply = input(f"{username} is your correct name?(yes/no)")
        if reply == 'yes':                    
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"Now {username} is your new user name")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()
        
