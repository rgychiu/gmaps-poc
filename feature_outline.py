import googlemaps
import json

# Retrieve API Key from json file
with open('credentials.json') as keyfile:
    data = json.load(keyfile)
    key = data['api_key']

# Authenticate and connect - this only allows access to APIs that support Python client library:
gmaps = googlemaps.Client(key=key)

# Geocoding API
"""
Convert address into coordinates and coordinates (latitude, longitude) to address
Understanding response information at https://developers.google.com/maps/documentation/geocoding/intro#Results
"""
geocode_ex = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
reverse_geocode_ex = gmaps.reverse_geocode((41.8789, -87.6359))
print('------------------------------------ GEOCODING API -----------------------------------------')
print('Response example: ' + json.dumps(geocode_ex, indent=4, sort_keys=False))
print('Geocode from address to coordinates: ' + str(geocode_ex[0]['formatted_address']))
print('Geocode from coordinates to address: ' + str(reverse_geocode_ex[0]['formatted_address']))

# Distance Matrix API


# Places API
"""
Seach for Shedd Aquarium and get all data available
Understanding response information at https://developers.google.com/places/web-service/intro
"""
place_search = gmaps.places('Shedd Aquarium')
print('------------------------------------ PLACES API -----------------------------------------')
print('Response example: ' + json.dumps(place_search, indent=4, sort_keys=False))
print('Places API Address: ' + place_search['results'][0]['formatted_address'])
print('Places place_id: ' + place_search['results'][0]['place_id'])