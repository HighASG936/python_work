#Name: Aurelio Siordia
#Date: 08/04/23

from restaurant import Restaurant as R
import user
from admin import Admin as A

#9-10 Imported Restaurant
restaurant = R('Jolly Joe', 'American food')
restaurant.describe_restaurant('$$', 'Lucca Street')
print()

#9-10 Imported Admin
user_admin = user.Admin('Aurelio', 'Siordia', '30', 'single')
user_admin.privileges.show_privileges()
print()

#9-11 Multiple modules
new_admin = A('Aurelio', 'Siordia', '30', 'single')
new_admin.privileges.show_privileges()

