import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4."

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

while True:
    try:
        length = int(input("Enter the desired password length (or 0 to exit): "))
        if length == 0:
            print("Exiting Password Generator. Goodbye!")
            break
        print(f"Generated Password: {generate_password(length)}\n")
    except ValueError:
        print("Invalid input! Please enter a valid number.")