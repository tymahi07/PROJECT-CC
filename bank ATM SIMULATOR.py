balance = 1000 
transactions = [] 


def display_balance():
    print(f"\n💰 Current Balance: ₹{balance}")


def deposit_money():
    global balance
    amount = float(input("Enter amount to deposit: ₹"))
    
    if amount > 0:
        balance += amount
        transactions.append(f"Deposited ₹{amount}")
        print("✅ Deposit successful!")
    else:
        print("❌ Invalid amount!")


def withdraw_money():
    global balance
    amount = float(input("Enter amount to withdraw: ₹"))
    
    if amount <= 0:
        print("❌ Invalid amount!")
    elif amount > balance:
        print("❌ Insufficient balance!")
    else:
        balance -= amount
        transactions.append(f"Withdrew ₹{amount}")
        print("✅ Withdrawal successful!")


def show_statement():
    print("\n📄 Transaction Statement:")
    if not transactions:
        print("No transactions yet.")
    else:
        for i, t in enumerate(transactions, 1):
            print(f"{i}. {t}")


def atm_menu():
    while True:
        print("\n====== ATM MENU ======")
        print("1. Display Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Statement")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_balance()
        elif choice == '2':
            deposit_money()
        elif choice == '3':
            withdraw_money()
        elif choice == '4':
            show_statement()
        elif choice == '5':
            print("👋 Thank you for using the ATM!")
            break
        else:
            print("❌ Invalid choice! Try again.")



atm_menu()
