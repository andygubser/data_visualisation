import pandas as pd


class DataCategorizer:
    @classmethod
    def categorize_data(cls, df):
        df = cls._categorize_injuries(df)
        df = cls._categorize_activities(df)
        df = cls._categorize_species(df)
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

    @classmethod
    def _categorize_species(cls, df):
        df["species_cat"] = "non_classified"
        df.loc[df["species"].str.contains("bull|leucas", case=False, na=False), "species_cat"] = "bull shark"
        df.loc[df["species"].str.contains("grey", case=False, na=False), "species_cat"] = "grey shark"
        df.loc[df["species"].str.contains("white", case=False, na=False), "species_cat"] = "white shark"
        df.loc[df["species"].str.contains("tiger", case=False, na=False), "species_cat"] = "tiger shark"
        df.loc[df["species"].str.contains("lemon", case=False, na=False), "species_cat"] = "tiger shark"
        df.loc[df["species"].str.contains("shovelnose", case=False, na=False), "species_cat"] = "shovelnose ray"
        df.loc[df["species"].str.contains("black", case=False, na=False), "species_cat"] = "blacktip shark"
        df.loc[df["species"].str.contains("whitetip|white tip", case=False, na=False), "species_cat"] = "whitetip shark"
        df.loc[df["species"].str.contains("galapagos", case=False, na=False), "species_cat"] = "galapagos shark"
        df.loc[df["species"].str.contains("broadnose", case=False, na=False), "species_cat"] = "broadnose shark"
        df.loc[df["species"].str.contains("cookiecutter", case=False, na=False), "species_cat"] = "cookiecutter shark"
        df.loc[df["species"].str.contains("nurse", case=False, na=False), "species_cat"] = "nurse shark"
        df.loc[df["species"].str.contains("spinner", case=False, na=False), "species_cat"] = "spinner shark"
        df.loc[df["species"].str.contains("reef", case=False, na=False), "species_cat"] = "reef shark"
        df.loc[df["species"].str.contains("stingray", case=False, na=False), "species_cat"] = "sting ray"
        df.loc[df["species"].str.contains("wobbegong", case=False, na=False), "species_cat"] = "wobbegong shark"
        df.loc[df["species"].str.contains("blue", case=False, na=False), "species_cat"] = "blue shark"
        df.loc[df["species"].str.contains("eel", case=False, na=False), "species_cat"] = "eel"
        df.loc[df["species"].str.contains("hammerhead", case=False, na=False), "species_cat"] = "hammerhead shark"
        df.loc[df["species"].str.contains("raggedtooth", case=False, na=False), "species_cat"] = "raggedtooth shark"
        df.loc[df["species"].str.contains("bonita", case=False, na=False), "species_cat"] = "bonita shark"
        df.loc[df["species"].str.contains("whaler", case=False, na=False), "species_cat"] = "whaler shark"
        df.loc[df["species"].str.contains("leopard", case=False, na=False), "species_cat"] = "leopard shark"
        df.loc[df["species"].str.contains("mako", case=False, na=False), "species_cat"] = "mako shark"
        df.loc[df["species"].str.contains("toadfish", case=False, na=False), "species_cat"] = "toadfish"
        df.loc[df["species"].str.contains("salmon", case=False, na=False), "species_cat"] = "salmon shark"
        df.loc[df["species"].str.contains("angel", case=False, na=False), "species_cat"] = "angel shark"
        df.loc[df["species"].str.contains("dogfish", case=False, na=False), "species_cat"] = "dogfish shark"
        df.loc[df["species"].str.contains("debris", case=False, na=False), "species_cat"] = "debris"
        df.loc[df["species"].str.contains("zambesi", case=False, na=False), "species_cat"] = "zambesi shark"
        df.loc[df["species"].str.contains("sevengill|seven-gill|7-gill", case=False, na=False), "species_cat"] = "sevengill shark"
        df.loc[df["species"].str.contains("sandbar", case=False, na=False), "species_cat"] = "sandbar shark"
        df.loc[df["species"].str.contains("porbeagle", case=False, na=False), "species_cat"] = "porbeagle shark"
        df.loc[df["species"].str.contains("bronze", case=False, na=False), "species_cat"] = "bronze whale shark"
        df.loc[df["species"].str.contains("dusky", case=False, na=False), "species_cat"] = "dusky shark"
        df.loc[df["species"].str.contains("basking", case=False, na=False), "species_cat"] = "basking shark"
        df.loc[df["species"].str.contains("goblin", case=False, na=False), "species_cat"] = "goblin shark"
        df.loc[df["species"].str.contains("sand", case=False, na=False), "species_cat"] = "sand shark"
        df.loc[df["species"].str.contains("catshark", case=False, na=False), "species_cat"] = "catshark shark"
        df.loc[df["species"].str.contains("silvertip", case=False, na=False), "species_cat"] = "silvertip shark"
        df.loc[df["species"].str.contains("hound", case=False, na=False), "species_cat"] = "smooth hound shark"
        df.loc[df["species"].str.contains("cow", case=False, na=False), "species_cat"] = "cow shark"
        df.loc[df["species"].str.contains("jackson", case=False, na=False), "species_cat"] = "port jackson shark"
        df.loc[df["species"].str.contains("spurdog", case=False, na=False), "species_cat"] = "spurdog"
        df.loc[df["species"].str.contains("carcharhinid|ground", case=False, na=False), "species_cat"] = "ground shark"
        df.loc[df["species"].str.contains("carpet", case=False, na=False), "species_cat"] = "carpet shark"
        df.loc[df["species"].str.contains("thresher", case=False, na=False), "species_cat"] = "thresher shark"

        df.loc[df["species"].str.contains("unknown|unidentified", case=False, na=False), "species_cat"] = "unknown"
        df.loc[df["species"].str.contains("doubtful|no shark|still|not|questionable|unconf|invalid|probable", case=False, na=False), "species_cat"] = "no or doubtful shark involvement"

        # df.loc[df["species"].str.contains("small|juvenile", case=False, na=False), "species_cat"] = "small shark"
        # df.loc[df["species"].str.contains("large", case=False, na=False), "species_cat"] = "large shark"
        df.loc[df["species"].str.contains("many|class|school|pack|number", case=False, na=False),
               "species_cat"] = "shark pack"

        return df
