import getpass
import re

def check_password_strength(password):
    strength = 0
    suggestions = []

    if len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Use at least 8 characters")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        suggestions.append("Add an uppercase letter")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        suggestions.append("Add a lowercase letter")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        suggestions.append("Add a number")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        suggestions.append("Add a special character")

    return strength, suggestions

def show_strength_meter(strength):
    meter = ["[-----]", "[#----]", "[##---]", "[###--]", "[####-]", "[#####]"]
    print(f"\nStrength Meter: {meter[strength]} ({strength}/5)")
    if strength < 5:
        print("Suggestions to improve:")
        for s in suggestions:
            print(f" - {s}")

if __name__ == "__main__":
    print("Enter your password to check its strength:")
    password = getpass.getpass("Password: ")

    strength, suggestions = check_password_strength(password)
    show_strength_meter(strength)
