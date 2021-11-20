from folium import Map
latitude = float("40.09")
longitude = float("3.47")

antipole_latitude = latitude.__mul__(int("-1"))

if longitude.__lt__(float("0")):
    antipole_longitude = longitude.__add__(float("180"))
elif longitude.__eq__(float("0")):
    antipole_longitude = float("180")
elif longitude.__gt__(float("180")):
    antipole_longitude = str("Invalid Longitude")
else: 
    antipole_longitude = longitude.__sub__(float("180"))

location = list((antipole_latitude, antipole_longitude))
my_map = Map(location)
my_map.save(str("antipole.html"))

print(antipole_latitude)
print(antipole_longitude)
print(my_map)



#dollars = float("252.2")
#euros = dollars.__mul__(float("0.87"))
#print("euros")