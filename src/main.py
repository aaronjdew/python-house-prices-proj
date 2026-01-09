"""-------------------------------------------------------
    MAIN PROCEDURE
        -- Extract all data from source files and merge
        -- Prepare data for machine learning
-------------------------------------------------------"""
from extract_all_data import extract_src_data
from prep_data import prep_data

df_src_data = extract_src_data()
df_prp_data = prep_data(df_src_data)
