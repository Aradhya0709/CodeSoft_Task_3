import random
import string

def generate_password(length):
    if length < 4:  # Minimum length to include all character types
        return "Password length should be at least 4 characters."

    # Define possible characters for the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure at least one character from each category
    password = [
        random.choice(string.ascii_uppercase),  # One uppercase letter
        random.choice(string.ascii_lowercase),  # One lowercase letter
        random.choice(string.digits),           # One digit
        random.choice(string.punctuation)       # One special character
    ]

    # Generate remaining characters randomly
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Convert list to string
    return ''.join(password)

def main():
    print("Password Generator")
    
    # Get desired password length from the user
    try:
        length = int(input("Enter the desired password length: "))
        # Generate password based on the specified length
        password = generate_password(length)
        # Display the generated password
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
