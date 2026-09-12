# Count blank (missing or empty-string) values in each column of the social_df dataframe
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

# Treat NaN and empty strings as blanks
blank_counts = social_df.isna().sum()
empty_string_counts = (social_df.astype(str).apply(lambda col: col.str.strip() == '')).sum()

total_blank_like = blank_counts + empty_string_counts

print(blank_counts)
print(empty_string_counts)
print(total_blank_like)
