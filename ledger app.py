# Dictionary to store transactions
ledger = []
 
def add_transaction():
    """Function to add a new transaction to the ledger."""
    # Get transaction details
    date = input("Enter the transaction date (YYYY-MM-DD): ")
    description = input("Enter a description for the transaction: ")
    amount = float(input("Enter the amount: "))
 
    # Determine if it's income or expense
    transaction_type = input("Enter 'income' or 'expense': ").lower()
 
    if transaction_type not in ['income', 'expense']:
        print("Invalid transaction type. Please enter 'income' or 'expense'.")
        return
 
    # Create a transaction dictionary
    transaction = {
        "date": date,
        "description": description,
        "amount": amount if transaction_type == 'income' else -amount,
        "type": transaction_type
    }
 
    # Add transaction to ledger
    ledger.append(transaction)
    print("Transaction added successfully!\n")
 
def view_transactions():
    """Function to display all transactions in the ledger."""
    print("\n--- Transaction Ledger ---")
    print(f"{'Date':<15}{'Description':<25}{'Type':<10}{'Amount':<10}")
    print("-" * 60)
    for transaction in ledger:
        print(f"{transaction['date']:<15}{transaction['description']:<25}{transaction['type']:<10}{transaction['amount']:<10.2f}")
    print("\n")
 
def calculate_balance():
    """Function to calculate and display the account balance."""
    total_income = sum(t['amount'] for t in ledger if t['type'] == 'income')
    total_expense = -sum(t['amount'] for t in ledger if t['type'] == 'expense')
    balance = total_income + total_expense
 
    print("\n--- Account Summary ---")
    print(f"Total Income : ${total_income:.2f}")
    print(f"Total Expenses: ${total_expense:.2f}")
    print(f"Current Balance: ${balance:.2f}\n")
 
def main():
    """Main function to display menu and execute selected actions."""
    print("Welcome to the Accounting Ledger Application")
 
    while True:
        print("\nPlease select an option:")
        print("1. Add a new transaction")
        print("2. View all transactions")
        print("3. View account balance")
        print("4. Exit")
 
        choice = input("Enter your choice: ")
 
        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            calculate_balance()
        elif choice == "4":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
 
# Run the application
if __name__ == "__main__":
    main()