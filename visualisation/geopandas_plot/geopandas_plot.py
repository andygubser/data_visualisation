import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
from preprocessing.functions.data_preprocessor import DataPreprocessor


class GeoPandasPlot:
    @classmethod
    def run(cls):
        data_preprocessor = DataPreprocessor()
        gdf_sharks = data_preprocessor.geo_data
        gdf_world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

        dict_colors_keys = gdf_sharks["species"].value_counts()[:10].index.tolist()
        gdf_sharks = gdf_sharks[gdf_sharks["species"].isin(dict_colors_keys)]
        dict_colors_values = sns.hls_palette(len(dict_colors_keys), l=.3, s=.8)
        dict_colors = dict(zip(dict_colors_keys, dict_colors_values))

        fig, ax = plt.subplots(figsize=(10, 20))
        gdf_world.boundary.plot(ax=ax, alpha=0.4, colors="grey")
        gdf_sharks.plot(ax=ax, markersize=10, alpha=0.5,
                        color=gdf_sharks["species"].apply(lambda x: dict_colors[x]),
                        )
        plt.show(prop={"size": 15})
