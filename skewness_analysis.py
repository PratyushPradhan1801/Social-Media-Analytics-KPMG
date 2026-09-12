# Compute skewness of all numeric columns in the social media dataset
import pandas as pd

# Assume social_df is already in memory; if not, load it
try:
    social_df
except NameError:
    social_df = pd.read_csv('social media - social_media_10000_outliers_duplicates.csv', encoding='ascii')

numeric_cols = social_df.select_dtypes(include=['number'])
skewness_series = numeric_cols.skew()

print(skewness_series)
