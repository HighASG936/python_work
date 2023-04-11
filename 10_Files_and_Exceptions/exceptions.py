#Name: Aurelio Siordia
#Date: 10/04/23

# 10-6 Addition
print('Enter two numbers to get their addtionn ')

number1 = input("Enter first number: ")
number2 = input("Enter second number: ")

try:
    result = int(number1) + int(number2)
except ValueError:
    print("Please enter valid values\n")
else:
    print(f"Result: {result}\n")


# 10-7 Addition Calculator
print('Enter two numbers to get their addtionn ')
print("(enter 'q' to quit)")

active = True
while active == True:
    number1 = input("Enter first number: ")
    if number1 == 'q':
        active = False
        break
    number2 = input("Enter second number: ")
    if number2 == 'q':
        active = False
        break

    try:
        result = int(number1) + int(number2)
    except ValueError:
        print("Please enter valid values\n")
    else:
        print(f"Result: {result}\n")
print()

# 10-8 Cats and Dogs, 10-9 Silent Cats and Dogs
def read_file(filename):
    """display all content into a file"""
    try:
        with open( filename, encoding='utf-8' ) as f:
            content = f.read()            
    except FileNotFoundError:
        #print(f"Sorry, {filename} doesn't exist\n")
        pass
    else:
        print(content)
        
filename = 'cats.txt'
read_file(filename)

filename = 'dogs.txt'
read_file(filename)

# 10-10 Common Words
filename = "book.txt"
with open(filename, encoding='utf-8') as f:
    lines = f.readlines()

counter = 0
pattern = 'Musketeers'
for line in lines:    
    counter += line.lower().count(pattern.lower())
print(f"'{pattern}' appears {counter} times in {filename}")    

