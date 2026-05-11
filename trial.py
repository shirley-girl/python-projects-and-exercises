users = {}

# -------- SIGNUP --------
def signup():
    print("\n--- SIGN UP ---")
    
    while True:
        username = input("Enter username: ")
        
        if len(username) < 3:
            print("Username must be at least 3 characters.")
        elif " " in username:
            print("Username should not contain spaces.")
        elif username in users:
            print("Username already exists.")
        else:
            break

    while True:
        password = input("Enter password: ")
        
        if len(password) < 6:
            print("Password must be at least 6 characters.")
        else:
            break

    users[username] = password
    print("Signup successful!\n")


# -------- LOGIN --------
def login():
    print("\n--- LOGIN ---")
    
    attempts = 3
    
    while attempts > 0:
        username = input("Username: ")
        password = input("Password: ")
        
        if username in users and users[username] == password:
            print("Login successful!\n")
            return
        else:
            attempts -= 1
            print(f"Invalid credentials. Attempts left: {attempts}")
    
    print("Too many failed attempts. Access denied.\n")


# -------- MAIN PROGRAM --------
while True:
    print("1. Signup")
    print("2. Login")
    print("3. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        signup()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option.\n")


# Difference of lambda function and defining functions and when to use them
# Eg 1 lambda function
numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) 

# using general function

number_list = [1,2,3,4,5]
def square (num):
    return num ** 2
squared_numbers = list(filter(number_list, square))
print(squared_numbers)




# number pattern generator

def number_pattern(n):

    if not isinstance(n,int):
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."

    result = "" # create empty string
    for i in range(1, n+1): # generates number from 1 upto the nth number
        result += str(i)
        if i != n: # if the number is not the last add space i.e(+ " ")
            result += " "
    return result

print(number_pattern(8))


        

       

            
        