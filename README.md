# Google Maps POC
Google Maps POC outlines the basic features of Google Maps through
the Python client library for Maps Web Services. These examples
focus on potentially useful APIs for retrieving location data,
including Geocoding API, Geolocation API, Distance Matrix API, and
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
**Geocoding API, Geolocation API, Distance Matrix API, Places API.**
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
**_*Note that the API key also needs to be within double quotes_**

The repository should be all setup for use! Now you enjoy the
examples and modify them to your liking!

### Additional Resources
The examples included were derived based on the help found through
Google's documentation, found at the following links:
* Geocoding API: https://developers.google.com/maps/documentation/geocoding/intro
* Geolocation API: https://developers.google.com/maps/documentation/geolocation/intro
* Distance Matrix API: https://developers.google.com/maps/documentation/distance-matrix/intro
* Places API:
https://cloud.google.com/maps-platform/places/