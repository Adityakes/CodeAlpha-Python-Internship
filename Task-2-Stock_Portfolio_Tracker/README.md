# Stock Portfolio Tracker

## Description
Stock Portfolio Tracker is a simple Python project that allows users to calculate the total investment value of their stock portfolio.

The program uses a predefined dictionary of stock prices. Users enter stock symbols and quantities, and the program calculates the investment value for each stock as well as the total portfolio value.

Additionally, the portfolio summary is saved to a text file for future reference.

---

## Features

- User-friendly input system
- Predefined stock price dictionary
- Calculates investment value for each stock
- Calculates total portfolio value
- Handles invalid stock symbols
- Saves portfolio summary to a text file
- Easy-to-read output

---

## Technologies Used

- Python 3
- Dictionary
- Loops
- Conditional Statements
- File Handling

---

## Stock Prices Used

| Stock Symbol | Price ($) |
|-------------|-----------|
| AAPL | 180 |
| TSLA | 250 |
| GOOGL | 140 |
| MSFT | 320 |
| AMZN | 150 |

---

## How to Run

1. Clone the repository

```bash
git clone <repository-link>
```

2. Navigate to the project folder

```bash
cd Stock-Portfolio-Tracker
```

3. Run the Python file

```bash
python stock_portfolio_tracker.py
```

---

## Sample Output

```text
===== Stock Portfolio Tracker =====

Enter the number of stocks you want to add: 2

Stock 1
Enter Stock Symbol: AAPL
Enter Quantity: 5

Stock 2
Enter Stock Symbol: TSLA
Enter Quantity: 3

===== Portfolio Summary =====

Stock: AAPL | Quantity: 5 | Price: $180 | Investment: $900
Stock: TSLA | Quantity: 3 | Price: $250 | Investment: $750

Total Investment Value: $1650
```

---

## Output File

The program automatically generates:

```text
portfolio_summary.txt
```

This file contains the complete portfolio summary and total investment value.

---

## Author

Aditya Keshri