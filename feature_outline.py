import googlemaps
import json

# Retrieve API Key from json file
with open('credentials.json') as keyfile:
    key = json.load(keyfile)['api_key']

# Authenticate and connect
gmaps = googlemaps.Client(key=key)

# Places API

# Geolocation API

# Geocoding API

# Distance Matrix API