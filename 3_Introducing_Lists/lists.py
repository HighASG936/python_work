
#Name: Aurelio Siordia
#Date: 15/03/23

friends=['laura', 'rodrigo', 'ricardo', 'gabriela', 'josé']
cars=['honda', 'tesla', 'toyota', 'kia']

#3-1 Names
print(friends[0].title())
print(friends[1].title())
print(friends[2].title())
print(friends[3].title())
print(f'{friends[4].title()}\n')

#3-2 Grettings
print(f'Hello {friends[0].title()}, would you like to learn some Python coding?')
print(f'Hello {friends[1].title()}, would you like to learn some Python coding?')
print(f'Hello {friends[2].title()}, would you like to learn some Python coding?')
print(f'Hello {friends[3].title()}, would you like to learn some Python coding?')
print(f'Hello {friends[4].title()}, would you like to learn some Python coding?\n')

#3-3 Your Own List
print(f'I have a {cars[-1].title()} car and I love it!') #I'm using last item by negative indexes
print(f'I think {cars[-2].title()} is a good brand cars') 
print(f"In the past, I wished a {cars[-3].title()} car, but now not 'cause bad quality")
print(f"I think {cars[-4].title()} cars are very expensive!")

