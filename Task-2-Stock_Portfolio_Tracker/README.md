# 📈 Stock Portfolio Tracker

> **A simple and beginner-friendly Python application to calculate and track stock portfolio investments.**

The **Stock Portfolio Tracker** is a command-line Python project that allows users to enter stock symbols and quantities, calculate individual investments, and determine the **total portfolio value**.

The project also generates a `portfolio_summary.txt` file containing the complete investment summary for future reference.

---

## ✨ Features

* 📝 Easy-to-use command-line input
* 📊 Predefined stock price database
* 💰 Calculates investment value for each stock
* 📈 Calculates total portfolio investment
* ⚠️ Handles invalid stock symbols
* 📄 Automatically generates a portfolio summary file
* 🔄 Supports multiple stocks in a single portfolio
* 💻 Simple and beginner-friendly implementation

---

## 🛠️ Technologies Used

| Technology                    | Purpose                   |
| ----------------------------- | ------------------------- |
| 🐍 **Python 3**               | Core programming language |
| 📚 **Dictionary**             | Store stock prices        |
| 🔁 **Loops**                  | Process multiple stocks   |
| 🔀 **Conditional Statements** | Validate stock symbols    |
| 📁 **File Handling**          | Save portfolio summary    |

---

## 💹 Available Stocks

The application currently uses the following predefined stock prices:

| Stock Symbol | Price |
| ------------ | ----: |
| 🍎 AAPL      |  $180 |
| 🚗 TSLA      |  $250 |
| 🔎 GOOGL     |  $140 |
| 💻 MSFT      |  $320 |
| 📦 AMZN      |  $150 |

> **Note:** These are predefined/demo prices and are not live market prices.

---

## ⚙️ How It Works

The application follows a simple workflow:

```text
        ┌─────────────────────┐
        │ Start Application   │
        └──────────┬──────────┘
                   ↓
        ┌─────────────────────┐
        │ Enter Number of     │
        │ Stocks              │
        └──────────┬──────────┘
                   ↓
        ┌─────────────────────┐
        │ Enter Stock Symbol  │
        │ & Quantity           │
        └──────────┬──────────┘
                   ↓
        ┌─────────────────────┐
        │ Validate Symbol     │
        └──────────┬──────────┘
                   ↓
        ┌─────────────────────┐
        │ Calculate Investment│
        └──────────┬──────────┘
                   ↓
        ┌─────────────────────┐
        │ Calculate Total     │
        │ Portfolio Value     │
        └──────────┬──────────┘
                   ↓
        ┌─────────────────────┐
        │ Save Summary to     │
        │ Text File           │
        └─────────────────────┘
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone <repository-link>
```

### 2️⃣ Navigate to the Project

```bash
cd Stock-Portfolio-Tracker
```

### 3️⃣ Run the Program

```bash
python stock_portfolio_tracker.py
```

---

## 🖥️ Sample Execution

```text
===== 📈 Stock Portfolio Tracker =====

Enter the number of stocks you want to add: 2

Stock 1
Enter Stock Symbol: AAPL
Enter Quantity: 5

Stock 2
Enter Stock Symbol: TSLA
Enter Quantity: 3

===== 📊 Portfolio Summary =====

Stock: AAPL | Quantity: 5 | Price: $180 | Investment: $900
Stock: TSLA | Quantity: 3 | Price: $250 | Investment: $750

----------------------------------------
Total Investment Value: $1650
----------------------------------------

Portfolio summary saved successfully!
```

---

## 📄 Generated Output

After execution, the program automatically creates:

```text
portfolio_summary.txt
```

Example:

```text
===== Portfolio Summary =====

Stock: AAPL
Quantity: 5
Price: $180
Investment: $900

Stock: TSLA
Quantity: 3
Price: $250
Investment: $750

-----------------------------
Total Investment Value: $1650
-----------------------------
```

---

## 📁 Project Structure

```text
Stock-Portfolio-Tracker/
│
├── 📄 stock_portfolio_tracker.py
├── 📄 portfolio_summary.txt
└── 📄 README.md
```

---

## 🧠 Concepts Practiced

This project helped practice several important Python fundamentals:

* Variables and data types
* Dictionaries
* `for` / `while` loops
* `if-else` conditions
* User input
* Arithmetic operations
* String formatting
* File handling
* Basic input validation
* Program flow and logic

---

## 🔮 Future Improvements

The current version uses predefined stock prices. Possible future improvements include:

* 🌐 Fetching **live stock prices using an API**
* 💾 Storing portfolio data in JSON/CSV
* 📊 Adding portfolio performance charts
* 📈 Tracking profit and loss
* 🗃️ Adding a database
* 🔐 Adding user accounts
* 🖥️ Building a web interface using Flask or Django
* 📱 Creating a responsive frontend
* ☁️ Deploying the application online

---

## 🎯 Project Objective

The main objective of this project is to build a simple application while practicing **Python programming fundamentals, data structures, loops, conditional logic, input validation, and file handling**.

It is designed as a beginner-level project and can be extended into a complete **real-time portfolio management application**.

---

## 👨‍💻 Author

**Aditya Keshri**

🎓 B.Tech CSE
🐍 Python Developer | AI/ML Enthusiast
💻 GitHub: `Adityakes`

---

## ⭐ If You Like This Project

If you found this project useful, consider giving the repository a ⭐ on GitHub!

---

### 📌 Disclaimer

This project is created for **educational purposes**. The stock prices used in the application are predefined sample values and **do not represent real-time market prices or financial advice**.
