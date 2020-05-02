import pandas as pd


class DataCategorizer:
    @classmethod
    def categorize_data(cls, df):
        df = cls._categorize_injuries(df)
        df = cls._categorize_activities(df)
        return df

    @classmethod
    def _categorize_injuries(cls, df):
        df["injury_cat"] = "non-classified"
        df.loc[df["injury"].str.contains("foot", case=False, na=False), 'injury_cat'] = "foot"
        df.loc[df["injury"].str.contains("leg", case=False, na=False), 'injury_cat'] = "leg"
        df.loc[df["injury"].str.contains("arm", case=False, na=False), 'injury_cat'] = "arm"
        df.loc[df["injury"].str.contains("hand", case=False, na=False), 'injury_cat'] = "hand"
        return df

    @classmethod
    def _categorize_activities(cls, df):
        df["activity_cat"] = "non-classified"
        df.loc[df["activity"].str.contains("surf|board", case=False, na=False), 'activity_cat'] = "surfing"
        df.loc[df["activity"].str.contains("sup|paddl", case=False, na=False), 'activity_cat'] = "paddling"
        df.loc[df["activity"].str.contains("swim|float|jump|fell", case=False, na=False), 'activity_cat'] = "swimming"
        df.loc[df["activity"].str.contains("fish", case=False, na=False), 'activity_cat'] = "fishing"
        df.loc[df["activity"].str.contains("div", case=False, na=False), 'activity_cat'] = "diving"
        df.loc[df["activity"].str.contains("fish", case=False, na=False), 'activity_cat'] = "bathing"
        df.loc[df["activity"].str.contains("snorkel", case=False, na=False), 'activity_cat'] = "snorkeling"
        df.loc[df["activity"].str.contains("kayak|canoe|row|sail", case=False, na=False), 'activity_cat'] = "kayaking"
        df.loc[df["activity"].str.contains("craft|boat", case=False, na=False), 'activity_cat'] = "watercraft"
        df.loc[df["activity"].str.contains("shark", case=False, na=False), 'activity_cat'] = "shark contacting"
        return df

    @classmethod
    def _categorize_age(cls, df):
        df["age_cat"] = "non_classified"
        df["age_prep"] = pd.to_numeric(df["age_prep"])
        bins = pd.IntervalIndex.from_tuples([(0, 10), (10, 20), (20, 30), (30, 40), (40, 50),
                                             (50, 60), (60, 70), (70, 90)])
        df["age_cat"] = pd.cut(df["age_prep"], bins)

        # df.loc[df["age_cat"].isna(), 'age'].unique()
        df.loc[df["age"].str.contains("10|minor", case=False, na=False), "age_cat"] = 8
        df.loc[df["age"].str.contains("teen", case=False, na=False), "age_cat"] = 18
        return df