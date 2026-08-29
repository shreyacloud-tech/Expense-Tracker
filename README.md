# Expense Tracker

A Python-based command-line application for managing and tracking personal expenses. The application allows users to add, view, search, calculate, and delete expenses through an interactive menu.

## Features

* Add new expenses
* View all expenses
* Calculate total expenses
* Search for expenses
* Delete expenses
* Store expense data in JSON format
* Interactive command-line interface
* Dockerized application
* Automated CI using GitHub Actions

## Technologies Used

* Python 3
* JSON
* Docker
* Git
* GitHub
* GitHub Actions

## Project Structure

```text
Expense-Tracker/
│
├── main.py
├── expenses.json
├── Dockerfile
├── .gitignore
├── README.md
│
└── .github/
    └── workflows/
        └── ci.yml
```

## How the Application Works

The application provides a menu-driven interface:

```text
===== EXPENSE TRACKER =====

1. Add expense
2. View expenses
3. Calculate total
4. Search expense
5. Delete expense
6. Exit
```

The user selects an option and performs the required operation.

## Expense Data

Expenses are stored in `expenses.json`.

Each expense contains information such as:

* Expense ID
* Description
* Amount
* Category

Using JSON allows the data to be stored between program executions.

## Python Concepts Used

This project demonstrates:

* Variables
* Data types
* Strings
* Integers and floating-point numbers
* Lists
* Dictionaries
* Functions
* Function parameters
* Return values
* `if`, `elif`, and `else`
* `for` loops
* `while` loops
* `break`
* User input
* Type conversion
* Searching data
* Updating and deleting data
* JSON file handling
* Exception handling

## Running the Application Locally

Make sure Python is installed.

Check the Python version:

```bash
python --version
```

Run the application:

```bash
python main.py
```

## Docker

The application is containerized using Docker.

### Build the Docker Image

From the project directory:

```bash
docker build -t expense-tracker .
```

### Run the Docker Container

Because the application requires interactive user input, run the container using interactive mode:

```bash
docker run -it --rm expense-tracker
```

The Expense Tracker menu will appear inside the container.

### Stop the Application

Select option `6` from the menu to exit the application.

## GitHub Actions

This project uses **GitHub Actions** for Continuous Integration (CI).

The workflow is located at:

```text
.github/workflows/ci.yml
```

The workflow runs automatically when changes are pushed to the `main` branch or when a pull request is created.

### CI Pipeline

The GitHub Actions workflow:

1. Checks out the repository
2. Sets up Python 3.12
3. Installs the required `psutil` dependency
4. Checks the Python syntax using `py_compile`

The workflow helps verify that the Python application can be checked automatically whenever changes are pushed.

## Git Workflow

The project is managed using Git and GitHub.

Common commands used during development:

```bash
git status
git add .
git commit -m "Update project"
git push
```

## What I Learned

Through this project, I practiced building a complete Python command-line application and managing data using JSON.

I also learned how to containerize a Python application using Docker and automate basic testing and validation using GitHub Actions.

This project helped me understand how application development can be combined with basic DevOps practices such as version control, containerization, and continuous integration.

## Future Improvements

Possible improvements include:

* Add expense categories and filtering
* Add monthly expense reports
* Export expenses to CSV
* Add graphical charts
* Connect the application to a database
* Add automated unit tests
* Create a web-based interface
* Deploy the application to the cloud

## Author

Salla Shreya

## Project Status

Completed
