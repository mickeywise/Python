from folium import Map, Marker
from geo import Geopoint

#Get latitude and longitude
latitude = 40.7
longitude = -3.7

geopoint = Geopoint(latitude = latitude, longitude, longitude)


#Folium Map Instance
mymap = Map(location = [latitude, longitude])

#Create a Marker instance and add to map
madrid = Marker(location = [40.4, -3.7], popup = "Hi Michael, you're now in Madrid")
madrid.add_to(mymap)

#Save the Map instance into HTML file
mymap.save("Madrid.html")