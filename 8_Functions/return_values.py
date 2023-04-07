#Name: Aurelio Siordia
#Date: 07/04/23

#8-6 City Names
def city_country(name, country):
    text = f'"{name.title()}, {country.title()}"'
    return text

print(city_country('tijuana', 'mexico'))
print(city_country('ottawa', 'canada'))
print(city_country('lodon', 'england'))

# 8-7 Album
def music_album(artist_name, album_title, number_of_songs=None):
    if number_of_songs:
        info={'artist': artist_name.title(), 'album': album_title.upper(), 'number of songs': number_of_songs}
    else:
        info={'artist': artist_name.title(), 'album': album_title.upper() }
    
    return info
    
print(music_album(album_title='the dark side of the moon',artist_name='pink floyd'))
print(music_album(album_title='abbey road',artist_name='the beatles'))
print(music_album(album_title='house of the holy',artist_name='led zeppelin', number_of_songs=8))
print()

# 8-8 User Albums

prompt = 'Put information of album:\n'
prompt += "(enter 'q' to quit)\n"
print(prompt)
while True:    
    name = input('Name of album: ')
    if name == 'q':
        break    
    
    artist = input('Artist: ')
    if artist == 'q':
        break    
    
    number_of_songs = input('Number of songs(optional):')
    if number_of_songs == 'q':
        break            
    
    print(f'{music_album(album_title=name, artist_name=artist, number_of_songs=number_of_songs)}\n')



