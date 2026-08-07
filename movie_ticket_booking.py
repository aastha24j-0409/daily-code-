# Day 42 - Movie Ticket Booking System

print("=== Movie Ticket Booking ===")

name = input("Enter your name: ")
movie = input("Enter movie name: ")
tickets = int(input("Enter number of tickets: "))

ticket_price = 12.50
total = tickets * ticket_price

# Apply discount
if tickets >= 5:
    discount = total * 0.10
else:
    discount = 0

final_amount = total - discount

print("\n===== Booking Summary =====")
print(f"Customer Name : {name}")
print(f"Movie          : {movie}")
print(f"Tickets        : {tickets}")
print(f"Price/Ticket   : ${ticket_price:.2f}")
print(f"Total Price    : ${total:.2f}")
print(f"Discount       : ${discount:.2f}")
print(f"Amount to Pay  : ${final_amount:.2f}")

print("\nEnjoy your movie! 🍿")
print("==========================")
