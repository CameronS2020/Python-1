"""#in class practice
def main():

    # Writing user input to a file
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    # Open or create the file in write mode
    with open('writing_files/contacts.txt', 'a') as file:  # 'w' mode overwrites existing content
        # Add newline for better formatting
        # I could skip the file path if I had opened writing_files as my project folder when I opened
        # visual studio code
        file.write(name + ', ' + phone + '\n')


main()

"""


#main function
#The top part of the function seperates each piece of information between 
def main():
    date = input("Hello! please put in the current date xx/xx/xxxx ")
    time = input("And now the current time xx:xx am/pm ")
    entry = input("And a diary entry of how you're feeling today! ")
    with open('diary/diary.txt', 'w') as file:
        file.write(date + ', ' + time + ', ' + entry)
    with close('diary/diary.txt') as file:
        file.close('diary.txt')

        
main()