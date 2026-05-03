# 🐍 Python Assignments 1 & 2

A collection of Python programming exercises covering core language fundamentals and data structures, organized into two assignments.

---

## 📁 Project Structure

```
python-assignment-1_2-main/
├── Assignment-1/
│   ├── Conditions/
│   ├── Data-Types/
│   ├── For-Loop/
│   ├── Match-Case/
│   ├── Nested-Conditions/
│   ├── Operators/
│   ├── Shorthand/
│   ├── Type-Casting/
│   ├── Variables/
│   └── While-Loop/
├── Assignment-2/
│   └── (20 exercise files)
├── Data/
│   ├── data.xlsx
│   └── write.xlsx
└── main.py
```

---

## 📘 Assignment 1 — Python Fundamentals

### 🔢 Variables
| File | Description |
|------|-------------|
| `Variables-1.py` | Declares multiple variables of different types (str, int, float, list, bool) using multiple assignment |
| `Variables-2.py` | Calculates the area of a circle using `π` and radius |

### 🧮 Operators
| File | Description |
|------|-------------|
| `Operators-1.py` | Demonstrates arithmetic operators (+, -, *, /, %) on two numbers |
| `Operators-2.py` | Compares two user-input numbers using comparison operators |
| `Operators-3.py` | Checks if a number is between 10 and 50 using `and` operator |
| `Operators-4.py` | Checks divisibility by 3, 5, or both using logical operators |

### 🏷️ Data Types
| File | Description |
|------|-------------|
| `Date-Types-1.py` | Prints variables of types str, int, float, and bool with `type()` |
| `Data-Types-2.py` | Detects the type of user input (int, float, bool, or str) using `try/except` |
| `Data-Types-3.py` | Converts a string `"100"` to int and multiplies it |

### 🔄 Type Casting
| File | Description |
|------|-------------|
| `Type-Casting-1.py` | Converts a float to int (truncation) |
| `Type-Casting-2.py` | Reads a string input, converts to int, and adds 10 |

### ✅ Conditions
| File | Description |
|------|-------------|
| `Conditions-1.py` | Checks if a number is Positive, Negative, or Zero |
| `Conditions-2.py` | Finds the greater of two numbers |
| `Conditions-3.py` | Checks if a number is Even or Odd |
| `Conditions-4.py` | Assigns a grade (A/B/C/Fail) based on marks |
| `Conditions-5.py` | Determines if a year is a Leap Year |

### 🪆 Nested Conditions
| File | Description |
|------|-------------|
| `Nested-Conditions-1.py` | Finds the largest of three numbers |
| `Nested-Conditions-2.py` | Checks divisibility by 2 and/or 3 |
| `Nested-Conditions-3.py` | Simulates a simple login system with email and password |
| `Nested-Conditions-4.py` | Checks job eligibility based on age and degree |
| `Nested-Conditions-5.py` | Assigns ticket price category based on age |

### ⚡ Shorthand (Ternary Operator)
| File | Description |
|------|-------------|
| `Shorthand-1.py` | Even or Odd check using ternary |
| `Shorthand-2.py` | Pass or Fail check using ternary |
| `Shorthand-3.py` | Finds maximum of two numbers using ternary |
| `Shorthand-4.py` | Positive or Negative check using ternary |
| `Shorthand-5.py` | Divisibility by 5 check using ternary |

### 🔀 Match-Case
| File | Description |
|------|-------------|
| `Match-Case-1.py` | Calculator using `match` on operator symbols (+, -, *, /, ^) |
| `Match-Case-2.py` | Returns day name from a number (1–7) |
| `Match-Case-3.py` | Interactive menu-driven Add/Subtract calculator with loop |
| `Match-Case-4.py` | Maps grade letter (A/B/C) to a descriptive message |
| `Match-Case-5.py` | Classifies a character as Vowel, Consonant, or Digit |

### 🔁 For Loop
| File | Description |
|------|-------------|
| `For-Loop-1.py` | Prints numbers 1 to 10 |
| `For-Loop-2.py` | Prints even numbers from 1 to 20 |
| `For-Loop-3.py` | Calculates the sum of numbers from 1 to N |
| `For-Loop-4.py` | Counts vowels in a user-input string |

### 🔃 While Loop
| File | Description |
|------|-------------|
| `While-Loop-1.py` | Countdown from 10 to 1 |
| `While-Loop-2.py` | Calculates factorial using a while loop |
| `While-Loop-3.py` | Repeats input until user types `exit` |

---

## 📗 Assignment 2 — Data Structures & File Handling

| # | File | Description |
|---|------|-------------|
| 1 | `1-Prime-Number.py` | Optimized prime checker using 6k±1 algorithm; tests a list of numbers |
| 2 | `2-Factorial-Number.py` | Iterative factorial function; handles negative numbers and edge cases |
| 3 | `3-Vowel_Count.py` | Counts words in a sentence that start with a vowel |
| 4 | `4-List-Length.py` | Manually calculates list length without using `len()` |
| 5 | `5-Even-Number-Remove.py` | Removes even numbers from a list |
| 6 | `6-Common-Element.py` | Finds common elements between two lists using two-pointer technique |
| 7 | `7-Convert-List-Set.py` | Converts a list to a `set` (removes duplicates) and a `tuple` |
| 8 | `8-Different-Value-Set.py` | Finds the difference between two sets using `-` operator |
| 9 | `9-Sub-Set-Verify.py` | Checks if one set is a subset of another using `.issubset()` |
| 10 | `10-Tuple-Access.py` | Converts a tuple to list, modifies it, and converts back to tuple |
| 11 | `11-Tuple-List.py` | Converts a tuple directly to a list |
| 12 | `12-Tuple-Min-Max.py` | Finds the min and max values in a tuple |
| 13 | `13-Merge-Two-List_Dict.py` | Zips two lists (keys & values) into a dictionary |
| 14 | `14-Count-Frequency.py` | Counts character frequency in a string using a dictionary |
| 15 | `15-Merge-Two-Dict.py` | Merges two dictionaries using `.copy()` and `.update()` |
| 16 | `16-Sort-Keys.py` | Sorts a dictionary by keys alphabetically |
| 17 | `17-Sort-Values.py` | Sorts a dictionary by values numerically |
| 18 | `18-Read-Excel-File.py` | Reads an Excel file (`data.xlsx`) using `pandas` |
| 19 | `19-Write-Excel-File.py` | Creates a DataFrame and writes it to `write.xlsx` |
| 20 | `20-Excel-File-Update.py` | Reads an Excel file, updates a cell value, and saves it |

---

## 🛠️ Requirements

**Python 3.10+** is required (for `match`/`case` syntax used in Assignment 1).

For Assignment 2 Excel tasks, install `pandas` and `openpyxl`:

```bash
pip install pandas openpyxl
```

---

## ▶️ How to Run

```bash
# Clone or extract the project
cd python-assignment-1_2-main

# Run any exercise
python Assignment-1/Conditions/Conditions-1.py
python Assignment-2/1-Prime-Number.py
```

> **Note:** Excel-related scripts (18–20) expect the `Data/` folder to be present at the project root with `data.xlsx` inside.

---

## 💡 Topics Covered

`Variables` · `Data Types` · `Type Casting` · `Operators` · `Conditions` · `Nested Conditions` · `Shorthand / Ternary` · `Match-Case` · `For Loop` · `While Loop` · `Functions` · `Lists` · `Tuples` · `Sets` · `Dictionaries` · `Excel File I/O (pandas)`
