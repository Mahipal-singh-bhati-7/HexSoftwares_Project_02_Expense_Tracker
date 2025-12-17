expenses = []

while True:
    print("\n--- EXPENSE TRACKER ---")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Category-wise Summary")
    print("4. Total Expense")
    print("5. Exit")

    choice = input("Choose (1-5): ")

    if choice == "1":
        name = input("Expense name: ")
        amount = int(input("Amount :₹ "))
        category = input("Category (Food, Travel, etc): ")
        date = input("Date (DD-MM-YYYY): ")

        expense = {
            "name": name,
            "amount": amount,
            "category": category,
            "date": date
        }

        expenses.append(expense)
        print("✅ Expense Added")

    elif choice == "2":
        print("\nAll Expenses:")
        for e in expenses:
            print(e["date"], "|", e["name"], "|", e["category"], "|", e["amount"])

    elif choice == "3":
        summary = {}

        for e in expenses:
            cat = e["category"]
            summary[cat] = summary.get(cat, 0) + e["amount"]

        print("\nCategory-wise Summary:")
        for cat, amt in summary.items():
            print(cat, ":", amt)

    elif choice == "4":
        total = 0
        for e in expenses:
            total += e["amount"]
        print("💰 Total Expense:", total)

    elif choice == "5":
        print("👋 Project Ended")
        break

    else:
        print("❌ Invalid Choice")
