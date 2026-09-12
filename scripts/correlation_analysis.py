# Compute and visualize correlation matrix for key numeric variables in the social media dataset

from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

DATA_PATH = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "social media - social_media_10000_outliers_duplicates.csv"
)

social_df = pd.read_csv(DATA_PATH, encoding="ascii")

# Add a few derived metrics
social_df['engagement'] = social_df['likes'] + social_df['comments'] + social_df['shares']

num_cols = ['impressions','reach','likes','comments','shares','clicks','conversions','Duration_seconds','Paid_Amount_INR','engagement']

corr_matrix = social_df[num_cols].corr()

plt.figure(figsize=(10,8))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', square=True)
plt.title('Correlation Matrix of Key Social Media Metrics')
plt.tight_layout()
plt.show()

print(corr_matrix.head())
