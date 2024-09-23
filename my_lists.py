#working with lists
#append adds a last number
"""
my_list = [1, 2, 3]
my_list.append(4)
print(my_list) #output: [1, 2, 3, 4]
"""
#remove removes the first instance of inserted instance
"""
my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list) # output: [1, 3, 2]
"""
#Sory sorts them from smallest to largest (by default)
"""
my_list = [3, 1, 4, 1, 5, 9, 2]
my_list.sort()
print(my_list) #output [1, 1, 2, 3, 4, 5, 9]
"""
#reverses the order of items in the list
"""
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)
"""

#pop removes and returns the item at a giiven index ( default is the last item)

"""
my_list = [1, 2, 3]
popped_item = my_list.pop()
print(popped_item) #output 3
print(my_list) #output [1, 2]
"""


#len() not a method, but a built in function that returns the number of items inside of the list.
"""
my_list = [1, 2, 3]
print(len(my_list)) #output 3 items in the list.
"""

#homework assignment.
"""
Create a List: Start by creating a list named days that includes all seven days of the week.
Initialize an Empty List: Create an empty list called steps. This will store the number of steps taken each day.
User Input: Using a loop, ask the user to enter the number of steps they took for each day, based on your days list.
For example, "How many steps did you take on Monday?"
Store Steps: Append the user's input (number of steps) to the steps list for each day.
Display Daily Steps: Show the user the steps recorded for each day.
Total Steps: Calculate and display the total number of steps taken in the week.
Average Steps: Create a variable named average to calculate the average steps taken.
Use the formula: average = round(total / len(steps)). Display the average step
"""
#lists use square brackets, and can contain words as well as numbers. gonna practice using the example
"""
months = ["January", "February", "March", "April", "May", "June", 
"July", "August", "September", "October", "November", "December"]

num_of_days = [31,28,31,30,31,30,31,31,30,31,30,31]

for i in range(len(months)):
    month = months[i]

    days = num_of_days[i]


    print(f"{month} has {days} days")
"""
#The loop that asks you how many steps you took each day
total_steps = 0
number_of_steps = []
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
for x in days:
    my_steps = int(input(f"How many steps did you take on {x} "))

    number_of_steps.append(my_steps)
    total_steps += my_steps
    print(total_steps)
    # print(number_of_steps)
    

for i in range(len(days)):
    day = days[i]

    steps = number_of_steps[i]
    
    print(f"on {day} you took {steps} steps!")

avereage = total_steps/7
print(f"You walked a total of {total_steps} steps, with an average of {avereage} steps!")



    
#non looping way to get the information for the list.
""" [input("How many steps did you take on Sunday? "), input("How many steps did you take on Monday? "),
input("How many steps did you take on Tuesday? "), input("How many steps did you take on Wednesday? "), 
input("How many steps did you take on Thursday? "), input("How many steps did you take on Friday? "), 
input("And finally, how many steps did you take on Saturday? ")]"""

