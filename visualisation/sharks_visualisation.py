import pandas as pd
import matplotlib.pyplot as plt
from preprocessing.functions.data_helper import DataHelper
from preprocessing.functions.data_formatter import DataFormatter
import geopandas as gpd

# prepare geopandas
shapefile = './data/data_countries/ne_10m_admin_0_countries.shp'
gdf = gpd.read_file(shapefile)[['ADMIN', 'ADM0_A3', 'geometry']]
gdf.columns = ['country', 'country_code', 'geometry']
gdf = gdf[gdf['country'] != 'Antarctica']

# prepare shark data
data_helper = DataHelper()
data_formatter = DataFormatter()
df = data_helper.data_categorized
df = df[df["year"].between(1999, 2019)]

df.columns
cols = ['case_number', 'date_prep', 'year_prep', 'type', 'country', 'area', 'location',
       'activity_cat', 'sex', 'age_prep', 'injury_cat', 'fatal(y/n)', 'time',
       'species_cat', 'activity_cat']
df = df[cols]

# df["year"] = df["year"].astype(int)
#
# df.groupby(["year"]).size().plot()
# plt.show()


# merge data
df_merged = gdf.merge(df, left_on="country", right_on="country")

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world.plot()

gpd.datasets._available_dir

from datawrapper import Datawrapper
dw = Datawrapper(access_token = "1234567890")