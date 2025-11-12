import pandas as pd
import matplotlib.pyplot as plt
import os

# Create file if it doesn't exist
if not os.path.exists("expenses.csv"):
    df = pd.DataFrame(columns=["Date", "Category", "Amount"])
    df.to_csv("expenses.csv", index=False)

def add_expense(date, category, amount):
    df = pd.read_csv("expenses.csv")
    new_entry = pd.DataFrame([[date, category, amount]], columns=df.columns)
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv("expenses.csv", index=False)
    print("✅ Expense added successfully!")

def view_summary():
    df = pd.read_csv("expenses.csv")
    if df.empty:
        print("No expenses recorded yet.")
        return
    print("\n=== Monthly Summary ===")
    print(df.groupby("Category")["Amount"].sum())

def show_chart():
    df = pd.read_csv("expenses.csv")
    if df.empty:
        print("No data to display.")
        return
    df.groupby("Category")["Amount"].sum().plot(kind="bar", color="skyblue")
    plt.title("Spending by Category")
    plt.ylabel("Amount")
    plt.show()

# Menu
while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Summary")
    print("3. Show Chart")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category (Food, Transport, etc): ")
        amount = float(input("Enter amount: "))
        add_expense(date, category, amount)

    elif choice == "2":
        view_summary()

    elif choice == "3":
        show_chart()

    elif choice == "4":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice, try again.")
