#Name: Aurelio Siordia
#Date:20/03/23


#4-3 Counting to Twenty
for number in range(1,21):
	print(number)
print("\n")


#4-4 One Million
list_of_numbers=[]
for number in range(1,1_000_001):
	list_of_numbers.append(number)

for number in list_of_numbers:
	print(number)
print("\n")


#4-5 Summing a Million
list_of_numbers=[]
for number in range(1,1_000_001):
	list_of_numbers.append(number)
print(min(list_of_numbers))
print(max(list_of_numbers))
print(sum(list_of_numbers))
print("\n")


#4-6 Odd Numbers
list_of_numbers=[]
for number in range(1,21,2):
	list_of_numbers.append(number)
for number in list_of_numbers:
	print(number)
print("\n")


#4-7 Threes
list_of_numbers=[]
for number in range(3,31):
	list_of_numbers.append(number*3)
for number in list_of_numbers:
	print(number)	
print("\n")


#4-8 Cubes
list_of_numbers=[]
for number in range(1,11):
	list_of_numbers.append(number**3)
for number in list_of_numbers:
	print(number)	
print("\n")

#4-9 Cube Comprehension
list_of_numbers=[number**3 for number in range(1,11)]
print(list_of_numbers)










