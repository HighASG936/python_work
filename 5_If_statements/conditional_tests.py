#Name: Aurelio Siordia
#Date:25/03/23


#5-1 Conditional Test
car='subaru'
print("Is car == 'subaru'? I predict True")
print(car == 'subaru')
print("Is car == 'audi'? I predict False")
print(car == 'audi')
print()

pizza='anchovies'
print("Is pizza == 'pepperoni'? I predict False")
print(pizza == 'pepperoni')
print("Is pizza == 'anchovies'? I predict True")
print(pizza == 'anchovies')
print()

my_guest='John'
print("Is my guest == 'John'? I predict True")
print(my_guest.lower() == 'john')
print("Is my guest == 'Rebbeca'? I predict True")
print(my_guest.lower() == 'rebecca')
print()

banned_user='Phillip'
print("Is banned user == 'Carl'? I predict False")
print(banned_user.lower() == 'carl')
print("Is my guest == 'Phillip'? I predict True")
print(banned_user.lower() == 'phillip')
print()

next_side='top'
print("Is next side == 'left'? I predict False")
print(next_side == 'left')
print("Is next side == 'top'? I predict True")
print(next_side == 'top')
print()

#5-2 More Conditional Tests

#Test for equality and equality with strings
print('Car is not bmw')
print(car != 'bmw')
print('Car is not subaru')
print(car != 'subaru')
print()

#Using the lower() method
print('Banned User is not Phillip')
print(banned_user.lower() != 'phillip')
print('Banned User is not Steven')
print(banned_user.lower() != 'steven')
print()

#Numerical tests
age_1=43
age_2=38
print(f'{age_1} is equal to {age_2}')
print(age_1 == age_2)
print(f'{age_1} is not equal to {age_2}')
print(age_1 != age_2)
print(f'{age_1} is grater than {age_2}')
print(age_1 > age_2)
print(f'{age_1} is less than {age_2}')
print(age_1 < age_2)
print(f'{age_1} is less than or equal to {age_2}')
print(age_1 >= age_2)
print(f'{age_1} is less than or equal to {age_2}')
print(age_1 <= age_2)
print()

#Using the and keyword and the or keyword
Today_is_windy=True
Today_is_Sunday=False

print("Today is sunny Sunday")
print(Today_is_Sunday and Today_is_windy)

print("Today is Sunday or is a windy day")
print(Today_is_Sunday or Today_is_windy)
print()


#Test whether an item is in a list
good_pets=['dog', 'cat', 'parrot', 'hamster']
print('a lion could make good pet')
print('lion' in good_pets)
print('a cat could make good pet')
print('cat' in good_pets)
print()

#Test whether an item is not in a list
print("a lion couldn't make good pet")
print('lion' not in good_pets)
print("a cat couldn't make good pet")
print('cat' not in good_pets)
print()




















