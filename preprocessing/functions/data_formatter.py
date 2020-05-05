import pandas as pd
import numpy as np

pd.options.display.max_rows = 500


class DataFormatter:
    @classmethod
    def format_data(cls, df):
        df = cls._format_columns(df)
        df = cls._format_booleans(df)
        df = cls._format_numericals(df)
        df = cls._format_rows(df)
        df = cls._format_datetimes(df)
        df = cls._format_age(df)
        return df.reset_index(drop=True)

    @classmethod
    def _format_columns(cls, df):
        df.dropna(how="all", axis="columns", inplace=True)
        df.columns = map(cls._camel_to_snake, df.columns)

        unnamed_cols = df.columns[df.columns.str.contains('unnamed')].tolist()
        df.drop(unnamed_cols, axis="columns", inplace=True)

        # df = df.reindex(sorted(df.columns), axis="columns")
        return df

    @classmethod
    def _format_rows(cls, df):
        df["case_number"] = df["case_number"].replace(0, np.nan)
        df = df[~df["case_number"].isna()]

        return df

    @classmethod
    def _camel_to_snake(cls, single_column_name):
        import re
        single_column_name = single_column_name.replace(" ", "").replace(".", "_")
        single_column_name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', single_column_name)
        single_column_name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', single_column_name).lower()
        return single_column_name

    @classmethod
    def _format_booleans(cls, df):
        return df.replace(["false", "true"], [False, True])

    @classmethod
    def _format_numericals(cls, df):
        params = list([df.columns[df.columns.str.startswith("param_")],
                       df.columns[df.columns.str.startswith("kpi_")],
                       df.columns[df.columns.str.startswith("recipe_")]
                       ])
        params = [item for sublist in params for item in sublist]
        params = [x for x in params if 'timestamp' not in x]
        df[params] = df[params].apply(pd.to_numeric, downcast="signed", errors="ignore")
        return df

    @classmethod
    def _format_date(cls, df):
        df["date_prep"] = df["date"].str.lower()
        df["date_prep"] = df["date_prep"].str.strip()
        df["date_prep"] = df["date_prep"].str.replace("reported", "")
        df["date_prep"] = df["date_prep"].str.replace("before", "")
        df["date_prep"] = pd.to_datetime(df["date_prep"], errors="ignore")
        return df

    @classmethod
    def _format_year(cls, df):
        df["year_prep"] = df["year"].replace(0.0, np.nan)
        df["year_from_casenumber"] = df["case_number"].str.findall('\d{4}').str[0]
        df["year_from_casenumber"] = pd.to_numeric(df["year_from_casenumber"])
        df["year_from_casenumber"] = df["year_from_casenumber"].mask(df["year_from_casenumber"] < 1000)

        df["year_from_date"] = df["date"].str.findall('\d{4}').str[-1]
        df["year_from_date"] = pd.to_numeric(df["year_from_date"])

        df.loc[df["year_prep"].isna(), 'year_prep'] = df["year_from_date"]
        df.loc[df["year_prep"].isna(), 'year_prep'] = df["year_from_casenumber"]
        return df

    @classmethod
    def _format_datetimes(cls, df):
        df = cls._format_date(df)
        df = cls._format_year(df)
        return df

    @classmethod
    def _format_age(cls, df):
        df["age_prep"] = df["age"].astype(str).str.findall('\d+').str[0]
        df["age_prep"] = pd.to_numeric(df["age_prep"], errors="ignore")
        # df.loc[df["age_prep"].str.len() == 0, "age_prep"]
        return df

    # @classmethod
    # def _unstack_list(cls, df, col_to_concatenate):
    #     cols_all = set(df.columns)
    #     cols_to_repeat = cols_all.difference(col_to_concatenate)
    #     number_of_lists_per_row = df[col_to_concatenate].str.len().fillna(1)
    #
    #     df_unstacked = pd.DataFrame({
    #         col: np.repeat(df[col].values, number_of_lists_per_row) for col in cols_to_repeat
    #     }).assign(**{col_to_concatenate: np.concatenate(df[col_to_concatenate].values)})[df.columns.tolist()]
    #
    #     # df = pd.DataFrame({cols_to_repeat:
    #     #                        np.repeat(
    #     #                            df[cols_to_repeat].values,
    #     #                            df[col_to_concatenate].str.len()),
    #     #                    col_to_concatenate:
    #     #                        np.concatenate(df[col_to_concatenate].values)})
    #     return df
