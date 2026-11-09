
expenses = []

def add_expense():
    print("\n--- Add New Expense ---")

    category = input("Enter expense category: ")
    amount = float(input("Enter amount (Rs.): "))
    description = input("Enter description: ")

    expense = {
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense)

    print("Expense added successfully!")


def view_expenses():
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses recorded yet.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(f"\nExpense {i}")
        print("Category:", expense["category"])
        print("Amount: Rs.", expense["amount"])
        print("Description:", expense["description"])


def calculate_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("\nTotal Expenses: Rs.", total)


def category_summary():
    print("\n--- Category Summary ---")

    if not expenses:
        print("No expenses recorded yet.")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    for category, total in summary.items():
        print(category, ": Rs.", total)


def main():
    while True:
        print("\n====== STUDENT EXPENSE TRACKER ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total Expenses")
        print("4. Category-wise Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            calculate_total()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
