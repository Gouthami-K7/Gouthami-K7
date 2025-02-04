import re

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def validate_password(self):
        if len(self.password) < 9:
            return False
        if not re.search(r"[A-Z]", self.password):  
            return False
        if not re.search(r"[a-z]", self.password):  
            return False
        if not re.search(r"[\W_]", self.password): 
            return False
        return True

class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        user = User(username, password)
        if user.validate_password():
            self.users[username] = user.password
            print(f"User '{username}' registered successfully!\n")
        else:
            print(f"Error: Password for {username} is not valid.\n")

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            print(f"Login Successful! Welcome, {username}.\n")
        else:
            print("Login Failed! Invalid username or password.\n")


if __name__ == "__main__":
    passs = UserManager()

    passs.add_user("Vamshi", "VamsHi@123")
    passs.add_user("Gouthami", "Gouth9@")
    passs.add_user("Chaitanya", "Chait@nya10")
    print("--- LOGIN ---\n")
    for i in range(3):
        username = input("Enter username: ")
        password = input("Enter password: ")
        passs.login(username, password)

