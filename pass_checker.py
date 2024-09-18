# Predefined system password
SYSTEM_PASSWORD = "SecurePassword123"  # Replace with your desired password

# Function to check password
def check_password():
    # Prompt the user to enter a password
    user_password = input("Please enter your password: ")

    # Compare the entered password with the system password
    if user_password == SYSTEM_PASSWORD:
        print("Access granted. Welcome to the system!")
    else:
        print("Access denied. Incorrect password.")

# Call the function to check password
check_password()
