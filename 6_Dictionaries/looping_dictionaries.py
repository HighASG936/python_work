#Name: Aurelio Siordia
#Date:30/03/23


#6-4 Glossary 2

glossary={'tuple':'Just like struct at c/c++ but in python',
          'dictionary':'Just like hashes at perl but in python',
          'test statement':'a command that approches to eval expresion',
          'linux':'open source operative system created by Linus Torvals',
          'loop':'feature that permit to surfing around a list or dictionary',
         }
for word, meaninig in glossary.items():
    print(f"{word.title()} - {meaninig}")
print()


#6-5 Rivers 
rivers={'nile': 'egypt',
        'amazon': 'brasil',
        'lerma': 'mexico',
        'ganges': 'india',
       }
for river, country in rivers.items():
    print(f"{river.title()} runs through {country.title()}")
print()

for river in rivers.keys():
    print(river.title())
print()

for country in rivers.values():
    print(country.title())
print()


#6-6 Polling
favorite_lenguage={'jen':'python',
                   'sarah':'c',
                   'edward':'ruby',
                   'phil':'python',
                  }
poll_names=['jen','sarah','carl','edward','steven','phil']

for poll_name in poll_names:
    if poll_name in favorite_lenguage.keys():
        print(f'{poll_name.title()}, thank you for reponse at polling')
    else:
        print(f'{poll_name.title()}, I invite to take poll')
    print()
