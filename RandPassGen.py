import random
import string
import pyperclip

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars):
    # Define the character sets based on user preferences
    character_set = ""
    if use_uppercase:
        character_set += string.ascii_uppercase
    if use_lowercase:
        character_set += string.ascii_lowercase
    if use_numbers:
        character_set += string.digits
    if use_special_chars:
        character_set += string.punctuation

    # Generate the password
    password = "".join(random.choice(character_set) for _ in range(length))
    return password

def main():
    # Get user preferences
    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
    use_numbers = input("Include numbers? (y/n): ").lower() == "y"
    use_special_chars = input("Include special characters? (y/n): ").lower() == "y"

    # Generate the password
    password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars)

    # Display the password
    print("Generated Password:", password)

    # Copy password to clipboard
    pyperclip.copy(password)
    print("Password copied to clipboard.")

if __name__ == "__main__":
    main()