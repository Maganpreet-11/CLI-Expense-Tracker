import json
def load_expenses():
    global expenses
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except:
        expenses = []

def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

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
    save_expenses()
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
        save_expenses()
        print(f"🗑️ Deleted: ₹{removed['amount']} - {removed['category']}\n")
    else:
        print("❌ Invalid index!\n")

def edit_expense():
    if not expenses:
        print("⚠️ No expenses to edit.\n")
        return
    
    view_expenses()

    try:
        index = int(input("Enter expense number to edit: ")) - 1
    except ValueError:
        print("❌ Please enter a valid number.\n")
        return
    
    # Check if index is valid BEFORE asking for new data
    if 0 <= index < len(expenses):
        try:
            amount = float(input("Enter new amount: ₹"))
            if amount <= 0:
                print("❌ Amount must be greater than 0.\n")
                return
        except ValueError:
            print("❌ Invalid amount! Please enter a number.\n")
            return

        category = input("Enter new category: ").strip()
        if not category:
            print("❌ Category cannot be empty.\n")
            return
        
        expense = {
            "amount" : amount,
            "category" : category
        }
        
        expenses[index] = expense
        save_expenses()
        print("✅ Expense updated successfully!\n")
    else:
        print("❌ Invalid index!\n")

def filter_by_category():
    if not expenses:
        print("⚠️ No expenses.\n")
        return
    
    category = input("Enter the category to filter: ").strip().lower()
    found = False
    
    print(f"\n🔍 Results for '{category}':")
    for item in expenses:
        # Compare the lowercase version of the saved category
        if item["category"].lower() == category:
            print(f"- ₹{item['amount']}")
            found = True
            
    if not found:
        print(f"❌ No expenses found in the '{category}' category.")
    print() # Add an empty line for clean spacing

def show_menu():
    print("===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Edit Expense")
    print("5. View by Category")
    print("6. Exit")

def main():
    load_expenses()
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
            edit_expense()
        elif choice == "5":
            filter_by_category()
        elif choice == '6':
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
