def encrypts(text, shift):
    encrypted = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted


def decrypts(text, shift):
    return encrypt(text, -shift)  # Just use encrypt with negative shift


def get_code():
    text = input("Enter the text: ")
    while True:
        try:
            shift = int(input("Enter the number  value (0-25): "))
            if 0 <= shift <= 25:
                break
            else:
                print("Please enter a number between 0 and 25.")
        except ValueError:
            print("Please enter a valid number.")
    return text, shift


def menu():
    print("=== Caesar Cipher Menu ===")
    print("1. Encrypt text")
    print("2. Decrypt text")
    print("3. Exit")


def main():
    while True:
        menu()
        choice = input("Choose an option (1/2/3): ")
        
        if choice == '1':
            text, shift = get_code()
            print("Encrypted Text:", encrypts(text, shift))
        elif choice == '2':
            text, shift = get_code()
            print("Decrypted Text:", decrypts(text, shift))
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
        print()  # blank line for better readability


if __name__ == "__main__":
    main()
