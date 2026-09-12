# Social Media Analytics & Data Quality Assessment

Python-based analysis of an AI-generated social media dataset, covering data quality assessment, statistical analysis, and KPI exploration.

## Objective

To analyse social media performance data, identify data-quality issues, examine relationships between key metrics, and explore platform-level KPIs.

## Dataset

The project uses an AI-generated social media dataset containing post-level performance metrics such as:

- Impressions
- Reach
- Likes
- Comments
- Shares
- Clicks
- Conversions
- Duration
- Paid Amount
- Platform
- Content Type
- Promotion Type
- Post Theme
- Time Posted

## Analysis Performed

### Data Quality Assessment
- Dataset structure and descriptive statistics
- Duplicate-row detection
- Missing and blank-value analysis
- Skewness analysis of numeric variables

### Statistical Analysis
- Correlation analysis across key social media metrics
- Derived engagement metric using likes, comments, and shares

### KPI Analysis
The project explores 10 KPI questions, including:

- Total impressions by platform
- Total engagement by platform
- Average engagement rate by platform
- Impressions vs. engagement
- Reach vs. conversions
- Average CTR by platform
- Conversion per click by platform
- Paid amount vs. impressions
- Duration vs. engagement
- Average engagement by content type

## Visualizations

The analysis outputs are available in the [`outputs/`](./outputs) folder.

They include:

- Platform-level performance comparisons
- Engagement and conversion analysis
- CTR and conversion-per-click comparisons
- Relationship-based scatter plots
- Content-type performance analysis
- Duplicate-record visualization

## Key Insights

- Facebook recorded the highest total impressions and total engagement among the analysed platforms.
- YouTube showed the highest average CTR and conversion-per-click in the platform comparison.
- Image content generated the highest average engagement among the analysed content types.
- Impressions and engagement showed a positive relationship, while higher reach was generally associated with higher conversions.
- The dataset required data-quality assessment for duplicate records, missing values, and skewed numeric variables.

## Tools & Technologies

- Python
- Pandas
- Matplotlib
- Seaborn
- Data Analysis
- Data Visualization

## Project Structure

```text
Social-Media-Analytics-KPMG/
├── data/
│   └── social media - social_media_10000_outliers_duplicates.csv
│
├── scripts/
│   ├── correlation_analysis.py
│   ├── data_preprocessing.py
│   ├── duplicate_detection.py
│   ├── kpi_analysis.py
│   ├── missing_value_analysis.py
│   └── skewness_analysis.py
│
├── outputs/
│   ├── duplicate_rows_screenshot.png
│   ├── total_impressions_by_platform.png
│   ├── total_engagement_by_platform.png
│   ├── average_engagement_rate_by_platform.png
│   ├── impressions_vs_engagement.png
│   ├── reach_vs_conversions.png
│   ├── average_ctr_by_platform.png
│   ├── average_conversion_per_click_by_platform.png
│   ├── paid_amount_vs_impressions.png
│   ├── duration_vs_engagement.png
│   └── average_engagement_by_content_type.png
│
└── README.md
