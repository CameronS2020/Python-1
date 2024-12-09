"""#in class example
def check():
    print("checking the system...")

def create():
    print("Creating a new entry...")

def read():
    print("Reading an entry...")

def update():
    print("Updating an entry...")

def delete():
    print("Deleting an entry...")
def main_menu():
    print("Menu:")
    while True:
        try:
            print("\nWelcome! You can create new email entries, change email addresses, delete entries, or display entries.")
            print("1. Create a new entry")
            print("2. Display an entry by last name")
            print("3. Upddate an existing entry")
            print("4. Remove an entry")
            print("5. Quit")
            choice = int(input("Please enter the number of your selection: "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("That is not a valid number. Try again.")
        except ValueError:
            print("That is not a valid number. Try again.")

main_menu()



def check():
    try:
        file = open("customer_list.txt", 'r')
        lines = file.readlines()
        file.close()
        return lines
    except FileNotFoundError:
        print("Customer list does not exist. Creating a new file...")
        return[]"""

#teachers example
"""_summary_
    CRUD - Create, Read, Update, Delete
"""
def menu():
    try:
        customer = check()
        print("Hello, what would you like to do today?")
        choice = 0
        while choice != 5:
            # menu will display options, accept a number, then call the appropriate function.
            print("1.  Search for and display a record.")
            print("2.  Create a new record.")
            print("3.  Update an existing record")
            print("4.  Delete an existing record")
            print("5.  Quit the program")
            choice = int(input("Please enter the number of your selection: "))
            if choice == 1:
                display(customer)
            elif choice == 2:
                create(customer)
            elif choice == 3:
                update(customer)
            elif choice == 4:
                delete(customer)
            elif choice == 5:
                print("Goodbye!")
            else:
                print("I don't understand!")
    except Exception as e:
            print("Invalid! ", e)



def check():
    try:
        with open("data.txt", 'r') as file:
            customers = file.readlines()
            return customers
    except FileNotFoundError:
        customers = []
        return customers
    except Exception as e:
        print("Unsuccessfull: ", e)

def create(customers):
    #create a new record, call the save function and save to the exetrnal file.
    print("Create a new record!")
    f_name = input("Please enter the first name: ").capitalize()
    l_name = input("Please enter the last name:  ").capitalize()
    email = input("Please enter the email:  ")
    record = f_name + "," + l_name + "," + email + "\n"
    customers.append(record)
    save(customers)

def save(customers):
    #Called any time a change is made
    #Writes the customers list to the data.txt
    try:
        with open("data.txt", "w") as file:
            for line in customers:
                file.write(line)
        file.close()
        print(customers)
        print("Successfully saved.")
    except Exception as e:
        print("Oops. That didn't work!", e)


# def read(customers):
#     print("Read") #Unnecessary code, it reads in the check.
#Project creep (Beyond the boundaries of the assignment) more than necessary

def find(customers):
    #find a customer, return the index of the customer
    #Search by phone number
    #return the index (The line that it's on)
    #TODO Note: IN VERSION 2 - allow searching by last name
    print("Let me look for that record for you")
    email = input("Please enter the email you want to look for  ")
    my_index = 0
    for line in customers:
        line = line.strip("\n")
        record = line.split(',')
        print(record[2])
        if record[2] == email:
            print("found!", line)
            return my_index
        else:
            my_index += 1
    print("\n\nRecord not found for email:  ", email)
    return "I'm sorry, that record does not exist \n\n"


def display(customers):
    print("We will update an existing record. ")
    account = find(customers)
    if (type(account)) == int:
        print("Account Found!")
        print(f"The record is: {customers[account]}")
    else:
        print(f"Record not found!\n{account}")

def update(customers):
    try:
        print("We will update an existing record. ")
        account = find(customers)
        changeme = customers[account].split(",")
        for item in changeme:
            print(item)

        if (type(account)) == int:
            print("Account Found!")
            print(f"The record is: {customers[account]}")
        else:
            print(f"Record not found!\n{account}")

        # menu for changing item
        choice = True
        while choice:
            print("1:  Change First Name\n2:  Change Last Name\n3:  Change Email")
            choice = int(
                input("Please enter the number of the value that you want to change:  "))

            if choice == 1:
                fname = input("Please enter the new first name:  ")
                changeme[0] = fname
                choice = False
            elif choice == 2:
                lname = input("Please enter the new last name:  ")
                changeme[1] = lname
                choice = False
            elif choice == 3:
                email = input("please enter the new last name:  ")
                changeme[2] = email
                choice = False
            else:
                "That is not a valid choice"
                choice = False

        change = ",".join(changeme)
        print(change, "Is the updated record.")
        customers[account] = change
        save(customers)

    except Exception as e:
        print("Not a valid menu choice, ", e)






def delete(customers):
    try:
        print("We will update an existing record. ")
        account = find(customers)
        deleteme = customers[account].split(",")
        for item in deleteme:
            print(item)
        if (type(account)) == int:
            print("Account Found!")
            print(f"The record is: {customers[account]}")
        else:
            print(f"Record not found!\n{account}")
        choice = True
        while choice: 
            print("1: delete this record\n2: Keep this record.")
            choice = int(input("Please enter the number of the value that you want to change: "))
           
            if choice == 1:
                print("This record has been deleted.")
                choice = False
                customers.pop(account)
            elif choice == 2:
                keep = print("This record is safe... for now. ")
                choice = False
        save(customers)
    except Exception as e:
                print("not a valid menu choice, ", e)




def main():
    # menu for user
    #customer will be the list of customer records
     #Does the file exist? If yes, copy to list, if not, create list.
    menu()

    # check()  # does the file exist? create it/ copy to list
    # save() # save the list to a file
    # create()  # create a new record
    # read() # read records
    # find() # find and display a record
    # update() # change a record
    # delete() # remove a record
    # display() # Display a record

main()
