#Name: Aurelio Siordia
#Date: 02/04/23


#6-7 People
Person1={'first_name': 'stephany',
		'last_name':  'harrison',
		'age': 26,
		'city': 'New York'
		}

Person2={'first_name': 'zoe',
		'last_name':  'mclifter',
		'age': 18,
		'city': 'Wisconsin'
		}

Person3={'first_name': 'gustav',
		'last_name':  'romanivich',
		'age': 35,
		'city': 'moscu'
		}
people=[Person1, Person2, Person3]		

for person in people:
	print(person)


#6-8 Pets	
cat = {'name':'cat',
	   'type':'feline',
	   'owner': 'Zoe',
	  }

dog = {'name':'dog',
	   'type':'canine',
	   'owner': 'Gustav',
  	  }

tursoise = {'name':'turtoise',
	        'type':'reptile',
	        'owner': 'Steven',
	       }	

dove = {'name':'dove',
	    'type':'bird',
	    'owner': 'Carolina',
	   }	

parrot = {'name':'parrot',
	      'type':'bird',
	      'owner': 'Alfred',
	     }	

golden_fish={'name':'golden fish',
	      'type':'fish',
	      'owner': 'Fred',
	     }	

pets=[cat, dog, tursoise, dove, parrot, golden_fish]

print()
for pet in pets:
	print(pet)


#6-9 Favorite Places
favorite_places={'gilbert': ['london', 'paris'],
				 'bill': ['ottawa', 'new york'],
                 'francis': ['madrid'],
                 'ismael': ['Caracas', 'Monterey', 'Machupichu'],
                 }
print()
for person, places in favorite_places.items():
	print(person.title())                 
	for place in places:
		print(f'\t{place.title()}')
	print()


#6-10 Favorite Numbers
favorite_numbers={'catherine':[8,9,7,12],
				  'louis': [78],
				  'carl': [13,28],
				  'william': [24],
				  'max': [8,24,72,98],
                 }	

for person, my_favorite_numbers in favorite_numbers.items():
	print(person.title())
	for favorite_number in my_favorite_numbers:
		print(f'\t{favorite_number}')
	print()


#6-11 & 12 Cities
cities={'guadalajara':{'country':'mexico',
					   'population':'150k',
					   'fact':'here baking off famous "birote salado"',
					  },
		
		'london' : {'country':'england',
					'population':'250k',
					'fact':"here's big ben clock",
				   },
		
		'giza' : {'country':'egypt',
					'population':'80k',
					'fact':"here's great piramids",
				   },				   
	   }

for name, info in cities.items():
	print(name.title())
	for key, value in info.items():
		if key == 'country':
			value = value.title()
		print(f'\t{key}: {value}')
	print()




