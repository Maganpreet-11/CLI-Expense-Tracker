expenses = []

def add_expenses():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

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
    for i,exp in enumerate(expenses):
        print(f"{i+1}. ₹{exp['amount']} - {exp['category']}")
    print()

def delete_expense():
    if not expenses:
        print("⚠️ No expenses to delete.\n")
        return
    
    view_expenses()
    index = int(input("Enter expense number to delete: ")) - 1

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
        choice = input("Enter your choice: ")
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