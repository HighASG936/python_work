
person_name="Aurelio Siordia"
famous_person="Albert Einsten"

#2-3 Personal Message
print(f"Hello {person_name}, would you like to lear Python today")

#2-4 Name Cases
print(person_name.lower())
print(person_name.upper())
print(person_name.title())

#2-5 Famous Quote
print('Albert Einsten once said,"A person who never made a mistake never tried anythong new"')

#2-6 Famous Quote 2
message=f'{famous_person} once said,"A person who never made a mistake never tried anythong new"'
print(message)

#2-7 Stripping Names
person_name="\n \tAurelio Siordia \t\t\n"
print(person_name)
print(person_name.rstrip())
print(person_name.lstrip())
print(person_name.strip())