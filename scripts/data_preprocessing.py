#social_media_preprocessing_review
# Load the social media CSV and inspect basic structure for the project writeup
import pandas as pd

file_path = '../data/social media - social_media_10000_outliers_duplicates.csv'

social_df = pd.read_csv(file_path, encoding='ascii')

print(social_df.head())
print(social_df.describe(include='all'))
