# Personal Finance Health Analyzer

A comprehensive financial health assessment tool built with Streamlit that uses proven financial formulas and algorithms to analyze your personal finances.

## Features

- **Formula-Based Analysis**: Uses industry-standard financial ratios and calculations
- **Real-Time Assessment**: Instant analysis of your financial health
- **Interactive Dashboard**: Visual charts and metrics for easy understanding
- **Personalized Recommendations**: Actionable advice based on your financial data
- **Educational Content**: Learn about financial formulas and best practices

## Financial Metrics Calculated

1. **Savings Rate**: Percentage of income saved after expenses
2. **Debt-to-Income Ratio**: Debt burden relative to income
3. **Credit Utilization**: Credit card usage vs available credit
4. **Emergency Fund Ratio**: Months of expenses covered by savings
5. **Debt-to-Asset Ratio**: Debt burden relative to total assets
6. **Financial Health Score**: Composite score combining all metrics

## Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run main.py
   ```

## Usage

1. Open the application in your browser
2. Enter your financial data in the sidebar:
   - Monthly income
   - Monthly expenses
   - Current savings
   - Monthly debt payments
   - Total debt
   - Credit card balance and limit
3. Click "Run Financial Analysis"
4. View your results, charts, and recommendations

## Formulas Used

The analyzer uses the following financial formulas:

- **Savings Rate**: `(Income - Expenses) / Income × 100`
- **Debt-to-Income Ratio**: `Debt Payments / Income × 100`
- **Credit Utilization**: `Balance / Limit × 100`
- **Emergency Fund**: `Savings / Monthly Expenses`
- **Debt-to-Asset Ratio**: `Debt / (Debt + Savings) × 100`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.
