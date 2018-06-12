# Google Maps POC
Google Maps POC outlines the basic features of Google Maps through
the Python client library for Maps Web Services. These examples
focus on potentially useful APIs for retrieving place data,
including Geocoding API, Distance Matrix API, and
Places API.

### Setup
In order to get started with using these examples, first clone the
repository:
```
https://github.com/rgychiu/gmaps-poc.git
```

The Google Maps APIs also require an API Key. To obtain a key to 
use for these examples:
1. Visit https://console.developers.google.com/ and login.
2. Create a new project or use an existing project and navigate
to the credentials tab.
3. Once in the dashboard, search for and enable the following APIs:
**Geocoding API, Distance Matrix API, Places API.**
4. Navigate to the credentials tab and create a new API Key
5. Restrict the API Key to the following APIs by clicking on 
the APIs tab when editing the key and selecting the enabled APIs.

After setting up an API key, navigate to the cloned respository
and create a new file named ```credentials.json``` and paste the
following JSON into the file:
```
{
    "api_key": YOUR_API_KEY_HERE
}
```
**_*NOTE: that the API key also needs to be within double quotes.
The file ```credentials.json``` is also included in the .gitignore.
This is to ensure the secrecy of the API Key._**

The repository should be all setup for use! Now you can enjoy the
examples and modify them to your liking!

### Additional Information
The Google Maps Platform and Web Service provide many tools that
aid in gathering information about different places, such as 
searching and getting data through the Places API. The different
APIs also work seamlessly together through using addresses as 
search queries or ```place_ids```. This feature also means that
GMaps is also able to interact with other APIs such as Yelp to
extract further information about a location. Extra tools are also included, such
as the ability to calculate distance between two locations with
the Distance Matrix API.

Nonetheless, each API comes with some drawbacks and biases
including the region and viewport biases found in the Geocoding
API. More information can be found in the documentation of each
API.

### Resources
The examples included were derived based on the help found through
Google's documentation, found at the following links:
* Geocoding API: https://developers.google.com/maps/documentation/geocoding/intro
* Distance Matrix API: https://developers.google.com/maps/documentation/distance-matrix/intro
* Places API: https://cloud.google.com/maps-platform/places/
* Client Documentation: https://googlemaps.github.io/google-maps-services-python/docs/