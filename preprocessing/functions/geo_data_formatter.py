import geopandas as gpd
from shapely.geometry import Point


class GeoDataFormatter:
    @classmethod
    def run(cls, df):
        geometry = [Point(xy) for xy in zip(df["longitude"], df["latitude"])]
        crs = {"init": "epsg:4326"}

        gdf = gpd.GeoDataFrame(df,
                               crs=crs,
                               geometry=geometry)
        return gdf
