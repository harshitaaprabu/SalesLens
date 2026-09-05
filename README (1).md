# 5-Year Sales Data Analysis

This project analyzes 5 years of invoice-level sales data to uncover trends, top-performing customers and products, seasonality patterns, and overall revenue behavior. It includes both a **data cleaning/exploration script** and a **cleaned, summarized Excel workbook** with pre-computed aggregates and charts.

## Contents

| File | Description |
|---|---|
| `inv5yrsstats.py` | Python script that loads raw invoice data, cleans it, and generates summary statistics and visualizations |
| `cleaned_sales_and_summaries.xlsx` | Cleaned dataset plus pre-built summary sheets (by year, by month, monthly time series, top products) and charts |

## Dataset Overview

The source data is invoice-level sales records with the following fields:

| Column | Description |
|---|---|
| custid | Customer ID |
| sinvno | Sales invoice number |
| sinvdate | Invoice date |
| itemcode | Product/item code |
| qty | Quantity sold |
| amount | Sale amount |

During cleaning, additional derived fields are added, including `sales_amount_clean`, `quantity_clean`, missing/negative value flags, and `year` / `month` / `month_name` / `month_year` breakdowns for time-based analysis.

## Workbook Structure (`cleaned_sales_and_summaries.xlsx`)

- **Cleaned_Data** — full cleaned transaction-level dataset with data-quality flags
- **Sales_By_Year** — total, count, and average sales aggregated by year
- **Sales_By_Month** — total, count, and average sales aggregated by calendar month
- **Monthly_TS** — monthly time series of cleaned sales amounts, useful for trend/forecasting analysis
- **Top_Products** — items ranked by total revenue and transaction count
- **Charts** — supporting visualizations built from the above summaries

## Analysis Performed (`inv5yrsstats.py`)

1. **Data Loading & Cleaning**
   - Load raw invoice data from Excel
   - Inspect shape, missing values, and data types
   - Drop rows with missing key fields (`custid`, `sinvdate`, `amount`)
   - Derive `year` and `month` from invoice date

2. **Summary Statistics**
   - Descriptive statistics (mean, std, etc.) across numeric columns

3. **Visualizations**
   - **Daily Sales Trend** — line plot of total sales over time
   - **Yearly Sales Amount** — bar plot of total revenue per year
   - **Top 10 Customers by Revenue** — highest-spending customers
   - **Top 10 Selling Items** — best-selling products by quantity
   - **Monthly Seasonality** — total sales aggregated by calendar month across all years
   - **Correlation Heatmap** — relationship between quantity sold and sales amount

## Tech Stack

- Python
- pandas — data loading, cleaning, and aggregation
- Matplotlib, Seaborn — visualizations
- openpyxl (via pandas) — Excel I/O

## Getting Started

### Prerequisites
```bash
pip install pandas matplotlib seaborn openpyxl
```

### Running the Script
1. Clone this repository
   ```bash
   git clone <your-repo-url>
   cd <your-repo-name>
   ```
2. Place your raw invoice file (`inv_5yrs.xlsx`) in the project directory, or point the script to `cleaned_sales_and_summaries.xlsx` if starting from the cleaned data
3. Run the script
   ```bash
   python inv5yrsstats.py
   ```

## Repository Structure

```
.
├── inv5yrsstats.py                     # Data cleaning & analysis script
├── cleaned_sales_and_summaries.xlsx    # Cleaned data + summary sheets
└── README.md                           # Project documentation
```

## Key Insights Enabled

- Which years/months drive the most revenue
- Top customers and products by sales
- Seasonal patterns in purchasing behavior
- Data quality issues (missing or negative values) flagged for review

## License

This project is open source and available for personal and educational use.
