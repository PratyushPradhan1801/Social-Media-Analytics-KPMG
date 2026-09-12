# Count blank (missing or empty-string) values in each column of the social_df dataframe
import pandas as pd

# Ensure social_df exists
try:
    social_df
except NameError: 
    pd.read_csv('../data/social media - social_media_10000_outliers_duplicates.csv', encoding='ascii')

# Treat NaN and empty strings as blanks
blank_counts = social_df.isna().sum()
empty_string_counts = (social_df.astype(str).apply(lambda col: col.str.strip() == '')).sum()

total_blank_like = blank_counts + empty_string_counts

print(blank_counts)
print(empty_string_counts)
print(total_blank_like)
