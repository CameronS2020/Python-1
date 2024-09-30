#Operations on Lists.


#List operations Demos.
"""
delinquent_accounts = [1956, 2008, 3278, 4189]
if 2008 in delinquent_accounts:
    print("The account number 2008 is delinquent.")
else:
    print("The account number 2008 is not delinquent.")

for i in range(len(delinquent_accounts)):
    if delinquent_accounts[i] == 2008:
        print("The account number 2008 is at index", i) #1
"""

"""
#define the list of items needed to buy
needed_list = ["Apples", "Lettuce", "Bread", "Milk", "Peanut Butter"]

#initialize a variable to keep track of items acquired
got_it = "Ice cream"

#loop until the user indicates they are done shopping
while got_it  != "done":
    #display the list of needed items
    for item in needed_list:
        print(item)

    #prompt the user to enter the item they have acquired
    got_it = input("\nPlease enter the item that you have gotten from the list:    ")

    #Check if the acquired item is in the list of needed items
    if got_it in needed_list:
        #if the item is found, remove it from the list
        needed_list.remove(got_it)
    
    #check if all items have been acquired
    if len(needed_list) == 0:
        #if the list is empty, indicate that the shopping is complete
        print("You Are Done!")
        # set the variable to 'done' to exit the loop
        got_it = "done"
"""

"""
Homework assignment
Initialize the Seating List:

Create a list in your program representing the 20 seats. This list should initially include all seat numbers (1-20).
Display Available Seats:

Write code to display the list of available seats to the customer. This list should update as seats are sold.
Implement the Ticket Purchase Process:

Prompt the customer to select a seat by entering its number.
Include instructions in your prompt, indicating that the customer should enter '0' to finish their purchase.
Update Seat Availability:

Once a seat is selected, remove it from the list of available seats.
After each selection, display the updated list of available seats.
Continue this process until the customer enters '0', indicating they are done buying tickets.
Ensure User-Friendly Interaction:

Your program should handle inputs gracefully. If a customer selects a seat that doesn't exist or is already sold, display a friendly message and prompt them to choose again.
Test Your Program:

Run your program to ensure it works as expected. Try different scenarios, such as selling all seats, selling a few seats, and entering invalid seat numbers.

"""

seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

sold_seats = 100
purchased = []
while sold_seats != 0:
    for seat in seats:
        print(seat, end = ", ")
    
    
    sold_seats = int(input("\nPlease enter which seat out of 1-20 you want to purchase, and then enter 0 when you are done:   "))
    print(f"You want to buy seat {sold_seats}")
    if sold_seats in seats:
        seats.remove(sold_seats)
        purchased.append(sold_seats)
    elif len(seats) == 0:
        print("You've bought ALL of the seats!!!")
        sold_seats = "bought"
    elif sold_seats == 0:
        print(f"Thank you for purchasing seats {purchased}")
    else:
        print("Sorry, but this seat is either taken or does not exist.")