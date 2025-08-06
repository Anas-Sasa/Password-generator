# Passowrd Generator [11]

# Import needed tools from Python's toolbox
# random - for creating random passwords
# string - for getting letters, numbers and symbols
# os - for clearing the screen
# time - for adding small delays
import random, string
import os
import time

# Function to pause the program for a few seconds
def sleep(second):
    time.sleep(second)

# Function to clear the terminal screen
def clear_terminal():
    os.system('clear' if os.name == 'poix' else 'cls')


# Clear the screen when program starts
clear_terminal()

# Create empty lists to store:
# 1. The generated password pieces
# 2. The lengths for each password part (letters, numbers, symbols) 
password_generated_list = []
length_password = []

# Function to check if user input is a valid number
def verify_input(number):
    "Validate input and returns int(number) or by invalid returns false"

    # Check if the input contains only digits (1-9)
    if not number.isdigit() or int(number) == 0 :
        return False
    else:
        #If it's a valid number, convert it from text to actual number
        return int(number)

# Function to ask users how many letters, numbers and symbols they want
def take_tokens_num():

    "Take 3 inputs of passowrd length by (for loop), than check thier length if matched the length of asked password. After that append them to length_passowrd list, if something invalide --> returns False"

     # The three parts we'll ask about
    tokens_name = ["character", "number", "punctuation"]

    # Start by assuming all inputs will be valid
    is_valid = True

    # Ask about each part one by one
    for token in tokens_name:

        # Ask user how many of this part they want
        token_num = verify_input(number= input(f"\nEnter how many {token}:   "))
        
        # If input is valid, add number to our list
        if token_num:
            length_password.append(token_num)
        else:
            # If invalid, mark that we found a problem
            is_valid = False

    # Tell the calling code if everything was valid
    return is_valid

# Function to create the password based on user's requested lengths
def generate_passowrd(lenght_passowrd):
    "Generate pass and append it to the passowrd_generated --> list"

    # Temporary list to hold password parts before mixing
    asked_pass = []
    
    # For each length the user gave us...
    for num in lenght_passowrd:

        # If this is the first length = (characters)...
        if  lenght_passowrd.index(num) == 0:

            # Add random letters to our temporary list
            asked_pass.append(random.choices(string.ascii_letters, k= (num)))

        # If this the second length = (numbers)
        if lenght_passowrd.index(num) == 1:

             # Add random numbers to our temporary list
            asked_pass.append(random.choices (string.digits, k= (num)))

        # If this the theerd length = (symbols)
        if lenght_passowrd.index(num) == 2:

            # Add random symbols to our temporary list
            asked_pass.append(random.choices(string.punctuation, k= (num)))

    # Combine all the parts into the store list
    for token_list in asked_pass:

        for token in token_list:
            password_generated_list.append(token)

# Weclome massage
print("\n\n****** Welcome in Password Generator: ******\n\n")
sleep(1)

# Main program loop - keeps running until user wants to quit
program_on = True
while program_on:

    # Start by assuming everything will go well
    is_successful = True
    clear_terminal()

    # Ask user how long they want their password to be
    password_long = verify_input(number= input("\n\n\nHow long do you watn the password? [ 3, 4, 5......etc]:     "))
    
    # Check if they gave us a valid number
    if not password_long:
        print("\n--> Reasons..\n\n")
        print(f"1-Entry not accepted: [{password_long}]\n2- Acceptable inputs [ 1, 2, 3.... or higher!!]")
        is_successful = False
    else:
        # If first input was good, ask about letters/numbers/symbols
        if not take_tokens_num():
            print("\n--> Reasons..\n\n")
            print(f"\n\n1-Unacceptable entry!!\n2-Acceptable inputs [ 1, 2, 3...or higher!!!\n\n")
            is_successful = False
        else:
           # Check if the parts add up to the total length requested
            if password_long != sum(length_password):
                print(f"\n\nThe requewsted lenght of password not matched the number of tokens!!\n\n")
                is_successful = False

            else:

                # If everything checks out, generate the password!
                generate_passowrd(lenght_passowrd= length_password)

                # Mix up the characters so they're not in order (letters, then numbers, then symbols)
                random.shuffle(password_generated_list)

                # Combine all characters into one text string
                finaly_password = "".join(password_generated_list)

                # Show the generated password
                print(f"-----------\n\nPASSWORD:  {finaly_password}\n\n")
                input("PRESS ENTER TO CONTINUE.......")

    # If everything worked as wel, ask if user wants to make another password
    if is_successful:
        if input("Do you want to generate another password?  y/n  ").lower() == "y":

            # Reset our lists for a new password
            length_password = []
            password_generated_list = []
        else:
            # User wants to quit, so end the program
            program_on = False
            
    # Clean up for next password or exit
    length_password = []
    sleep(3)
    clear_terminal()