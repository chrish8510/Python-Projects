# note to self: all italian regions and city names are in italian and not in English
# create a mapping of region to abbreviation
regions = {
    'Lazio': 'LAZ',
    'Lombardia': 'LOM',
    'Campania': 'CAM',
    'Sicilia': 'SIC', 
    'Toscana': 'TOS'
}

# create a basic set of regions and some cities in them
cities = {
    'CAM': 'Napoli',
    'TOS': 'Firenze',
    'LOM': 'Milano'
}

# add some more cities
cities['SIC'] = 'Palermo'
cities['LAZ'] = 'Roma'

# print out some cities
print ("SIC Region has: ", cities['SIC'])
print ("LAZ Region has: ", cities['LAZ'])

# print some regions
print ("\n")
print ("Toscana's abbreviation is: ", regions ['Toscana'])
print ("Lombardia's abbreviation is: ", regions ['Lombardia'])

# do it by using the region then cities dict
print ("\n")
print ("Toscana has: ", cities[regions['Toscana']])
print ("Lombardia has: ", cities[regions['Lombardia']])


# print every region abbreviation
print ("\n")
for region, abbrev in regions.items():
    print ("%s is abbreviated %s" % (region, abbrev))

   
# print every city in region
print ("\n")
for abbrev, city in cities.items():
    print ("%s has the city %s" % (abbrev, city))
    
# now do both at the same time
print ("\n")
for region, abbrev in regions.items():
    print ("%s region is abbreviated %s and has city %s" % (region, abbrev, cities[abbrev]))
    
# safely get an abbreviation by region that might not be there
print ("\n")
region = regions.get('Veneto', None)

if not region:
    print ("Sorry, no Veneto.")
    
# get a city with a default values
print ("\n")
city = cities.get('VEN', 'Does not exist')
print ("The city for the region 'VEN' is: %s" % city)

