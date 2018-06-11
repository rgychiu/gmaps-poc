import googlemaps
import json
import requests

# Retrieve API Key from json file
with open('credentials.json') as keyfile:
    key = json.load(keyfile)['api_key']

# Authenticate and connect - this only allows access to APIs that support Python client library:
gmaps = googlemaps.Client(key=key)

# APIs that require HTTP requests and endpoints
places_endpoint = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'

# Geolocation API

# Geocoding API
# Convert address into coordinates and coordinates (latitude, longitude) to address
geocode_ex = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
reverse_geocode_ex = gmaps.reverse_geocode((41.8789, -87.6359))
print('------------------------------------ GEOCODING API -----------------------------------------')
print('Response example: ' + json.dumps(geocode_ex, indent=4, sort_keys=False))
print('Geocode from address to coordinates: ' + str(geocode_ex[0]['formatted_address']))
print('Geocode from coordinates to address: ' + str(reverse_geocode_ex[0]['formatted_address']))

# Distance Matrix API

# Places API
# Place Search
"""
params = {'input': 'mcdonalds', 'inputtype': 'textquery', 'key': key}
place_search = requests.get(places_endpoint, params=params)
print(place_search.url)
print(place_search.text)
"""