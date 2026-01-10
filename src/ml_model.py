"""-------------------------------------------------------
    Create machine learning model
        -- func: Machine Learning Model
        -- func: Run Predictions
        -- func: Backtest data
-------------------------------------------------------"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score as ac
from sklearn.inspection import permutation_importance as pi
import constants as cn


def ml_model(df_prp_data: pd.DataFrame, use_lst_yr_avg: bool) -> tuple[np.ndarray, float, list, str, pd.DataFrame]:
    """---------------------------------------------------
    ML model to predict house prices
        -- Return the predictions and accuracy
    ---------------------------------------------------"""
    df_hse_data = df_prp_data

    # Predictor columns
    predictors = cn.COL_PRP_DATA[0:4]

    # target column
    target = cn.COL_PRP_DATA[5]

    if use_lst_yr_avg:
        # OPTIONAL: Aim to increase accuracy by averaging last year

        # Get the last years averages
        yearly = df_hse_data.rolling(cn.IMP_ACC_ROLL, min_periods=1).mean()

        # Create yearly ratio column headers
        yearly_ratios = [p + cn.IMP_ACC_HDR for p in predictors]

        # Create yearly ratio column data
        df_hse_data[yearly_ratios] = df_hse_data[predictors] / \
            yearly[predictors]

        # Run predictions
        preds, accuracy = backtest(
            df_hse_data, predictors + yearly_ratios, target)
    else:
        # Run predictions
        preds, accuracy = backtest(df_hse_data, predictors, target)

    return preds, accuracy, predictors, target, df_hse_data


def predict(train: pd.DataFrame, test: pd.DataFrame, predictors: list, target: str) -> np.ndarray:
    """---------------------------------------------------
    Run prediction
    ---------------------------------------------------"""
    rf = RandomForestClassifier(min_samples_split=10, random_state=1)
    rf.fit(train[predictors], train[target])
    preds = rf.predict(test[predictors])
    return preds


def backtest(df_hse_data: pd.DataFrame, predictors: list, target: str) -> tuple[np.ndarray, float]:
    """---------------------------------------------------
    Back test against past data to avoid data leakage
    (Predict the past using future data)
    ---------------------------------------------------"""
    all_preds = []

    # Make predictions using number of weeks to predict the step
    for i in range(cn.BT_WEEKS, df_hse_data.shape[0], cn.BT_STEP):
        train = df_hse_data.iloc[:i]
        test = df_hse_data.iloc[i:(i + cn.BT_STEP)]
        all_preds.append(predict(train, test, predictors, target))

    # Concate all numpy array predictions
    preds = np.concatenate(all_preds)

    return preds, ac(df_hse_data.iloc[cn.BT_WEEKS:][target], preds)


def model_diags(preds: np.ndarray, df_mod_data: pd.DataFrame, predictors: list, target: str, show_perm: bool) -> None:
    """---------------------------------------------------
    Run model diagnostics
    ---------------------------------------------------"""

    if show_perm:
        rf = RandomForestClassifier(min_samples_split=10, random_state=1)
        rf.fit(df_mod_data[predictors], df_mod_data[target])
        result = pi(rf, df_mod_data[predictors],
                    df_mod_data[target], n_repeats=10, random_state=1)
        print(result["importances_mean"])

    # Create a series of prediction matches against the results
    s_pred_match = preds == df_mod_data[target].iloc[cn.BT_WEEKS:]

    # Create a plot data dataframe
    df_plot_data = df_mod_data.iloc[cn.BT_WEEKS:].copy()

    # Create scatter graph
    df_plot_data.reset_index().plot.scatter(
        x="index", y="adj_price", c=s_pred_match)

    # Show scatter
    plt.show()


if __name__ == "__main__":
    print("This module is intended for import only")
