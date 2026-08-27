# Expense Tracker

A beginner-friendly **Python Expense Tracker** that allows users to add, view, search, calculate, and delete expenses. The application also stores expenses permanently using a JSON file, so data is available even after the program is closed.

## Features

* Add new expenses
* View all saved expenses
* Calculate total expenses
* Search expenses by category
* Delete an expense
* Save expenses to a JSON file
* Load saved expenses when the application starts
* Input validation and error handling
* Interactive menu-driven interface

## Technologies Used

* **Python 3**
* **JSON**
* **VS Code**

## Python Concepts Practiced

This project was created to practice and strengthen the following Python concepts:

* Variables
* Data types
* Lists
* Dictionaries
* Functions
* `if`, `elif`, and `else`
* `while` loops
* `for` loops
* `break`
* `continue`
* `return`
* `input()`
* Type conversion using `float()` and `int()`
* String methods:

  * `strip()`
  * `lower()`
* String searching using `in`
* List methods:

  * `append()`
  * `pop()`
* `enumerate()`
* Exception handling using:

  * `try`
  * `except`
  * `ValueError`
  * `FileNotFoundError`
* Reading and writing files
* JSON data storage using:

  * `json.dump()`
  * `json.load()`
* Global variables
* Menu-driven programs

## How the Application Works

The application stores expenses inside a Python list.

Each expense is represented as a dictionary containing:

```text
amount
category
description
```

For example:

```python
{
    "amount": 500.0,
    "category": "Food",
    "description": "Lunch"
}
```

Multiple expense dictionaries are stored inside the `expenses` list.

## Main Functions

### `add_expense()`

Allows the user to enter:

* Expense amount
* Expense category
* Expense description

The function validates the amount and prevents invalid or empty input.

### `view_expenses()`

Displays all saved expenses along with their expense number, amount, category, and description.

### `calculate_total()`

Loops through all expenses and calculates the total amount spent.

### `search_expense()`

Allows the user to search for expenses using their category.

The search is case-insensitive, so `Food`, `food`, and `FOOD` can be matched.

### `delete_expense()`

Allows the user to select an expense number and remove it from the list.

The `pop()` method is used to remove the selected expense.

### `save_expenses()`

Saves the current expenses list into `expenses.json` using `json.dump()`.

### `load_expenses()`

Loads previously saved expenses from `expenses.json` using `json.load()`.

If the JSON file does not exist, the program starts with an empty expense list.

### `main()`

Controls the application's menu and allows the user to repeatedly select different operations until they choose Exit.

## Menu

When the application starts, the user sees:

```text
===== EXPENSE TRACKER =====
1. Add expense
2. View expenses
3. Calculate total
4. Search expense
5. Delete expense
6. Exit
Enter your choice:
```

## Sample Output

```text
===== EXPENSE TRACKER =====
1. Add expense
2. View expenses
3. Calculate total
4. Search expense
5. Delete expense
6. Exit

Enter your choice: 1

Enter amount: 500
Enter category: Food
Enter description: Lunch

===== EXPENSE TRACKER =====
1. Add expense
2. View expenses
3. Calculate total
4. Search expense
5. Delete expense
6. Exit

Enter your choice: 2

Expense 1
Amount: 500.0
Category: Food
Description: Lunch
--------------------
```

### Calculate Total

```text
Enter your choice: 3

Total Expenses: 500.0
```

### Search Expense

```text
Enter your choice: 4

Enter category to search: food

Amount: 500.0
Category: Food
Description: Lunch
--------------------
```

### Delete Expense

```text
Enter your choice: 5

Enter expense number to delete: 1

Deleted: Lunch
```

### Exit

```text
Enter your choice: 6

Thank you for using Expense Tracker!
```

## Error Handling

The application handles several types of invalid input.

### Invalid Amount

If the user enters:

```text
Enter amount: abc
```

the application displays:

```text
Please enter a valid number.
```

Negative or zero amounts are also rejected:

```text
Amount must be greater than 0.
```

### Empty Category

If the category is left empty:

```text
Category cannot be empty.
```

### Empty Description

If the description is left empty:

```text
Description cannot be empty.
```

### Invalid Delete Number

If the user enters an invalid expense number:

```text
Invalid expense number.
```

The application also handles non-numeric input using `try` and `except`.

## Data Persistence

The application uses a JSON file named:

```text
expenses.json
```

This allows expenses to remain saved even after the program is closed.

The data flow is:

```text
Python List
     ↓
json.dump()
     ↓
expenses.json
```

When the application starts again:

```text
expenses.json
     ↓
json.load()
     ↓
Python List
```

This means the user's expenses are not lost when the program exits.

## Project Structure

```text
Expense-Tracker/
│
├── main.py
├── expenses.json
└── README.md
```

### `main.py`

Contains the complete Python application and all functions.

### `expenses.json`

Stores the expenses permanently in JSON format.

### `README.md`

Contains the project documentation, features, technologies, concepts practiced, and usage information.

## How to Run the Project

### 1. Clone or download the project

Download the project and open the project folder in VS Code.

### 2. Make sure Python is installed

Check your Python installation using:

```text
python --version
```

### 3. Run the application

Open the VS Code terminal inside the project folder and run:

```text
python main.py
```

The Expense Tracker menu will appear in the terminal.

## Future Improvements

Possible improvements for future versions include:

* Add expense dates
* Edit existing expenses
* Filter expenses by date
* Show monthly spending
* Add category-wise totals
* Add a graphical user interface
* Add charts for expense analysis
* Export expenses to CSV
* Add a budget feature
* Add user authentication
* Add a database such as SQLite

## Learning Outcome

This project helped strengthen practical Python programming skills by combining multiple concepts into one complete application.

The project demonstrates how to:

1. Store data using lists and dictionaries.
2. Organize code using functions.
3. Use loops and conditional statements.
4. Validate user input.
5. Handle errors using exceptions.
6. Read and write files.
7. Store persistent data using JSON.
8. Build an interactive menu-driven application.
9. Combine multiple Python concepts into a real-world project.

## Author

**Shreya**

This project was created as part of my Python learning and practical project development.
