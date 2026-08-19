# 📧 Email Address Extractor

## 📌 Project Overview

**Email Address Extractor** is a Python automation project that scans a text file and automatically extracts valid email addresses using **Regular Expressions (Regex)**.

The program removes duplicate email addresses, sorts the extracted emails alphabetically, displays the results in the terminal, and saves the final list into a separate output file.

This project demonstrates practical use of **Python file handling, Regular Expressions, functions, exception handling, data processing, and automation**.

---

## 🎯 Project Objective

The main objective of this project is to automate the process of finding email addresses from unstructured text.

Instead of manually searching through a large text file, the program automatically:

1. Reads the input file.
2. Detects email addresses using Regex.
3. Removes duplicate addresses.
4. Sorts the results alphabetically.
5. Displays the extracted emails.
6. Saves them into an output file.

---

## 🚀 Features

* 📄 Read text from an input file
* 🔍 Extract valid email addresses using Regex
* ♻️ Remove duplicate email addresses
* 🔤 Sort emails alphabetically
* 💾 Save results to an output file
* 🖥️ Display extracted emails in the terminal
* ⚠️ Handle missing input files
* 🛡️ Handle file-related exceptions
* 🧩 Uses modular functions for clean code

---

## 🛠️ Technologies Used

| Technology         | Purpose                         |
| ------------------ | ------------------------------- |
| Python 3           | Core programming language       |
| `re` module        | Email pattern matching          |
| File Handling      | Reading and writing text files  |
| Functions          | Modular program structure       |
| Exception Handling | Handling unexpected file errors |

---

## 📂 Project Structure

```text
Task-3-Email-Extractor/
│
├── email_extractor.py
├── input.txt
├── emails.txt
└── README.md
```

### File Description

**`email_extractor.py`**

Contains the main Python program and extraction logic.

**`input.txt`**

Contains the source text from which email addresses are extracted.

**`emails.txt`**

Stores the final list of unique and sorted email addresses.

**`README.md`**

Contains project documentation and usage instructions.

---

## ⚙️ How the Program Works

```text
              Start
                │
                ▼
        Read input.txt
                │
                ▼
       Search using Regex
                │
                ▼
       Extract Email IDs
                │
                ▼
       Remove Duplicates
                │
                ▼
      Sort Alphabetically
                │
                ▼
       Display on Terminal
                │
                ▼
        Save to emails.txt
                │
                ▼
               End
```

---

## ▶️ How to Run

### Step 1 — Open Terminal

Open Command Prompt or PowerShell.

### Step 2 — Navigate to the Project

```bash
cd Task-3-Email-Extractor
```

### Step 3 — Run the Program

```bash
python email_extractor.py
```

---

## 📄 Input File

The program reads text from:

```text
input.txt
```

Example:

```text
Contact us at aditya@example.com
For support use support@example.com
You can also reach aditya@example.com
Send your queries to hello@company.org
```

---

## 📄 Output File

The extracted email addresses are saved to:

```text
emails.txt
```

Example output:

```text
aditya@example.com
hello@company.org
support@example.com
```

Duplicate email addresses are automatically removed.

---

## 🔍 Regular Expression

The project uses Python's built-in `re` module to identify email addresses from text.

A general email pattern is used to identify common formats such as:

```text
example@gmail.com
user.name@company.org
contact123@example.co.in
```

---

## 🛡️ Error Handling

The program handles common errors such as:

* Input file not found
* Empty input file
* File reading errors
* File writing errors
* Unexpected exceptions

This prevents the program from crashing unexpectedly and provides useful information to the user.

---

## 🧪 Manual Testing

### Test Case 1 — Valid Emails

**Input:**

```text
hello@gmail.com
admin@company.com
```

**Expected Result:**

Both email addresses should be extracted.

**Status:** Passed

---

### Test Case 2 — Duplicate Emails

**Input:**

```text
hello@gmail.com
hello@gmail.com
admin@company.com
```

**Expected Result:**

Only one occurrence of `hello@gmail.com` should appear in the output.

**Status:** Passed

---

### Test Case 3 — No Email Address

**Input:**

```text
This file does not contain any email address.
```

**Expected Result:**

No email addresses should be extracted.

**Status:** Passed

---

### Test Case 4 — Missing Input File

**Action:**

Delete or rename `input.txt` and run the program.

**Expected Result:**

The program should display an appropriate error message instead of crashing.

**Status:** Passed

---

## 📚 Python Concepts Demonstrated

This project demonstrates:

* Variables
* Strings
* Lists
* Sets
* Functions
* Regular Expressions
* File Handling
* `try-except`
* Loops
* Conditional Statements
* Data Processing
* Sorting

---

## 🔮 Future Improvements

The project can be extended with:

* Extracting phone numbers
* Extracting URLs
* Extracting social media links
* Supporting multiple input files
* CSV export
* Excel export
* GUI interface
* Command-line arguments
* Email domain filtering
* Large file processing

---

## 🎓 Learning Outcomes

After completing this project, the following practical skills are demonstrated:

* Working with Python Regular Expressions
* Reading and writing files
* Processing unstructured text
* Removing duplicate data
* Sorting and manipulating collections
* Implementing exception handling
* Building a small automation tool
* Structuring a Python project professionally

---

## 👨‍💻 Author

**Aditya Keshri**

Python Developer / B.Tech CSE Student

---

## 📌 Project Type

**Internship Task — Task 3**

**Project:** Email Address Extractor

**Language:** Python 3
