#Name: Aurelio Siordia
#Date: 07/04/23

# 8-3 T-Shirt
def make_shirt(size, text='I love Python'):
    summary = 'Summary of your shirt:\n'
    summary += f'\tSize: {size.upper()}\n'
    summary += f'\tText: {text}\n'
    print(summary)
    
make_shirt('xl', '"I love you"')

# 8-4 Large shirts
make_shirt(size='l')
make_shirt('m')
make_shirt(size='s', text = 'WTF?')

#8-5 Cities
def describe_city(name, country='mexico'):
    print(f'{name.title()} is in {country.title()}\n')
    
describe_city('guadalajara')
describe_city('Chicago','USA')
describe_city('Moterey')