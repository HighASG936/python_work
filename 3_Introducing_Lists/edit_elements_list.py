#Name: Aurelio Siordia
#Date: 15/03/23

guest=['other','ramiro', 'sofía', 'carmelo', 'sara']

guest.remove('other') #Remove element by value

#3-4 Guest List
print(f"Hello {guest[0].title()}! You're invited to my dinner tomorrow. See you later!")
print(f"Hi dear {guest[1].title()}! You're invited to my dinner tomorrow. See you later!")
print(f"'Sup {guest[2].title()}! You're invited to my dinner tomorrow. See you!")
print(f"Grettings {guest[3].title()}! You're invited to my dinner tomorrow. See you later!\n")

#3-5 Changing Guest List
print(f"What a shame that {guest[2].title()} won't go to the party :'( .\n")
guest[2]='sebastian'
print(f"Hello {guest[0].title()}! You're invited to my dinner tomorrow.")
print(f"Hi dear {guest[1].title()}! You're invited to my dinner tomorrow.")
print(f"Hey {guest[2].title()}! You're invited to my dinner tomorrow.")
print(f"Grettings {guest[3].title()}! You're invited to my dinner tomorrow.\n")

#3-6 More guest
print("Hi dudes! I just found a bigger dinner table, now more people can go to the party!\n")
guest.insert(0,'Carolina')	#Insert to beginning of list
guest.insert(3,'Roberto')  #Insert to index 3 at list
guest.append('Suzie')  	#Insert to the end of list

print(f"Hey {guest[0].title()}! You're invited to my dinner tomorrow.")
print(f"Hey {guest[1].title()}! You're invited to my dinner tomorrow.")
print(f"Hey {guest[2].title()}! You're invited to my dinner tomorrow.")
print(f"Hey {guest[3].title()}! You're invited to my dinner tomorrow.")
print(f"Hey {guest[4].title()}! You're invited to my dinner tomorrow.")
print(f"Hey {guest[5].title()}! You're invited to my dinner tomorrow.")
print(f"Hey {guest[6].title()}! You're invited to my dinner tomorrow.\n")

#3-7 Shrinking Guest Lists
print("Guys! I'm so sorry :c . The table won't arrive in time for dinner, \n \
so I can invite 2 persons only\n")
print(f"{(guest.pop(3)).title()}, I'm so sorry to I won't invite you :'(")
print(f"{(guest.pop(5)).title()}, I'm so sorry to I won't invite you :'(")
print(f"{(guest.pop(3)).title()}, I'm so sorry to I won't invite you :'(")
print(f"{(guest.pop(2)).title()}, I'm so sorry to I won't invite you :'(")
print(f"{(guest.pop(1)).title()}, I'm so sorry to I won't invite you :'(\n")

print(f"{guest[0].title()}, You're keep invited :D")
print(f"{guest[1].title()}, You're keep invited :D")

del guest[0]
del guest[0]
print(guest)
