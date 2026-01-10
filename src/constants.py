"""-------------------------------------------------------
    PROJECT CONFIG FILE FOR CONSTANTS
-------------------------------------------------------"""

from typing import Final

# --- File Path ---
# US CPI Inflation Measure | Monthly
FP_CPI_CSV: Final[str] = "data/CPIAUCSL.csv"
# Rental Vacancy rate | Quarterly
FP_RVR_CSV: Final[str] = "data/RRVRUSQ156N.csv"
# Mortgage Interest Rates | Weekly
FP_MIR_CSV: Final[str] = "data/MORTGAGE30US.csv"
# Zillow Median Sales Prices
FP_SAP_CSV: Final[str] = "data/Metro_median_sale_price_uc_sfrcondo_sm_week.csv"
# Zillow Home Value Index
FP_HVI_CSV: Final[str] = "data/Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_month.csv"

# -- DATA EXTRACTION ---
# Column Names - "interest rate", "vacancy rate", "inflation measure", "price", "value"
COL_SRC_DATA: Final[list[str]] = [
    "interest", "vacancy", "cpi", "price", "value"]

# Common Column Name
COL_COMMON: Final[str] = "monyr"
# Common Column Period Type
COL_COMMON_PT: Final[str] = "M"

# -- DATA PREPARATION ---
# Column Names - "interest rate", "vacancy rate", "adjusted price",
#                "adjusted value", "future price prediction",
#                "is future price prediction greater than adjusted price"
COL_PRP_DATA: Final[list[str]] = [
    "interest", "vacancy", "adj_price", "adj_value", "nxt_qtr_price", "change"]

# US CPI Inflation Multiplier
CPI_MULTI: Final[int] = 100

# Future price shifted row number
ROW_PRICE_SHIFT: Final[int] = -13

# -- ML MODEL ---

# Number of Weeks used for backtesting
BT_WEEKS: Final[int] = 260

# Number of Weeks used for backtesting (STEP)
BT_STEP: Final[int] = 52

# -- Optional: Use Last Year Avgs --
# Improve accuracy by rolling back number of weeks
IMP_ACC_ROLL: Final[int] = 52

# Improve accuracy by rolling back number of weeks (header)
IMP_ACC_HDR: Final[str] = "_year"
