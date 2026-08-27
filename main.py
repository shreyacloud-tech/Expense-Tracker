import json
expenses=[]
def add_expense():
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            break
        except ValueError:
            print("Please enter a valid number.")
    category=input("Enter category: ").strip()
    while not category:
        print("category cannot be empty.")
        category = input("Enter category: ").strip()
    description=input("Enter description: ").strip()
    while not description:
        print("Description cannot be empty.")
        description = input("Enter description: ").strip()
    expense={"amount":amount,"category":category,"description":description}
    expenses.append(expense)
def view_expense():
    if not expenses:
        print("No expenses found.")
        return
    for index, expense in enumerate(expenses,start=1):
        print("Amount:",expense["amount"])
        print("Category:",expense["category"])
        print("Description:",expense["description"])
        print("-------------------------------------")
def calculate_total():
    total=0
    for expense in expenses:
        total +=expense["amount"]
    print("Total Expenses:",total)
def search_expense():
    search=input("Enter category to search:").lower()
    found=False
    for expense in expenses:
        if expense["category"].lower()==search:
            print("Amount:",expense["amount"])
            print("category:",expense["category"])
            print("description:",expense["description"])
            print("--------------------------------------")
            found=True
    if not found:
        print("No expenses found")
def delete_expense():
    if not expenses:
        print("No expenses found.")
        return

    view_expense()
    try:
        choice = int(input("Enter expense number to delete: "))
    except ValueError:
        print("Please enter a valid number")

    if choice < 1 or choice > len(expenses):
        print("Invalid expense number.")
        return

    deleted = expenses.pop(choice - 1)

    print("Deleted:", deleted["description"])
def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)
def load_expenses():
    global expenses

    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []
def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)
def load_expenses():
    global expenses

    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []
def main():
    load_expenses()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Calculate total")
        print("4. Search expense")
        print("5. Delete expense")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense()
            save_expenses()

        elif choice == "2":
            view_expense()

        elif choice == "3":
            calculate_total()

        elif choice == "4":
            search_expense()

        elif choice == "5":
            delete_expense()
            save_expenses()

        elif choice == "6":
            save_expenses()
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")
main()