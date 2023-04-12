#Name: Aurelio Siordia
#Date: 11/04/23


def city_country(city, country, population=''):
    if population:
        m_population = f" - population {population}"
    else:
        m_population = ''    
    return(f"{city.title()}, {country.title()}{m_population}")

#print(city_country('santiago', 'chile', '507296'))

