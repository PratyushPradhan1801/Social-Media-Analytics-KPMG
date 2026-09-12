# Compute skewness of all numeric columns in the social media dataset
from pathlib import Path
import pandas as pd

DATA_PATH = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "social media - social_media_10000_outliers_duplicates.csv"
)

try:
    social_df
except NameError:
    social_df = pd.read_csv(DATA_PATH, encoding="ascii")

numeric_cols = social_df.select_dtypes(include=['number'])
skewness_series = numeric_cols.skew()

print(skewness_series)
