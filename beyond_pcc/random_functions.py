

# Generating a random number between 0 and 1
from random import random
random_num = random()
print(random_num)



# Generating a random integer
from random import randint
random_int = randint(1, 6)
print(random_int)



# Choosing a random element from a list
from random import choice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
random_player = choice(players)
print(random_player)



# Putting a list in random order.

# This function changes the order of the list, and you can’t get 
# the original order back.

from random import shuffle
players = ['charles', 'martina', 'michael', 'florence', 'eli']
shuffle(players)
print(players)

#If you want to keep the original order, pass a copy of the list 
#to the shuffle() function.

from random import shuffle

players = ['charles', 'martina', 'michael', 'florence', 'eli']

shuffled_players = players[:]
shuffle(shuffled_players)

print(players)
print(shuffled_players)

