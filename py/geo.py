from datetime import datetime
from pytz import timezone
from timezonefinder import TimezoneFinder
from sunnyday import Weather
from random import uniform
from folium import Marker

class Geopoint(Marker):
    
    def __init__(self, latitude, longitude, popup=None):
        super().__init__(location = [latitude, longitude], popup=popup)
        self.latitude = latitude
        self.longitude = longitude
        
    def closest_parallel(self):
        return round(self.latitude)
    
    def get_time(self):
        timezone_string = TimezoneFinder().timezone_at(lat =self.latitude, lng = self.longitude)
        time_now = datetime.now(timezone(timezone_string))
        return time_now
    
    def get_weather(self):
        weather = Weather(apikey="d27c0a2830d282c3e52c385fed667527",
                          lat = self.latitude, lon = self.longitude)
        return weather.next_12h_simplified()
    
    @classmethod
    def random(cls):
        return cls(latitude = uniform(-90,90), longitude = uniform(-180,180))
    
    
    
#tokyo = Geopoint(latitude = 35.7, longitude = 139.7)
#print(tokyo.closest_parallel())
#print(tokyo.get_time())
#print(tokyo.get_weather())
