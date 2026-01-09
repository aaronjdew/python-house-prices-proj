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

# --- Column Names ---
COL_HSE_DATA: Final[list[str]] = [
    "interest", "vacancy", "cpi", "price", "value"]

# --- Common Column ---
# Common Column Name
COL_COMMON: Final[str] = "monyr"
# Common Column Period Type
COL_COMMON_PT: Final[str] = "M"
