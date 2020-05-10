import pandas as pd


class DataFilter:
    @classmethod
    def filter(cls, df):

        # only include years after 1980
        df_sample = df[df["year"] >= 1950]

        # include only most common species
        species_to_include = set(df_sample["species_cat"].value_counts()[:10].index.tolist())
        species_to_include -= {"non_classified", "no or doubtful shark involvement", "non_classified"}
        df_sample = df_sample[df_sample["species_cat"].isin(species_to_include)]

        # include only provoked and unprovoked in type
        df_sample = df_sample[df_sample["type"].isin(["Provoked", "Unprovoked"])]

        # include only confirmed fatalities or confirmed non-fatalities
        df_sample = df_sample[~df_sample["fatal_cat"].isna()]
        df_sample = df_sample[df_sample["fatal_cat"] != "unknown"]
        df_sample["fatal_cat"] = pd.to_numeric(df_sample["fatal_cat"])

        # include only columns necessary for visualisation
        cols_to_include = ["year_prep",
                           "date_prep",
                           "time",
                           "activity_cat",
                           "species_cat",
                           "fatal_cat",
                           "injury_cat",
                           "type"]
        df_sample = df_sample[cols_to_include]
        df_sample.rename(columns={"year_prep": "year",
                                  "date_prep": "date",
                                  "activity_cat": "activity",
                                  "species_cat": "species",
                                  "fatal_cat": "fatal",
                                  "injury_cat": "injury"},
                         inplace=True)

        return df_sample
