"""-------------------------------------------------------
    Load Federal Reserve Data
        -- US CPI data (Inflation Measure)
        -- Rental Vacancy Rate (Quarterly)
        -- Mortgage Interest Rate (Weekly)
    Load Zillow Data
        -- Median Sales Price
        -- Home Value Index
    Merge All Data
-------------------------------------------------------"""
import string as st
from datetime import timedelta as td
import pandas as pd
import constants as cn


def extract_src_data() -> pd.DataFrame:

    # --Federal Data--
    # Federal files for retrieval
    fil_fed = [cn.FP_MIR_CSV, cn.FP_RVR_CSV, cn.FP_CPI_CSV]

    # Created nested list for files
    lst_fed = [pd.read_csv(fil, parse_dates=True, index_col=0)
               for fil in fil_fed]

    # Create a single dataframe
    df_fed = pd.concat(lst_fed, axis=1)

    # Forward fil missing data (assume data stays static)
    df_fed = df_fed.ffill()

    # Remove any rows that has any NAs
    df_fed = df_fed.dropna()

    # Add two days to data to align with Zillow data
    df_fed.index = df_fed.index + td(days=2)

    # --Zillow Data--
    # Zillow files for retrieval
    fil_zil = [cn.FP_SAP_CSV, cn.FP_HVI_CSV]

    # Created nested list for files
    lst_zil = [pd.read_csv(fil) for fil in fil_zil]

    # Filter only 1st row of data, filter out first 5 columns
    lst_zil = [pd.DataFrame(df.iloc[0, 5:]) for df in lst_zil]

    # Change index to datetime from string
    # Create a common column to merge the data
    for df in lst_zil:
        # Check third character is a special character
        spec_char = df.index.str[2].isin(list(st.punctuation)).any()

        if spec_char:
            # Check if max of first two characters are a day
            max_1 = max(int(i) for i in df.index.str[:2])
            # Check if max of characters 3 and 4 are a day
            max_2 = max(int(i) for i in df.index.str[3:5])
            if max_1 > 12 or max_2 > 12:
                df.index = pd.to_datetime(df.index, dayfirst=True)
            else:
                df.index = pd.to_datetime(df.index, dayfirst=False)
        else:
            df.index = pd.to_datetime(df.index, dayfirst=False)

        df[cn.COL_COMMON] = df.index.to_period(cn.COL_COMMON_PT)

    # Create df of merged data using new column
    df_zil = lst_zil[0].merge(lst_zil[1], on=cn.COL_COMMON)

    # Set the new data frame index as the same as the lst
    df_zil.index = lst_zil[0].index

    # Delete the created column / rename the merged columns
    del df_zil[cn.COL_COMMON]
    df_zil.columns = cn.COL_SRC_DATA[3:]

    # --Final Data--
    # Merge data using indexes
    df_src_data = df_fed.merge(df_zil, left_index=True, right_index=True)

    # Change column names
    df_src_data.columns = cn.COL_SRC_DATA

    return df_src_data


if __name__ == "__main__":
    print("This module is intended for import only")
