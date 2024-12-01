# ADD IN YOUR OWN SEPERATE FOLDER!!!!
import json

class RobloxAccount:
    def __init__(self, username, password, level, money):
        self.username = username
        self.password = password
        self.level = level
        self.money = money

    def __str__(self):
        return f"Username: {self.username}, Level: {self.level}, Money: {self.money}"

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "level": self.level,
            "money": self.money
        }

    @staticmethod
    def from_dict(data):
        return RobloxAccount(
            username=data["username"],
            password=data["password"],
            level=data["level"],
            money=data["money"]
        )

# File to store data
DATA_FILE = "accounts.json"

# List to store accounts
accounts = []

def load_accounts():
    global accounts
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            accounts = [RobloxAccount.from_dict(acc) for acc in data]
            print(f"Loaded {len(accounts)} accounts from file.")
    except FileNotFoundError:
        print("No saved data found. Starting fresh.")
    except json.JSONDecodeError:
        print("Corrupted data file. Starting fresh.")

def save_accounts():
    with open(DATA_FILE, "w") as file:
        json.dump([account.to_dict() for account in accounts], file)
    print("Accounts saved successfully!")

def add_account():
    username = input("Enter username: ")
    password = input("Enter password: ")
    level = input("Enter level: ")
    money = input("Enter money: ")
    accounts.append(RobloxAccount(username, password, level, money))
    print("Account added successfully!")
    save_accounts()

def view_accounts():
    if not accounts:
        print("No accounts available.")
        return
    for idx, account in enumerate(accounts):
        print(f"{idx + 1}. {account}")

def manage_account():
    if not accounts:
        print("No accounts available to manage.")
        return
    view_accounts()
    try:
        choice = int(input("Select an account to manage (by number): ")) - 1
        if 0 <= choice < len(accounts):
            account = accounts[choice]
            print(f"Selected Account: {account}")
            print("Options: 1. Update Level, 2. Update Money, 3. Show Password")
            option = input("Choose an option: ")
            if option == "1":
                account.level = input("Enter new level: ")
                print("Level updated successfully!")
            elif option == "2":
                account.money = input("Enter new money amount: ")
                print("Money updated successfully!")
            elif option == "3":
                print(f"Password: {account.password}")
            else:
                print("Invalid option.")
            save_accounts()
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    load_accounts()
    while True:
        print("\nRoblox Account Manager")
        print("1. Add Account")
        print("2. View Accounts")
        print("3. Manage Account")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_account()
        elif choice == "2":
            view_accounts()
        elif choice == "3":
            manage_account()
        elif choice == "4":
            print("Exiting...")
            save_accounts()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
