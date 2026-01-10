"""-------------------------------------------------------
    MAIN PROCEDURE
        -- Extract all data from source files and merge
        -- Prepare data for machine learning
        -- Create machine learning model
        -- Diagnose model
-------------------------------------------------------"""
from extract_all_data import extract_src_data
from prep_data import prep_data
from ml_model import ml_model, model_diags


df_src_data = extract_src_data()
df_prp_data = prep_data(df_src_data)
preds, accuracy, predictors, target, df_mod_data = ml_model(df_prp_data, True)
model_diags(preds, df_mod_data, predictors, target, True)
