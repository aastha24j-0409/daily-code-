# Day 41 - Simple Bank Account Simulator

print("=== Simple Bank Account ===")

name = input("Enter account holder's name: ")
balance = float(input("Enter current balance: $"))

print("\nChoose an option:")
print("1. Deposit")
print("2. Withdraw")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    amount = float(input("Enter deposit amount: $"))
    balance += amount
    print(f"\nSuccessfully deposited ${amount:.2f}")

elif choice == "2":
    amount = float(input("Enter withdrawal amount: $"))

    if amount <= balance:
        balance -= amount
        print(f"\nSuccessfully withdrew ${amount:.2f}")
    else:
        print("\nInsufficient balance!")

else:
    print("\nInvalid option!")

print("\n===== Account Summary =====")
print(f"Account Holder: {name}")
print(f"Available Balance: ${balance:.2f}")
print("===========================")
