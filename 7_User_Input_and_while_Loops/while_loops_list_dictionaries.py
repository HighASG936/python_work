# Name: Aurelio Siordia
# Date: 06/04/23

# 7-8 Deli & 7-9 No Pastrami
sandwich_orders = [ 'classic', 'club chicken', 'pastrami',
                    'peanutbutter', 'jelly',
                    'pastrami', 'pastrami' ]
finished_sandwiches = []

print('NOTICE: pastrami is run out!!\n')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
    print(f'I made your {sandwich} sandwich')

print('\nFinished orders: ')
for finished_sandwich in finished_sandwiches:
    print(f'\t{finished_sandwich} sandwich')
print()

# 7-10 Dream Vacation
prompt = 'If you could visit one place in the world,'
prompt += 'where would you go? '
Users={}

while True:        
    name = input('Enter your name: ')
    if name == 'quit' :
        break
    else:
        vacation_place = input(prompt)
        Users[name] = vacation_place
    print()

print('\nResult of polling: ')
for name, place in Users.items():
    print(f'\t{name.title()} would like go to {place.title()}')

        
        
        
        