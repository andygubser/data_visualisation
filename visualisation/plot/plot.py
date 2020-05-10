from preprocessing.functions.data_preprocessor import DataPreprocessor
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# get filtered data set
data_preprocessor = DataPreprocessor()
df_sharks = data_preprocessor.data_filtered

df = df_sharks.groupby(["species", "type"])["fatal"].mean().reset_index()
print(df.head())

sort_order = df[df["type"] == "Unprovoked"][["species", "fatal"]].sort_values("fatal")["species"].tolist()
dict_keys = sort_order
dict_values = range(len(sort_order))
dict_order = dict(zip(dict_keys, dict_values))
df["order"] = df["species"].replace(dict_order)
df.sort_values(by=["order", "type"],
               ascending=False,
               inplace=True)

sns.set(context="poster",
        palette=sns.color_palette("Set1", n_colors=8, desat=.5),
        style="white",
        )
fig, ax = plt.subplots(figsize=(15, 8))
sns.stripplot(data=df, x="species", y="fatal", hue="type", ax=ax,
              jitter=True, size=20)
sns.despine(offset=10, trim=True)
ax.set_title("Fatalities / Total Attacks")
ax.set_xlabel("")
ax.set_xticklabels(labels=df["species"].unique(),
                   rotation=60)
ax.set_ylabel("")
ax.set_ylim(-0.05, 0.5)
ax.legend()
plt.show()
