#Name: Aurelio Siordia
#Date: 09/04/23

#10-3 Guest
active = True
filename = 'guest.txt'
print("(Enter 'q' to quit)")
while active:
    user_name = input("Enter User Name: ")
    if user_name != 'q':
        with open(filename, 'w') as file_object:
            file_object.write(f"{user_name}\n")                        
    else:
        active = False
print()

#10-4 Guest Book
active = True
filename = 'guest_book.txt'     
while active:
    user_name = input("Enter User Name: ")
    if user_name != 'q':
        with open(filename, 'a') as file_object:
            print(f"\tWelcome {user_name}\n")
            file_object.write(f"{user_name}\n")                        
    else:
        active = False
print()

#10-5 Programming Poll
active = True
filename = 'responses.txt'     
while active:
    response = input("Why do you like programming? ")
    if response != 'q':
        with open(filename, 'a') as file_object:
            file_object.write(f"{response}\n")                        
    else:
        active = False
        

