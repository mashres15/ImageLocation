# mappingTools.py - a collection of simple functions related to mapping and geocodes
import math as m
from geopy.distance import vincenty

earthRadiusKm = 6378.1

def distanceBetweenPoints(lat1, lon1, lat2, lon2):
  place1 = (lat1, lon1)
  place2 = (lat2, lon2)
  distance = vincenty(place1, place2).km
  return(distance / earthRadiusKm)

def distanceBetweenPointsOld(lat1, lon1, lat2, lon2):
  # Compute the distance between two latitude, longitude pairs, 
  # Assume that the earth is a perfect sphere.

  # Convert latitude and longitude to spherical coordinates in radians.
  degrees_to_radians = m.pi / 180.0

  # phi = 90 - latitude
  phi1 = (90.0 - lat1) * degrees_to_radians
  phi2 = (90.0 - lat2) * degrees_to_radians

  # theta = longitude
  theta1 = lon1 * degrees_to_radians
  theta2 = lon2 * degrees_to_radians

  # Compute spherical distance from spherical coordinates. For two locations in 
  # spherical coordinates (1, theta, phi) and (1, theta', phi'): 
  #   cosine( arc length ) = sin phi sin phi' cos(theta-theta') + cos phi cos phi'
  #   distance = rho * arc length
  cos = (m.sin(phi1) * m.sin(phi2) * m.cos(theta1 - theta2) + m.cos(phi1) * m.cos(phi2))
  distance = m.acos(cos)

  # Multiply arc by the radius of the earth in the appropriate units to get normalized distance.
  return(distance)

def validateLat(lat):
  if ((lat >= -90.0) and (lat <= 90.0)):
    return(True)
  else:
    return(False)

def validateLon(lon):
  if ((lon >= -180.0) and (lon <= 180.0)):
    return(True)
  else:
    return(False)

def validateRadius(searchRadius):
  if ((searchRadius > 0.0) and (searchRadius < .5 * (2 * m.pi * earthRadiusKm))):
    return(True)
  else:
    return(False)

if __name__ == "__main__":
    inputFile = 'first-coordinates.dat'
    inputHandle = open(inputFile, "r")

    for line in inputHandle.readlines():
        (lat1, lon1, lat2, lon2) = line.split(",")
        (lat1, lon1, lat2, lon2) = float(lat1), float(lon1), float(lat2), float(lon2)

        distance = distanceBetweenPoints(lat1, lon1, lat2, lon2)
        print(lat1, "\t", lon1, "\t", distance, "\t", lat2, "\t", lon2)