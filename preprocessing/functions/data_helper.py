import pandas as pd
from preprocessing.functions.data_formatter import DataFormatter
from preprocessing.functions.data_categorizer import DataCategorizer


class DataHelper:
    def __init__(self):
        self.raw_data = pd.read_excel("data/data_sharks_raw.xlsx")
        # raw_data = pd.read_csv("http://www.sharkattackfile.net/spreadsheets/GSAF5.xls")
        self.data_formatted = DataFormatter.format_data(self.raw_data)
        self.data_categorized = DataCategorizer.categorize_data(self.data_formatted)


