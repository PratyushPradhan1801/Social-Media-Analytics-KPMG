#social_media_preprocessing_review
# Load the social media CSV and inspect basic structure for the project writeup
from pathlib import Path
import pandas as pd

DATA_PATH = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "social media - social_media_10000_outliers_duplicates.csv"
)

social_df = pd.read_csv(DATA_PATH, encoding="ascii")

print(social_df.head())
print(social_df.describe(include='all'))
