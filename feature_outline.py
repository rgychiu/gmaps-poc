import googlemaps
import json

"""
Python Client Library for Google Maps API Web Services
basic use cases and code samples.

This program demonstrates using the Places API, Geooding API, and
Distance Matrix API to search for specific locations in a variety
of different ways and find the distances between two locations.

Additional Documentation can be found at: https://developers.google.com/maps/documentation/
"""

# Retrieve API Key from json file
with open('credentials.json') as keyfile:
    data = json.load(keyfile)
    key = data['api_key']

# Authenticate and connect - this only allows access to APIs that support Python client library:
gmaps = googlemaps.Client(key=key)

# Places API
"""
Search for Shedd Aquarium and get all data available
Understanding response information at https://developers.google.com/places/web-service/intro
"""
place_search = gmaps.places('Shedd Aquarium')
place_details = gmaps.place(place_search['results'][0]['place_id'])
place_suggestions = gmaps.places_autocomplete('Paris')
place_suggest_query = gmaps.places_autocomplete_query('pizza near Chicago')
print('------------------------------------ PLACES API -----------------------------------------')
print('Response example: ' + json.dumps(place_search, indent=4, sort_keys=False))
print('Places API Address: ' + place_search['results'][0]['formatted_address'])
print('Places place_id: ' + place_search['results'][0]['place_id'])
print('Place details example response: ' + json.dumps(place_details, indent=4, sort_keys=False))
print('Place suggestions example response: ' + json.dumps(place_suggestions, indent=4, sort_keys=False))
print('Place query suggestions example response: ' + json.dumps(place_suggest_query, indent=4, sort_keys=False))

# Geocoding API
"""
Convert address into coordinates and coordinates (latitude, longitude) to address
Understanding response information at https://developers.google.com/maps/documentation/geocoding/intro#Results
"""
geocode_ex = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
reverse_geocode_ex = gmaps.reverse_geocode((41.8789, -87.6359))
place_id_geocode = gmaps.geocode(place_search['results'][0]['place_id'])
print('------------------------------------ GEOCODING API -----------------------------------------')
print('Response example: ' + json.dumps(geocode_ex, indent=4, sort_keys=False))
print('Geocode from address to coordinates: ' + str(geocode_ex[0]['formatted_address']))
print('Geocode from coordinates to address: ' + str(reverse_geocode_ex[0]['formatted_address']))

# Distance Matrix API
"""
Get distance between two cities (San Antonio and Orlando) in both miles and kilometers.
Understanding response information at https://developers.google.com/maps/documentation/distance-matrix/intro
"""
address_distance = gmaps.distance_matrix("San Antonio, TX", "Orlando, FL")
address_dist_imperial = gmaps.distance_matrix("San Antonio, TX", "Orlando, FL", units="imperial")
coord_distance = gmaps.distance_matrix((29.4241, 98.4936), (28.5383, 81.3792))
place_id_dist = gmaps.distance_matrix('place_id:' + place_search['results'][0]['place_id'], 'place_id:' + geocode_ex[0]['place_id'])
print('------------------------------------ DISTANCE MATRIX API -----------------------------------------')
print('Response example: ' + json.dumps(address_dist_imperial, indent=4, sort_keys=False))
print('Distance in metric units: ' + address_distance['rows'][0]['elements'][0]['distance']['text'])
print('Distance in imperial units: ' + address_dist_imperial['rows'][0]['elements'][0]['distance']['text'])
print('Place ID distance: ' + place_id_dist['rows'][0]['elements'][0]['distance']['text'])