#Name: Aurelio Siordia
#Date: 18/03/23

world_places=['Paris','Rome','Liverpool','Giza','Machu Pichu']
guest=['other','ramiro', 'sofía', 'carmelo', 'sara']
mystuff=['car','computer','phone','laptop','clock','TV']
#3-8 Seeing the World 

#original list
print(world_places)

#display list alphabetical order
print(sorted(world_places))

#original list
print(world_places)

#display list reverse alphabetical order
print(sorted(world_places,reverse=True))

#original list
print(world_places)

#change list reverse
world_places.reverse()
print(world_places)

#original list
world_places.reverse()
print(world_places)

#sort list alphabetical order and display
world_places.sort()
print(world_places)

#sort list reverse alphabetical order and display
world_places.sort(reverse=True)
print(world_places)

#3-9 Dinner Guests
number_of_guests=len(guest)
print(f"I've intived {number_of_guests} persons")

#3-10 Every function
print(f"{mystuff[0]} is first item")
print(f"{mystuff[-1]} is last item")
print(mystuff)
mystuff[3]="house"
print(mystuff)
mystuff.append("bed")
print(mystuff)
mystuff.insert(4,"Fan")
print(mystuff)
del mystuff[-1]
print(mystuff)
Poped_stuff=mystuff.pop()
print(f"Poped last stuff is {Poped_stuff}" )
Poped_stuff=mystuff.pop(2)
print(f"Poped third stuff is {Poped_stuff}" )
mystuff.remove('computer')
print(mystuff)












