#Name: Aurelio Siordia
#Date:26/03/23

#5-8 Hello Admin
usernames=['Gerald', 'Carmen', 'Joseph', 'Clara', 'Stephen','admin','Anna']
for username in usernames:
	if username == 'admin':
		print('Hello admni, would you like to see a status report?')
	else:
		print(f'Hello {username}, thank you for logging in again')
print()

#5-9 No Users
usernames=[]
if usernames:
	for username in usernames:
		if username == 'admin':
			print('Hello admni, would you like to see a status report?')
		else:
			print(f'Hello {username}, thank you for logging in again')
else:
	print('We nned to find some users')
print()

#5-10 Checking Username
current_users=['Gerald', 'Carmen', 'Joseph', 'Clara', 'Stephen','admin','Anna']
new_users=['Carl','carmen','anNa', 'Alfred', 'John']
current_lowercase_users=[]

for current_user  in current_users:
	current_lowercase_users.append(current_user.lower())


for new_user in new_users:
	if new_user.lower() in current_lowercase_users:
		print(f'Please enter a new username')
	else:
		print('This username is available')

#5-10 Ordinals numbers

numbers=[n for n in range(1,10)]
for number in numbers:
	if number == 1:
		number_end = 'st'
	elif number == 2:
		number_end = 'nd'
	elif number == 3:
		number_end = 'rd'
	else:
		number_end = 'th'
	print(f'{number}{number_end}')













