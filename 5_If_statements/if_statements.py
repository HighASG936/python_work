#Name: Aurelio Siordia
#Date:26/03/23

#5-3 Alien Colors #1
alien_color = 'green'	 #red, yellow
if alien_color == 'green':
	print('You just earned 5 points')

alien_color = 'red'
if alien_color == 'green':
	print('You just earned 5 points')
print()

#5-4 Alien Colors #2
alien_color = 'green'
if alien_color == 'green':
	print('You just earned 5 points')
else:
	print('You just earned 10 points')

alien_color = 'yellow'
if alien_color == 'green':
	print('You just earned 5 points')
else:
	print('You just earned 10 points')
print()

#5-5 Alien Colors #3
alien_color='green'
if alien_color == 'green':
	print('You just earned 5 points')
elif alien_color == 'yellow':	
	print('You just earned 10 points')
elif alien_color == 'red':
	print('You just earned 15 points')

alien_color='yellow'
if alien_color == 'green':
	print('You just earned 5 points')
elif alien_color == 'yellow':	
	print('You just earned 10 points')
elif alien_color == 'red':
	print('You just earned 15 points')

alien_color='red'
if alien_color == 'green':
	print('You just earned 5 points')
elif alien_color == 'yellow':	
	print('You just earned 10 points')
elif alien_color == 'red':
	print('You just earned 15 points')
print()

#5-6 Stages of Life
age = 65
if age < 2:
	print('This person is a baby')
elif age < 4:
	print('this person is a toddler')
elif age < 13:
	print('this person is a kid')
elif age < 20:
	print('this person is a teenager')
elif age < 65:
	print('this person is an adult')
elif age  >= 65:
	print('this person is an elder')	
print()

#5-7 Favorite Fruit
favorite_fruits=['strawberry', 'watermelon', 'pineapple']

if 'strawberry' in favorite_fruits:
	print('You really like strawberries')

if 'banana' in favorite_fruits:
	print('You really like bananas')

if 'watermelon' in favorite_fruits:
	print('You really like watermelon')

if 'apple' in favorite_fruits:
	print('You really like apples')

if 'pineapple' in favorite_fruits:
	print('You really like pineapples')
