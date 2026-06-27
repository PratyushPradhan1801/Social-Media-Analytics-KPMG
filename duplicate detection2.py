# Identify duplicate rows in the social media dataset, highlight them, and save an image (screenshot-style)
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors

# Assume social_df is already loaded in memory; if not, load it
try:
    social_df
except NameError:
    social_df = pd.read_csv('social media - social_media_10000_outliers_duplicates.csv', encoding='ascii')

# Find duplicates based on all columns
duplicates_mask = social_df.duplicated(keep=False)
duplicates_df = social_df[duplicates_mask].copy()

# If there are too many duplicates, limit to first 50 for visualization
max_rows_to_show = 50
display_df = duplicates_df.head(max_rows_to_show)

# Create a color map: duplicate rows in light red, others (if any) in white
row_colors = ['#ffcccc'] * len(display_df)

fig, ax = plt.subplots(figsize=(14, 0.4 * (len(display_df) + 2)))
ax.axis('off')

# Build a table-like screenshot of duplicates
table = ax.table(
    cellText=display_df.values,
    colLabels=display_df.columns,
    loc='center',
    cellLoc='center'
)

# Apply background color to all rows (since these are all duplicates)
for i in range(1, len(display_df) + 1):
    for j in range(len(display_df.columns)):
        table[(i, j)].set_facecolor('#ffcccc')

plt.tight_layout()

screenshot_filename = 'duplicate_rows_screenshot.png'
plt.savefig(screenshot_filename, dpi=200, bbox_inches='tight')
plt.show()

print('screenshot file:', screenshot_filename)
print('duplicate_rows_count')
print(duplicates_df.shape[0])
