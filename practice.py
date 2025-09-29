username = input("Enter username: ").lower().strip() # user inputs a username
security_level = input("Enter the security level, Low / Medium / High :").lower().strip()
lockout_threshold = int(input("Enter lockout threshold: ")) # this sets the amount of attempts the user gets

password = input("Guess your username. Or type quit if you can't:").lower().strip() # user guesses the password

attempts = 0
login_successful = False

while attempts != lockout_threshold:
    attempts += 1
    if security_level == "low":
        if password == "guest":
            print("You guessed the password correctly.")
        else:
            print("Incorrect password") 
            password = input("Guess your username. Or type quit if you can't:").lower().strip() # user guesses the password again
