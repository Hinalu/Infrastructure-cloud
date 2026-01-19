import datetime
print ("Current date and time: ")
print (datetime.datetime.now())

### Test 1
!pip install geopy
!pip install folium
from geopy.geocoders import Nominatim
import folium
import datetime
print ("Current date and time: ")
print (datetime.datetime.now())

geolocator = Nominatim(user_agent = "jupyter")
city_country = "Fugging, Austria"
location = geolocator.geocode(city_country)
devnet_lat = location.latitude
devnet_lon = location.longitude
coordinates = [devnet_lat,devnet_lon]
map = folium.Map(location = coordinates, tiles = 'OpenstreetMap', zoom_start=24)
display(map)

### Test 2
!pip install geopy
!pip install folium
from geopy.geocoders import Nominatim
import folium
#
geolocator = Nominatim(user_agent="http://biasc.be")
#### Enter city and country
city_country = "Merchtem, Belgium"
####
location = geolocator.geocode(city_country)
print(location.address)
devnet_lat = location.latitude
devnet_lon = location.longitude
print((devnet_lat, devnet_lon))
#
coordinates = [devnet_lat,devnet_lon]
map = folium.Map(location=coordinates, tiles='OpenStreetMap',  zoom_start=12)
# save method of Map object will create a map
# saved in Downloads
display(map)