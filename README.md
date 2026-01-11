# Predict US House Prices

In this project, using data from the Federal Reserve and Zillow, I train a model to predict future house prices. \
All data is prepared and combined and then used to train a random forest model. The model will predict if house prices will increase or decrease in the future. \
Backtesting is used to avoid data leakage and I included the option to improve the model with new predictors. <br>

This project can be customized to predict house prices in your metro area if you live in the US.

## Python Packages

The following was used to create this project: \
(For a full list of installed packages and versions check the 'requirements.txt' file in this project)

- Python 3.14.2
- Main Python Packages
  - pandas
  - scikit-learn
  - matplotlib

## Data Sources

Data was sourced from the following resources:

- Federal Reserve Data
  - [Consumer Price Index](https://fred.stlouisfed.org/series/CPIAUCSL) - CPIAUCSL.csv
  - [Rental Vacancy Rate](https://fred.stlouisfed.org/series/RRVRUSQ156N) - RRVRUSQ156N.csv
  - [Mortgage Interest Rate](https://fred.stlouisfed.org/series/MORTGAGE30US) - MORTGAGE30US.csv
- Zillow Data
  - [Median Sales](https://fred.stlouisfed.org/series/CPIAUCSL) - Metro_median_sale_price_uc_sfrcondo_sm_week.csv
  - [Home Value Index](https://fred.stlouisfed.org/series/RRVRUSQ156N) - Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_month.csv
