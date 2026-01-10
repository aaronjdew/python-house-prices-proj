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
from global_functions import get_boolean_input

inp_improve_model = get_boolean_input(
    "Would you like to try to improve the model using last years data averages?")

inp_diag_imp = get_boolean_input(
    "Would you like to include the importance mean in the diagnostics return?")

df_src_data = extract_src_data()
df_prp_data = prep_data(df_src_data)
preds, accuracy, predictors, target, df_mod_data = ml_model(
    df_prp_data, inp_improve_model)
model_diags(preds, df_mod_data, predictors, target, inp_diag_imp)
