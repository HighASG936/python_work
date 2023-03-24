#Name: Aurelio Siordia
#Date: 22/03/23


#4-10 Slices
pizzas=['pepperoni','pineapple','vegetenian','meat','classic','fish','italian']

print(f"the first three are {pizzas[:3]}")
print(f"3th to 5th are {pizzas[2:6]}")
print(f"the last three are {pizzas[-3:]}\n")


#4-11 My pizzas, your pizza
pizzas=['pepperoni','pineapple','vegetenian']
friend_pizzas=pizzas[:]

pizzas.append('classical')
friend_pizzas.append('fish')

print(f"My favorite pizzas are {pizzas}")
for my_pizza in pizzas:
    print(my_pizza)
print("\n")
print(f"My favorite pizzas are {friend_pizzas}")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
print("\n")

#4-12 More loops
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
for my_food in my_foods:
    print(my_food)

print("\nMy fried's favorite foods are:")
print(friend_foods)
for friend_food in friend_foods:
    print(friend_food)



