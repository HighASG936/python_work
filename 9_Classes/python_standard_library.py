#Name: Aurelio Siordia
#Date: 08/04/23

import dice as D
from random import choice

#9-13 Dice
dice = D.Dice()
for counter in range (0,10):
    dice.roll_dice(6)
print()

for counter in range (0,10):
    dice.roll_dice(10)
print()

for counter in range (0,10):
    dice.roll_dice(20)
print()    

#9-14 Lottery
characters = ('1', '9', '3', '7', '0', '8', '6', '4', '5', '3', 'f', 'p', 'w',
              't', 'x')
ticket=''
my_ticket = '8p7f'

for counter in range (0,4):
    character = choice(characters)
    ticket += character
print(f'Any ticket matching with {ticket.upper()} wins $10,000\n')

#9-14 Lottery Analysis
ticket=''
a_counter = 0
while my_ticket != ticket:
    ticket=''
    for counter in range (0,4):
        character = choice(characters)
        ticket += character
    a_counter += 1
print(f'You need {a_counter} attempts to win')    
 
#9-15  Python Module of the Week
"""" https://pymotw.com/3/ """
    
    
    
    
    
