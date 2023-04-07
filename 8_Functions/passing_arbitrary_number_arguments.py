#Name: Aurelio Siordia
#07/04/23

#8-12 Sandwiches
def sandwiches(*ingredients):
    """Display a summary of ingredients on sandwich"""
    print('Sandwich ingredients: ')
    for ingredient in ingredients:
        print(f'\t- {ingredient}')
    print()

sandwiches('hammon', 'cheesse')
sandwiches('chicken', 'cheesse', 'lettuce', 'tomate')
sandwiches('peanutbutter', 'jelly', 'nuts')


#8-13 User Profile
def build_profile(first, last, **user_info):
    """Build a dictionary containing we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile(
        'aurelio',
        'siordia',
        city='guadalajara',
        age=30,
        school='CETI Colomos',
        favorite_lengauge='Python'
        )
print(user_profile)
print()


#8-14 Cars
def make_car(manufacturer, model, **info_car):
    """Display manufacturer, model and other info of a car"""
    info_car['manufacturer'] = manufacturer
    info_car['model'] = model
    return info_car
    

car = make_car('FORTE', 'KIA', color='red', age_model='2020', owner='Aurelio')
print(car)
    
    
    
        
        
        