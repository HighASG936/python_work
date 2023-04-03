#Name: Aurelio Siordia
#Date:02/04/23


#7-1 Rental Car
prompt=input('Let me see if I can find you a Subaru: ')
print(f'{prompt}\n')

#7-2 Restaurant Seating
prompt=input('How many people are in you dinner group?: ')
prompt=int(prompt)
if prompt > 8:
	print("You'll have to wait for a table\n")
else:
	print("You're table is ready\n")

#7-3 Multiples of Ten
prompt=input('Enter a number: ')
prompt=int(prompt)
if prompt % 10 == 0:
	print(f'{prompt} is multiple of ten\n')
else:
	print(f'{prompt} is not multiple of ten\n')

