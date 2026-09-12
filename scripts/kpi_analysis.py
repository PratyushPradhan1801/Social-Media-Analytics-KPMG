# Create 10 KPI questions & answers with supporting bar and scatter plots

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

DATA_PATH = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "social media - social_media_10000_outliers_duplicates.csv"
)

social_df = pd.read_csv(DATA_PATH, encoding="ascii")

# Ensure engagement metrics exist
social_df['engagement'] = social_df['likes'] + social_df['comments'] + social_df['shares']
social_df['eng_rate'] = (social_df['engagement'] / social_df['reach']).replace([float('inf'), -float('inf')], 0).fillna(0)

# 1) KPI: Total impressions by platform (bar)
platform_impr = social_df.groupby('platform')['impressions'].sum().reset_index()
plt.figure(figsize=(6,4))
sns.barplot(data=platform_impr, x='platform', y='impressions', palette='Blues_d')
plt.title('Total Impressions by Platform')
plt.tight_layout()
plt.show()

# 2) KPI: Total engagement by platform (bar)
platform_eng = social_df.groupby('platform')['engagement'].sum().reset_index()
plt.figure(figsize=(6,4))
sns.barplot(data=platform_eng, x='platform', y='engagement', palette='Greens_d')
plt.title('Total Engagement by Platform')
plt.tight_layout()
plt.show()

# 3) KPI: Average engagement rate by platform (bar)
platform_rate = social_df.groupby('platform')['eng_rate'].mean().reset_index()
plt.figure(figsize=(6,4))
sns.barplot(data=platform_rate, x='platform', y='eng_rate', palette='Oranges_d')
plt.title('Average Engagement Rate by Platform')
plt.tight_layout()
plt.show()

# 4) KPI: Relationship between impressions and engagement (scatter)
plt.figure(figsize=(6,4))
sns.scatterplot(data=social_df.sample(1000, random_state=0), x='impressions', y='engagement', alpha=0.4)
plt.title('Scatter: Impressions vs Engagement')
plt.tight_layout()
plt.show()

# 5) KPI: Relationship between reach and conversions (scatter)
plt.figure(figsize=(6,4))
sns.scatterplot(data=social_df.sample(1000, random_state=1), x='reach', y='conversions', alpha=0.4, color='purple')
plt.title('Scatter: Reach vs Conversions')
plt.tight_layout()
plt.show()

# 6) KPI: Click-through rate by platform (bar)
social_df['ctr'] = (social_df['clicks'] / social_df['impressions']).replace([float('inf'), -float('inf')], 0).fillna(0)
platform_ctr = social_df.groupby('platform')['ctr'].mean().reset_index()
plt.figure(figsize=(6,4))
sns.barplot(data=platform_ctr, x='platform', y='ctr', palette='Reds_d')
plt.title('Average CTR by Platform')
plt.tight_layout()
plt.show()

# 7) KPI: Conversions per click (conversion rate) by platform (bar)
social_df['conv_rate'] = (social_df['conversions'] / social_df['clicks']).replace([float('inf'), -float('inf')], 0).fillna(0)
platform_conv_rate = social_df.groupby('platform')['conv_rate'].mean().reset_index()
plt.figure(figsize=(6,4))
sns.barplot(data=platform_conv_rate, x='platform', y='conv_rate', palette='Purples_d')
plt.title('Avg Conversion per Click by Platform')
plt.tight_layout()
plt.show()

# 8) KPI: Does paid amount drive impressions? (scatter)
plt.figure(figsize=(6,4))
sns.scatterplot(data=social_df.sample(1000, random_state=2), x='Paid_Amount_INR', y='impressions', alpha=0.4, color='teal')
plt.title('Scatter: Paid Amount vs Impressions')
plt.tight_layout()
plt.show()

# 9) KPI: Does video duration influence engagement? (scatter)
plt.figure(figsize=(6,4))
sns.scatterplot(data=social_df.sample(1000, random_state=3), x='Duration_seconds', y='engagement', alpha=0.4, color='brown')
plt.title('Scatter: Duration vs Engagement')
plt.tight_layout()
plt.show()

# 10) KPI: Engagement by content type (bar)
content_eng = social_df.groupby('content_type')['engagement'].mean().reset_index()
plt.figure(figsize=(6,4))
sns.barplot(data=content_eng, x='content_type', y='engagement', palette='cubehelix')
plt.title('Average Engagement by Content Type')
plt.tight_layout()
plt.show()
