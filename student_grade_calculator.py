# Day 38 - Student Grade Calculator

print("=== Student Grade Calculator ===")

name = input("Enter student name: ")

math = float(input("Enter Math score: "))
science = float(input("Enter Science score: "))
english = float(input("Enter English score: "))
computer = float(input("Enter Computer score: "))

total = math + science + english + computer
average = total / 4

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print("\n=== Student Report ===")
print(f"Student Name: {name}")
print(f"Math: {math}")
print(f"Science: {science}")
print(f"English: {english}")
print(f"Computer: {computer}")

print(f"\nTotal Score: {total}")
print(f"Average Score: {average:.2f}")
print(f"Final Grade: {grade}")

if average >= 60:
    print("Status: PASS")
else:
    print("Status: FAIL")

print("==========================")
