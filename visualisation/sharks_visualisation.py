import seaborn as sns
from visualisation.geopandas_plot.geopandas_plot import GeoPandasPlot
from preprocessing.functions.data_preprocessor import DataPreprocessor
import os
os.chdir(r"C:\Users\Andy Gubser\OneDrive - Hochschule Luzern\01 Studium\03 MSc Data Science\Master "
         r"FS20\Wahlpflichtmodule\W.MSCIDS_DVN03.F2001\LNW2")
sns.set()

GeoPandasPlot.run()

