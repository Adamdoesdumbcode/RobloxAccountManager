import json
import os
import random
import string

class RobloxAccount:
    def __init__(self, username, password, level, money, style, fruit):
        self.username = username
        self.password = password
        self.level = level
        self.money = money
        self.style = style
        self.fruit = fruit

    def __str__(self):
        return f"Username: {self.username}, Level: {self.level}, Money: {self.money}, Style: {self.style}, Fruit: {self.fruit}"

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "level": self.level,
            "money": self.money,
            "style": self.style,
            "fruit": self.fruit
        }

    @staticmethod
    def from_dict(data):
        return RobloxAccount(
            username=data["username"],
            password=data["password"],
            level=data["level"],
            money=data["money"],
            style=data["style"],
            fruit=data["fruit"]
        )

# File to store data
DATA_FILE = #add the FULL FILE  PATH to your json file
# List to store accounts
accounts = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_accounts():
    global accounts
    try:
        print(f"Loading accounts from {os.path.abspath(DATA_FILE)}")  # Print the absolute path for debugging
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as file:
                data = json.load(file)
                accounts = [RobloxAccount.from_dict(acc) for acc in data]
                print(f"Loaded {len(accounts)} accounts from file.")
        else:
            print("No saved data found. Starting fresh.")
    except json.JSONDecodeError:
        print("Corrupted data file. Starting fresh.")
    except Exception as e:
        print(f"An error occurred while loading accounts: {e}")

def save_accounts():
    try:
        print(f"Saving accounts to {os.path.abspath(DATA_FILE)}")  # Print the absolute path for debugging
        with open(DATA_FILE, "w") as file:
            json.dump([account.to_dict() for account in accounts], file, indent=4)  # Add indent for readability
        print("Accounts saved successfully!")
    except PermissionError:
        print("Permission denied: Unable to save accounts. Please check file permissions or try running as administrator.")
    except Exception as e:
        print(f"An unexpected error occurred while saving: {e}")

def generate_random_username():
    words = ["Blue", "Tiger", "Fox", "Shadow", "Light", "Moon", "Star", "Cloud", "Hunter", "Wolf"]
    return random.choice(words) + random.choice(words) + random.choice(words) + str(random.randint(100, 999))

def generate_random_password():
    length = random.randint(8, 20)
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(characters) for _ in range(length))

def add_account():
    username = generate_random_username()
    password = generate_random_password()
    level = input("Enter starting level: ")
    money = input("Enter starting money: ")
    style = input("Enter starting style: ")
    fruit = input("Enter starting fruit: ")
    accounts.append(RobloxAccount(username, password, level, money, style, fruit))
    print(f"Account added successfully!\nUsername: {username}\nPassword: {password}")
    save_accounts()

def delete_account():
    if not accounts:
        print("No accounts available to delete.")
        return
    view_accounts()
    try:
        choice = int(input("Select an account to delete (by number): ")) - 1
        if 0 <= choice < len(accounts):
            deleted = accounts.pop(choice)
            print(f"Deleted Account: {deleted.username}")
            save_accounts()
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

def view_accounts():
    if not accounts:
        print("No accounts available.")
        return
    for idx, account in enumerate(accounts):
        print(f"{idx + 1}. Username: {account.username}, Password: {account.password}, Level: {account.level}, Money: {account.money}, Style: {account.style}, Fruit: {account.fruit}")

def manage_account():
    if not accounts:
        print("No accounts available to manage.")
        return
    view_accounts()
    try:
        choice = int(input("Select an account to manage (by number): ")) - 1
        if 0 <= choice < len(accounts):
            account = accounts[choice]
            print(f"\nSelected Account:\nUsername: {account.username}\nLevel: {account.level}\nMoney: {account.money}\nStyle: {account.style}\nFruit: {account.fruit}")
            print("Options: 1. Update Level, 2. Update Money, 3. Update Style, 4. Update Fruit, 5. Show Password, 6. Delete Account")
            option = input("Choose an option: ")
            if option == "1":
                account.level = input("Enter new level: ")
                print("Level updated successfully!")
                save_accounts()
            elif option == "2":
                account.money = input("Enter new money amount: ")
                print("Money updated successfully!")
                save_accounts()
            elif option == "3":
                account.style = input("Enter new style: ")
                print("Style updated successfully!")
                save_accounts()
            elif option == "4":
                account.fruit = input("Enter new fruit: ")
                print("Fruit updated successfully!")
                save_accounts()
            elif option == "5":
                print(f"Password: {account.password}")
            elif option == "6":
                accounts.pop(choice)
                print("Account deleted successfully!")
                save_accounts()
            else:
                print("Invalid option.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    load_accounts()
    while True:
        clear_screen()
        print("\nRoblox Account Manager")
        print("1. Add Account")
        print("2. View Accounts")
        print("3. Manage Account")
        print("4. Delete Account")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_account()
        elif choice == "2":
            view_accounts()
            input("\nPress Enter to return to the menu...")
        elif choice == "3":
            manage_account()
            input("\nPress Enter to return to the menu...")
        elif choice == "4":
            delete_account()
            input("\nPress Enter to return to the menu...")
        elif choice == "5":
            print("Exiting...")
            save_accounts()
            break
        else:
            print("Invalid choice. Please try again.")
            input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        input("\nPress Enter to close the program...")
