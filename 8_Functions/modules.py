#Name: Aurelio Siordia
#07/04/23
import printing_functions as pf
from make_shirt import *
import city_country
from user import build_profile
from car import make_car as mc


#8-15 Printing Models
unprinted_designs=['phone case', 'robot pendant', 'dodecahedron']
completed_desings=[]

pf.print_models(unprinted_designs, completed_desings)
pf.show_completed_models(completed_desings)
print()


#8-16 Imports
make_shirt('xl', 'Highway to hell')
print(city_country.city_country('madrid','Spain'))
user_profile = build_profile(
        'aurelio',
        'siordia',
        city='guadalajara',
        age=30,
        school='CETI Colomos',
        favorite_lengauge='Python'
        )
print(user_profile)
car = mc('FORTE', 'KIA', color='red', age_model='2020', owner='Aurelio')
print(car)

