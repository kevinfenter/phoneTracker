import phonenumbers

import folium

from target_number import number
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode

Key = 'fc977906701e4209b624cc1015106021'

tgt_nmber = phonenumbers.parse(number)
targetLocation = geocoder.description_for_number(tgt_nmber, "en")
print(targetLocation)

servicer = phonenumbers.parse(number)
targetProvider = carrier.name_for_number(servicer, "en")
print(targetProvider)

geocoder = OpenCageGeocode(Key)

query = str(targetLocation)

results = geocoder.geocode(query)
print(results)

lat = results[0]['geometry']['lat']

lng = results[0]['geometry']['lng']

print(lat, lng)


myMap = folium.Map(location=[lat, lng], zoom_start=9)

folium.Marker([lat, lng], popup=targetLocation).add_to((myMap))

myMap.save("targetLocation.html")
