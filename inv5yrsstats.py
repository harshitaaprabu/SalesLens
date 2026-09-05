# # import pandas lib as pd
# import pandas as pd

# # read by default 1st sheet of an excel file
# dataframe1 = pd.read_excel("inv_5yrs.xlsx")

# print(dataframe1)



# import pandas as pd
# df = pd.read_excel("C:\Users\harsh\Downloads\inv_5yrs.xlsx")
# print(df.mean())
# print(df.std())



# import os 
# dir_path = "C:/Users/harsh/OneDrive/Desktop"
# filename in os.listdir(dir_path)
# if filename.endswith('xlsx'):
#     file_path = os.path.join(dir_path, inv_5yrs.xlsx)
#     workbook = openpyx1.load_-workbook(file_path)
#     print(workbook)


import pandas as pd
df = pd.read_excel('inv_5yrs.xlsx')
print(df.head())


# import os
# print(os.getcwd())

# To find product with most revenue
# df['Revenue'] = df['amount'] * df['qty']
# revenue_by_product = df.groupby('sinvno')['Revenue'].sum()
# # Identify the product with the maximum revenue
# max_revenue_product = revenue_by_product.idxmax()
# max_revenue_value = revenue_by_product.max()
# print(f'The product with the most revenue is {max_revenue_product} with a revenue of {max_revenue_value}.')

 

# # to find the month with most revenue
# df['sinvdate'] = pd.to_datetime(df['sinvdate'])
# # Extract the month from the 'Date' column
# df['Month'] = df['sinvdate'].dt.month
# # Group by month and sum the revenues
# revenue_by_month = df.groupby('Month')['Revenue'].sum()
# # Identify the month with the maximum revenue
# max_revenue_month = revenue_by_month.idxmax()
# max_revenue_value = revenue_by_month.max()
# print(f'The month with the most revenue is {max_revenue_month} with a revenue of {max_revenue_value}.')


# # to find customer with most revenue
# revenue_by_customer = df.groupby('custid')['Revenue'].sum()
# # Identify the customer with the maximum revenue
# max_revenue_customer = revenue_by_customer.idxmax()
# max_revenue_value = revenue_by_customer.max()
# print(f'The customer with the most revenue is {max_revenue_customer} with a revenue of {max_revenue_value}.')

# # to find the day with most revenue
# df['sinvdate'] = pd.to_datetime(df['sinvdate'])
# # Group by day (date) and sum the revenues
# revenue_by_day = df.groupby('sinvdate')['Revenue'].sum()
# # Identify the day with the maximum revenue
# max_revenue_day = revenue_by_day.idxmax()
# max_revenue_value = revenue_by_day.max()
# print(f'The day with the most revenue is {max_revenue_day.strftime("%Y-%m-%d")} with a revenue of {max_revenue_value}.')


# # To find the product with most number of units sold
# grouped_df = df.groupby('itemcode')['qty'].sum().reset_index()

# # Step 5: Find the product with the maximum quantity sold
# max_product = grouped_df.loc[grouped_df['qty'].idxmax()]

# # Output the result
# print(f"The product with the most quantity sold is '{max_product['itemcode']}' with {max_product['qty']} units sold.")


# # Forecasting Sales
# import pandas as pd
# import statsmodels.api as sm
# from statsmodels.tsa.arima.model import ARIMA
# import matplotlib.pyplot as plt

# # Step 3: Prepare the data
# df['sinvdate'] = pd.to_datetime(df['sinvdate'])
# df_grouped = df.groupby(['sinvdate', 'itemcode'])['qty'].sum().reset_index()
# df_pivot = df_grouped.pivot(index='sinvdate', columns='itemcode', values='qty').fillna(0)

# # Step 4: Forecasting the sales
# forecasts = {}
# for product in df_pivot.columns:
#     model = ARIMA(df_pivot[product], order=(5, 1, 0))
#     model_fit = model.fit()
#     forecast = model_fit.forecast(steps=12)  # Forecasting the next 12 periods
#     forecasts[product] = forecast

# forecast_df = pd.DataFrame(forecasts)
# # Step 5: Determine which product will be sold more
# total_forecasted_sales = forecast_df.sum()
# top_product = total_forecasted_sales.idxmax()

# print(f"The product expected to sell the most is '{top_product}' with an estimated {total_forecasted_sales[top_product]} units.")

# # Step 6: Plot the forecasted sales
# forecast_df.plot(figsize=(10, 6))
# plt.title('Forecasted Sales for Each Product')
# plt.xlabel('sinvdate')
# plt.ylabel('qty')
# plt.legend(title='Products')
# plt.show()

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_excel("inv_5yrs.xlsx", sheet_name="inv_5yrs")

# Basic overview
print("Dataset Shape:", df.shape)
print("\nMissing Values:\n", df.isnull().sum())
print("\nData Types:\n", df.dtypes)

# Handle missing data (if needed)
df = df.dropna(subset=["custid", "sinvdate", "amount"])  # Drop key missing rows

# Create year & month columns
df['year'] = df['sinvdate'].dt.year
df['month'] = df['sinvdate'].dt.month_name()

# ---- Summary Statistics ----
print("\nDescriptive Stats:\n", df.describe())

# ---- 1. Sales Trend Over Time ----
sales_trend = df.groupby('sinvdate')['amount'].sum().reset_index()
plt.figure(figsize=(12,6))
sns.lineplot(data=sales_trend, x='sinvdate', y='amount')
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales Amount")
plt.show()

# ---- 2. Sales by Year ----
plt.figure(figsize=(8,5))
sns.barplot(x='year', y='amount', data=df, estimator='sum', ci=None)
plt.title("Yearly Sales Amount")
plt.show()

# ---- 3. Top 10 Customers by Revenue ----
top_customers = df.groupby('custid')['amount'].sum().nlargest(10).reset_index()
plt.figure(figsize=(10,5))
sns.barplot(data=top_customers, x='custid', y='amount', palette='viridis')
plt.title("Top 10 Customers by Sales")
plt.xticks(rotation=45)
plt.show()

# ---- 4. Top 10 Selling Items ----
top_items = df.groupby('itemcode')['qty'].sum().nlargest(10).reset_index()
plt.figure(figsize=(10,5))
sns.barplot(data=top_items, x='itemcode', y='qty', palette='mako')
plt.title("Top 10 Selling Items (by Quantity)")
plt.xticks(rotation=45)
plt.show()

# ---- 5. Monthly Seasonality ----
monthly_sales = df.groupby('month')['amount'].sum().reindex([
    'January','February','March','April','May','June','July',
    'August','September','October','November','December'])
plt.figure(figsize=(10,5))
sns.barplot(x=monthly_sales.index, y=monthly_sales.values)
plt.title("Monthly Sales Seasonality")
plt.xticks(rotation=45)
plt.show()

# ---- 6. Correlation Heatmap ----
plt.figure(figsize=(5,4))
sns.heatmap(df[['qty','amount']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation between Quantity and Amount")
plt.show()
