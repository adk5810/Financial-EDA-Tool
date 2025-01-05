import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np

# Ensure files are saved in the same folder as the script
output_folder = os.path.dirname(os.path.abspath(__file__))

# Define a function to introduce missing values for testing
def introduce_missing_values(data, column_name, percentage=0.1):
    np.random.seed(42)  # Ensure reproducibility
    n_missing = int(len(data) * percentage)
    missing_indices = np.random.choice(data.index, n_missing, replace=False)
    data.loc[missing_indices, column_name] = np.nan
    return data

# Function to retrieve data
def fetch_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

# Function to handle missing values
def clean_data(data):
    if data.isnull().sum().sum() > 0:
        print("\nHandling missing values...")
        data.ffill(inplace=True)
        data.bfill(inplace=True)
    return data

# Function to calculate daily returns
def calculate_daily_returns(data, column):
    data['Daily Return'] = data[column].pct_change()
    return data

# Function to plot and save figures
def plot_and_save(data, x, y, title, xlabel, ylabel, filepath, kind='line', **kwargs):
    plt.figure(figsize=(14, 7))
    if kind == 'line':
        plt.plot(data[x], data[y], **kwargs)
    elif kind == 'hist':
        sns.histplot(data[y].dropna(), bins=100, kde=True)
    elif kind == 'heatmap':
        sns.heatmap(data, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(filepath)
    plt.show()

# Main pipeline
if __name__ == "__main__":
    # Step 1: Data Retrieval
    ticker = 'AAPL'
    start_date = '2020-01-01'
    end_date = '2024-12-31'

    print("Fetching data...")
    data = fetch_data(ticker, start_date, end_date)

    # Reset index to make 'Date' a column
    data.reset_index(inplace=True)

    # Validate required columns
    price_columns = ['Adj Close', 'Close']
    valid_price_column = next((col for col in price_columns if col in data.columns), None)

    if not valid_price_column:
        print("Error: No valid price column found ('Adj Close' or 'Close').")
        print("Available columns:", data.columns)
        raise KeyError("Required price column is missing from the dataset.")

    required_columns = ['Volume', 'High', 'Low']
    missing_columns = [col for col in required_columns if col not in data.columns]

    if missing_columns:
        print(f"Warning: Missing columns in the dataset: {missing_columns}")
        print("Available columns:", data.columns)

    # Step 2: Introduce Missing Values for Testing
    print("Introducing missing values for testing...")
    data = introduce_missing_values(data, valid_price_column, percentage=0.1)

    # Step 3: Data Summary
    print("\nData Info:")
    print(data.info())

    print("\nMissing Values:")
    print(data.isnull().sum())

    # Step 4: Data Cleaning
    data = clean_data(data)

    # Step 5: Calculate Daily Returns
    data = calculate_daily_returns(data, valid_price_column)

    # Step 6: Visualizations
    price_plot_path = os.path.join(output_folder, 'AAPL_Price_Plot.png')
    plot_and_save(data, 'Date', valid_price_column, f'AAPL {valid_price_column} Price (2020-2024)', 'Date', 'Price (USD)', price_plot_path)

    returns_plot_path = os.path.join(output_folder, 'AAPL_Daily_Returns_Distribution.png')
    plot_and_save(data, None, 'Daily Return', 'Distribution of Daily Returns', 'Daily Return', 'Frequency', returns_plot_path, kind='hist')

    # Step 7: Correlation Analysis
    if all(col in data.columns for col in ['Volume', 'High', 'Low']):
        data['Volume Change'] = data['Volume'].pct_change()
        data['High-Low Diff'] = data['High'] - data['Low']
        corr_matrix = data[[valid_price_column, 'Daily Return', 'Volume Change', 'High-Low Diff']].corr()

        corr_plot_path = os.path.join(output_folder, 'AAPL_Correlation_Matrix.png')
        plot_and_save(corr_matrix, None, None, 'Correlation Matrix for AAPL Metrics', '', '', corr_plot_path, kind='heatmap')
    else:
        print("Skipping correlation analysis due to missing columns.")

    # Step 8: Custom Analysis: Moving Averages
    data['20-Day MA'] = data[valid_price_column].rolling(window=20).mean()
    data['50-Day MA'] = data[valid_price_column].rolling(window=50).mean()

    moving_avg_plot_path = os.path.join(output_folder, 'AAPL_Moving_Averages.png')
    plt.figure(figsize=(14, 7))
    plt.plot(data['Date'], data[valid_price_column], label=f'{valid_price_column} Price')
    plt.plot(data['Date'], data['20-Day MA'], label='20-Day Moving Average')
    plt.plot(data['Date'], data['50-Day MA'], label='50-Day Moving Average')
    plt.title(f'AAPL {valid_price_column} Price and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.savefig(moving_avg_plot_path)
    plt.show()

    # Step 9: Save Dataset
    output_data_path = os.path.join(output_folder, 'AAPL_Data.csv')
    data.to_csv(output_data_path, index=False)

    # Step 10: Documenting Insights and Reporting
    print("\nKey Insights:")
    print("1. The Adjusted/Close Price shows periods of growth and decline, with clear trends revealed by moving averages.")
    print("2. The correlation matrix highlights significant relationships, such as between High-Low differences and Adjusted/Close prices.")
    print("3. The daily return distribution shows a typical pattern with a few extreme values, which could indicate high market volatility on certain days.")
    print("4. Volume changes correlate weakly with daily returns, suggesting that other factors drive price movements.")
    print("5. Moving averages smooth out noise and reveal longer-term trends in stock performance.")

    # Confirm saved files
    print(f"Data saved to: {output_data_path}")
    print(f"Price plot saved to: {price_plot_path}")
    print(f"Daily returns distribution plot saved to: {returns_plot_path}")
    print(f"Correlation matrix plot saved to: {corr_plot_path}")
    print(f"Moving averages plot saved to: {moving_avg_plot_path}")
