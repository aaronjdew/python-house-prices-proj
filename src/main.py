"""-------------------------------------------------------
    MAIN PROCEDURE
        -- Extract all data from source files and merge
        -- Prepare data for machine learning
        -- Create machine learning model
-------------------------------------------------------"""
from extract_all_data import extract_src_data
from prep_data import prep_data
from ml_model import ml_model, model_diags


df_src_data = extract_src_data()
df_prp_data = prep_data(df_src_data)
preds, accuracy, target = ml_model(df_prp_data, False)
