from geopy.geocoders import Nominatim
import pandas as pd
import numpy as np


class GetLatitudeLongitude:

    @classmethod
    def _verify_location(cls, address):
        geolocator = Nominatim()
        return geolocator.geocode(address)

    @classmethod
    def _get_lat_long(cls, address):
        print(cls, address)
        geolocator = Nominatim()
        address_split = address.split(",")
        if cls._verify_location(address) is None:
            location = np.nan, np.nan
            print(location)
            return location

        elif cls._verify_location(address):
            location = geolocator.geocode(address)
            print((location.latitude, location.longitude))
            return location.latitude, location.longitude

        elif cls._verify_location(address_split[0]):
            location = geolocator.geocode(address_split[0])
            print((location.latitude, location.longitude))
            return location.latitude, location.longitude

        elif cls._verify_location(address_split[1]):
            location = geolocator.geocode(address_split[1])
            print((location.latitude, location.longitude))
            return location.latitude, location.longitude

        elif cls._verify_location(address_split[2]):
            location = geolocator.geocode(address_split[2])
            print((location.latitude, location.longitude))
            return location.latitude, location.longitude

    @classmethod
    def merge_with_lat_long(cls, data):
        df_lat_long = pd.read_csv("data/data_long_lat.csv").T.reset_index()
        df_lat_long.columns = ["location", "latitude", "longitude"]
        df = pd.merge(left=data, right=df_lat_long, left_on="location", right_on="location")
        return df

