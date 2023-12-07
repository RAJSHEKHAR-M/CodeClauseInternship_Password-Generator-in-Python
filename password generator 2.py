import random
import string
from colorama import init, Fore, Style

init(autoreset=True)  # Initialize Colorama for cross-platform color support

def generate_password(length=50, use_lowercase=True, use_uppercase=True, use_digits=True, use_punctuation=True):
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation

    if not any([use_lowercase, use_uppercase, use_digits, use_punctuation]):
        return Fore.RED + "Please select at least one character type."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_passphrase(words=4):
    # A simple example list of words; you might want to replace this with a larger wordlist
    word_list = ['apple', 'banana', 'orange', 'grape', 'pear', 'kiwi', 'melon', 'pineapple', 'strawberry', 'blueberry']
    
    if len(word_list) < words:
        return Fore.RED + "Word list is too short for this passphrase."

    passphrase = ' '.join(random.choice(word_list) for _ in range(words))
    return passphrase

def print_menu():
    print(Fore.GREEN + "Welcome to the Password Generator!")
    print(Fore.CYAN + "Choose an option:")
    print("1. Generate a Random Password")
    print("2. Generate a Passphrase")
    print(Fore.YELLOW + "Type 'exit' to quit.")
    print(Style.RESET_ALL)

while True:
    print_menu()
    choice = input("Enter your choice (1 or 2): ")

    if choice.lower() == 'exit':
        break
    elif choice == '1':
        length = int(input("Enter the length of the password (default is 50): "))
        password = generate_password(length)
        print(Fore.MAGENTA + "New Generated Password:", password)
    elif choice == '2':
        words = int(input("Enter the number of words for the passphrase (default is 4): "))
        passphrase = generate_passphrase(words)
        print(Fore.MAGENTA + "New Generated Passphrase:", passphrase)
    else:
        print(Fore.RED + "Invalid choice. Please select 1, 2, or type 'exit'.")
    input(Fore.GREEN + "Press Enter to continue...")
