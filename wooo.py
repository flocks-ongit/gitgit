import hashlib

# Predefined hashed password (hashed version of "SecurePassword123")
SYSTEM_PASSWORD_HASH = hashlib.sha256("SecurePassword123".encode()).hexdigest()


# Function to hash the password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Function to check password with 3 attempts
def check_password():
    attempts = 3  # User gets 3 attempts

    while attempts > 0:
        # Prompt the user to enter a password
        user_password = input("Please enter your password: ")

        # Hash the entered password
        user_password_hash = hash_password(user_password)

        # Compare the hashed entered password with the stored hashed password
        if user_password_hash == SYSTEM_PASSWORD_HASH:
            print("Access granted. Welcome to the system!")
            return  # Exit the function after a successful login
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect password. You have {attempts} {'attempt' if attempts == 1 else 'attempts'} left.")
            else:
                print("Access denied. You have been locked out due to too many incorrect attempts.")
                return


# Call the function to check password
check_password()
