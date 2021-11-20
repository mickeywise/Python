from folium import Map, Marker, Popup
from geo import Geopoint

#Get latitude and longitude
latitude = -1.29 
longitude = 36.82

#Folium Map Instance
mymap = Map(location = [latitude, longitude])

#Create a Geopoint Instance
geopoint = Geopoint(latitude = latitude, longitude = longitude)

forecast = geopoint.get_weather()
popup_content = f"""
{forecast[0][0][-8:-6]}h: {round(forecast[0][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[0][-1]}@2x.png" width=35>
<hr style="margin:1px">
{forecast[1][0][-8:-6]}h: {round(forecast[1][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[1][-1]}@2x.png" width=35>
<hr style="margin:1px">
{forecast[2][0][-8:-6]}h: {round(forecast[2][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[2][-1]}@2x.png" width=35>
<hr style="margin:1px">
{forecast[3][0][-8:-6]}h: {round(forecast[3][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[3][-1]}@2x.png" width=35>
"""

#Create Popup object and add it to Geopoint
popup = Popup(popup_content, max_width=400)
popup.add_to(geopoint)
geopoint.add_to(mymap)
 

#Save the Map instance into HTML file
mymap.save("Madrid.html")
