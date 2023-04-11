#Name: Aurelio Siordia
#Date: 09/04/23

#10-1 Learning Python
filename = 'learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()
print(contents)

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.strip())

#10-2 Learning C
with open(filename) as file_object:
    contents = file_object.read()
print(contents.replace('Python', 'C++'))
 
