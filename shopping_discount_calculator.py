# Day 39 - Shopping Discount Calculator

print("=== Shopping Discount Calculator ===")

customer_name = input("Enter customer name: ")
purchase_amount = float(input("Enter purchase amount: $"))

# Determine discount
if purchase_amount >= 500:
    discount_percent = 20
elif purchase_amount >= 300:
    discount_percent = 15
elif purchase_amount >= 100:
    discount_percent = 10
else:
    discount_percent = 0

# Calculate discount
discount_amount = purchase_amount * (discount_percent / 100)
final_price = purchase_amount - discount_amount

# Display receipt
print("\n=== Purchase Summary ===")
print(f"Customer: {customer_name}")
print(f"Original Price: ${purchase_amount:.2f}")
print(f"Discount: {discount_percent}%")
print(f"Discount Amount: ${discount_amount:.2f}")
print(f"Final Price: ${final_price:.2f}")

if discount_percent > 0:
    print("Congratulations! You received a discount.")
else:
    print("Spend $100 or more to receive a discount.")

print("============================")
