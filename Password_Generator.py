import random
import string

def generate_password(length):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

    # Ensure at least one from each category
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special)
    ]

    all_characters = uppercase + lowercase + digits + special

    # Fill remaining characters
    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    random.shuffle(password)
    return ''.join(password)


# ---- User Input ----
allowed_lengths = [4, 6, 12, 16]
length = int(input("Enter password length (4 / 6 / 12 / 16): "))

if length not in allowed_lengths:
    print("Invalid length! Please choose 4, 6, 12, or 16.")
else:
    print("Generated Password:", generate_password(length))
