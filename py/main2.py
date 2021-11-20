from folium import Map
from geo import Geopoint

latitude = 40.09
longitude = 3.47

antipole_latitude = latitude * -1

if longitude <= 0:
    antipole_longitude = longitude + 180
elif longitude == 0 :
    antipole_longitude = 180
elif longitude >= 180:
    antipole_longitude = "Invalid Longitude"
else: 
    antipole_longitude = longitude - 180

location = list((antipole_latitude, antipole_longitude))

my_map = Map(location)
my_map.save("antipole.html")

my_point = Geopoint(41.2, 4.1)
cp = my_point.closest_parallel()
print(cp)

print(antipole_latitude)
print(antipole_longitude)
print(my_map)



#dollars = float("252.2")
#euros = dollars.__mul__(float("0.87"))
#print("euros")
