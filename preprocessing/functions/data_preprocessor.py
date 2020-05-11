import pandas as pd
from preprocessing.functions.data_formatter import DataFormatter
from preprocessing.functions.data_categorizer import DataCategorizer
from preprocessing.functions.get_latitude_longitude import GetLatitudeLongitude
from preprocessing.functions.data_filter import DataFilter
from preprocessing.functions.geo_data_formatter import GeoDataFormatter


class DataPreprocessor:
    def __init__(self):
        self.raw_data = pd.read_excel("data/data_sharks/data_sharks_raw.xlsx")
        # raw_data = pd.read_csv("http://www.sharkattackfile.net/spreadsheets/GSAF5.xls")
        self.data_formatted = DataFormatter.format_data(self.raw_data)
        self.data_categorized = DataCategorizer.categorize_data(self.data_formatted)
        self.data_filtered = DataFilter.filter(self.data_categorized)

        # data preparation for visualisation with geopandas
        self.geo_data_with_lat_long = GetLatitudeLongitude.merge_with_lat_long(self.data_categorized)
        self.geo_data = GeoDataFormatter.run(self.geo_data_with_lat_long)
