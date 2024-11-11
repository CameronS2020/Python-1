"""
Finding the ASCII values of strings.
"""
#The main function
def main():
    user_input = input("Enter a character: ")
    while len(user_input) != 1: #This makes sure that if the user input is more than 1 character, it loops and asks politely "Please use 1 character"
        print("Please enter exactly one character.")
        user_input = input("Enter a character: ")
    ascii_value = ord(user_input)
    print(f"The ASCII value of {user_input} is {ascii_value}") #Prints out it's precise location in the ascii order.

main()
