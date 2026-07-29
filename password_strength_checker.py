def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(not char.isalnum() for char in password):
        score += 1

    if score == 5:
        return "Strong 💪"
    elif score >= 3:
        return "Medium 👍"
    else:
        return "Weak ❌"


password = input("Enter a password: ")
print("Password Strength:", check_password_strength(password))
