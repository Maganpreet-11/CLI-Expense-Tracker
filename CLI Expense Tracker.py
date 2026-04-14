expenses = []

def add_expenses():
    try:
        amount = float(input("Enter amount: ₹"))
        if amount <= 0:
            print("❌ Amount must be greater than 0.\n")
            return
    except ValueError:
        print("❌ Invalid amount! Please enter a number.\n")
        return

    category = input("Enter category: ").strip()
    if not category:
        print("❌ Category cannot be empty.\n")
        return

    expense = {
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    print("✅ Expense added successfully!\n")


def view_expenses():
    if not expenses:
        print("⚠️ No expenses recorded.\n")
        return 
    
    print("\n📄 All Expenses:")
    total = 0

    for i, exp in enumerate(expenses):
        print(f"{i+1}. ₹{exp['amount']} - {exp['category']}")
        total += exp['amount']

    print(f"\n💰 Total Expenses: ₹{total}\n")


def delete_expense():
    if not expenses:
        print("⚠️ No expenses to delete.\n")
        return
    
    view_expenses()

    try:
        index = int(input("Enter expense number to delete: ")) - 1
    except ValueError:
        print("❌ Please enter a valid number.\n")
        return

    if 0 <= index < len(expenses):
        removed = expenses.pop(index)
        print(f"🗑️ Deleted: ₹{removed['amount']} - {removed['category']}\n")
    else:
        print("❌ Invalid index!\n")


def show_menu():
    print("===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expenses()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()
