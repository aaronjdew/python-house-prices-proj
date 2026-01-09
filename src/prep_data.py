"""-------------------------------------------------------
    Prepare data for machine learning
        -- Create adjusted values for price and value
        -- Predict a future price 
        -- Compare predict price against adjusted price
-------------------------------------------------------"""
import pandas as pd
import constants as cn


def prep_data(df_src_data: pd.DataFrame) -> pd.DataFrame:

    # Init
    df_prp_data = df_src_data

    # Remove inflation from house price/value
    df_prp_data[cn.COL_PRP_DATA[2]] = df_prp_data[cn.COL_SRC_DATA[3]] / \
        df_prp_data[cn.COL_SRC_DATA[2]] * cn.CPI_MULTI

    df_prp_data[cn.COL_PRP_DATA[3]] = df_prp_data[cn.COL_SRC_DATA[4]] / \
        df_prp_data[cn.COL_SRC_DATA[2]] * cn.CPI_MULTI

    # Predict future house price
    df_prp_data[cn.COL_PRP_DATA[4]
                ] = df_prp_data[cn.COL_PRP_DATA[2]].shift(cn.ROW_PRICE_SHIFT)

    # Remove data with no future price
    df_prp_data.dropna(inplace=True)

    # Is the future price greater than the adj price (return an int)
    compare_prices = df_prp_data[cn.COL_PRP_DATA[4]
                                 ] > df_prp_data[cn.COL_PRP_DATA[2]]
    df_prp_data[cn.COL_PRP_DATA[5]] = compare_prices.astype(int)

    return df_prp_data


if __name__ == "__main__":
    print("This module is intended for import only")
