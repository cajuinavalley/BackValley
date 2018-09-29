from django.conf import settings
import googlemaps

def getLatLon(address):
  gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
  geocode_result = gmaps.geocode(address)

  if (geocode_result):
    if ('geometry' in geocode_result[0]):
      if ('location' in geocode_result[0]['geometry']):
        lat, lon = geocode_result[0]['geometry']['location'].values()
        return lat, lon