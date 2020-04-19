import pandas as pd
import datetime as dt
import numpy as np
import re
import matplotlib.pyplot as plt

pd.options.display.max_rows = 999

# read data
raw_data = pd.read_excel("data_sharks.xlsx")


# raw_data = pd.read_excel("http://www.sharkattackfile.net/spreadsheets/GSAF5.xls")

# rename colnames

def camel_to_snake(name):
    import re
    name = name.replace(" ", "").replace(".", "_")
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()
    return name


def colnames_to_snake(colnames: object) -> object:
    return [camel_to_snake(col) for col in list(colnames)]


df = raw_data
df.columns = colnames_to_snake(df.columns)

# format date
substrings_to_drop = "Reported.|Ca.| |\.a|\.b|Before|Mid-"
df["date_cleaned"] = df["date"].str.replace(substrings_to_drop, "").str.replace("--", "-")

df["year_extracted"] = df["date_cleaned"].str.extract("(\d{4})")
df["year_extracted"] = pd.to_numeric(df["year_extracted"], errors="ignore")
df["year_extracted"] = df["year_extracted"].fillna(0).astype(int)
df["year_extracted"].value_counts()

df["month_extracted"] = df["date_cleaned"].str.extract("([A-Z]{1}[a-z]{2}\-)", )
df["month_extracted"] = df["month_extracted"].str.replace("-", "")
df["month_extracted"].value_counts()

df["date_cleaned"] = pd.to_datetime(df["date_cleaned"], errors="coerce", utc=None)

# factorize activity
def get_synonyms(colname, string):
    return df[df[colname].str.contains(string, case=False, na=False)][colname].unique().tolist()


df["activity_cat"] = df["activity"].str.lower()
df["activity_cat"].replace(get_synonyms("activity", "surf|board"), "surfing", inplace=True)
df["activity_cat"].replace(get_synonyms("activity", "sup|paddl"), "paddling", inplace=True)
df["activity_cat"].replace(get_synonyms("activity", "swim|float|jump|fell"), "swimming", inplace=True)
df["activity_cat"].replace(get_synonyms("activity", "fish"), "fishing", inplace=True)
df["activity_cat"].replace(get_synonyms("activity", "div"), "diving", inplace=True)
df["activity_cat"].replace(get_synonyms("activity", "wad|stand|walk|tread|play|splash|clam|dang|bath"), "bathing", inplace=True)
df["activity_cat"].replace(get_synonyms("activity", "snorkel"), "snorkeling", inplace=True)
df["activity_cat"].replace(get_synonyms("activity", "kayak|canoe|row|sail"), "kayaking", inplace=True)
df["activity_cat"].replace(get_synonyms("activity", "craft|boat"), "watercraft", inplace=True)
df["activity_cat"].replace(get_synonyms("activity", "shark"), "shark contacting", inplace=True)

activity_cat = set(["surfing", "paddling", "swimming", "fishing", "diving", "bathing",
                       "snorkeling", "kayaking", "watercraft", "shark contacting"])
nonclassified_cat = set(df["activity_cat"]) - activity_cat
nonclassified_cat = list(nonclassified_cat)

df["activity_cat"].replace(nonclassified_cat, "non-classified", inplace=True)
# df = df[df["year_extracted"] > 1999]


# factorize injury
df["injury_cat"] = df["injury"].str.lower()
df["injury_cat"].replace(get_synonyms("injury", "fatal"), "fatal", inplace=True)
df["injury_cat"].replace(get_synonyms("injury", "foot"), "foot", inplace=True)
df["injury_cat"].replace(get_synonyms("injury", "leg"), "leg", inplace=True)
df["injury_cat"].replace(get_synonyms("injury", "arm"), "arm", inplace=True)
df["injury_cat"].replace(get_synonyms("injury", "hand"), "hand", inplace=True)


df["injury_cat"].value_counts()

activity_cat = set(["surfing", "paddling", "swimming", "fishing", "diving", "bathing",
                       "snorkeling", "kayaking", "watercraft", "shark contacting"])
nonclassified_cat = set(df["activity_cat"]) - activity_cat
nonclassified_cat = list(nonclassified_cat)

df["activity_cat"].replace(nonclassified_cat, "non-classified", inplace=True)



# export data to excel
df.to_excel("data_preprocessed.xlsx")
