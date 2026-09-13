def create_account():
    username = input("Create a username: ")
    try:
        with open("accounts.txt", "r") as file:
            if username in file.read():
                print("Username already exists. Please try again.")
                return
    except FileNotFoundError:
        pass
    if len(username) < 3:
        print("Username must be at least 3 characters long.")
        return
    password = input("Create a password: ")
    if len(password) < 3:
        print("Password must be at least 3 characters long.")
        return
    with open("accounts.txt", "a") as file:
        file.write(f"{username},{password}\n")
        print("Account created successfully!")
def login(): 
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    with open("accounts.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) != 2:
                continue
            saved_username, saved_password = parts
            if username == saved_username and password == saved_password:
                print("Login successful!")
                print(f"Welcome {username}!")
                exit()
        else:
            print("Incorrect login details. Try again.")
while True:
    print("1.Create account")
    print("2.Login")
    print("3.Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        print("Creating an account...")
        create_account()
    elif choice == "2":
        print("Logging in...")
        login()
    elif choice == "3":
        break
    else:
        print("Invalid option. Please try again.")


