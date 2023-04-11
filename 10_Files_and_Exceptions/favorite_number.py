#Name: Aurelio Siordia
#Date: 11/04/23
import json

filename = 'favorite_number.json'
with open(filename) as f:
    favorite_number = json.load(f)
print(favorite_number)

