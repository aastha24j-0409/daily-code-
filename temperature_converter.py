# Day 40 - Temperature Converter

print("=== Temperature Converter ===")

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Choose an option (1 or 2): ")

if choice == "1":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32

    print("\n=== Result ===")
    print(f"{celsius:.2f}°C = {fahrenheit:.2f}°F")

elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9

    print("\n=== Result ===")
    print(f"{fahrenheit:.2f}°F = {celsius:.2f}°C")

else:
    print("Invalid choice. Please run the program again and select 1 or 2.")

print("==============================")
