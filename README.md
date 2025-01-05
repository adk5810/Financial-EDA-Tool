# Financial Data Analysis Tool

## Overview
This Python project provides a comprehensive framework for analyzing financial data, specifically historical stock performance. It includes features for data retrieval, cleaning, visualization, and analysis, making it suitable for both academic and professional purposes.

## Features
1. **Data Retrieval**:
   - Downloads historical stock data using the Yahoo Finance API via the `yfinance` library.

2. **Data Cleaning**:
   - Handles missing values using forward and backward filling techniques.

3. **Calculations**:
   - Computes daily returns to analyze stock volatility.
   - Calculates moving averages to identify long-term trends.

4. **Visualizations**:
   - Plots stock prices, moving averages, and distribution of daily returns.
   - Generates a heatmap for correlation analysis of key financial metrics.

5. **Dynamic Handling of Missing Data**:
   - Introduces missing values for testing the robustness of cleaning methods.

## Use Cases
- Analyze historical stock performance.
- Study price trends and volatility for investment decisions.
- Generate insights into financial correlations.

## Prerequisites
- Python 3.7 or higher
- Libraries:
  - `yfinance`
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `numpy`

## Installation
Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Open the `financial_eda_tool.py` file in your code editor.
2. Modify the `ticker`, `start_date`, and `end_date` variables to specify the stock and date range you wish to analyze.
3. Run the script:
   ```bash
   python financial_eda_tool.py
   ```
4. Generated plots and the processed dataset will be saved in the same directory as the script.

## Outputs
- **CSV File**:
  - Cleaned and processed dataset with additional metrics such as daily returns and moving averages.
- **Plots**:
  - Stock price trends.
  - Distribution of daily returns.
  - Correlation heatmap for financial metrics.
  - Moving averages comparison.

## File Descriptions
- `financial_eda_tool.py`: Main Python script for data retrieval, cleaning, visualization, and analysis.
- `requirements.txt`: List of required Python libraries.
- `README.md`: Documentation for the project.

## Example Configuration
```python
# User-defined parameters
ticker = 'AAPL'           # Stock ticker symbol
start_date = '2020-01-01' # Start date for analysis
end_date = '2024-12-31'   # End date for analysis
```

## Contribution
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push the branch:
   ```bash
   git push origin feature-name
   ```
4. Submit a pull request with a detailed description of your changes.

## Acknowledgements
- Yahoo Finance API for providing free financial data.
- Open-source Python libraries for enabling robust data analysis.

## Contact
For any questions or feedback, please reach out to:
- **Name**: Aditya Kadam
- **Email**: adi5810@gmail.com
- **GitHub**: https://github.com/adk5810

