from preprocessing.functions.data_helper import DataHelper
from preprocessing.functions.data_formatter import DataFormatter

data_helper = DataHelper()
data_formatter = DataFormatter()
df = data_helper.data_categorized

df.to_excel("data/data_sharks_prep.xlsx")
