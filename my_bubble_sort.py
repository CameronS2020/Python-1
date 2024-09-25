#Bubble sorts sort by swapping side by side integers one at a time. like example in class (by height)
'''
    Demonstration of the Bubble Sort algorithm.
'''
"""
# Initialize a list of numbers
numbers = [8, 6, 7, 6, 5, 3, 0, 9]

# Flag to track if a swap has occurred
swapped = True

# Continue looping until no swaps occur
while swapped:
    swapped = False  # Reset the flag at the start of each iteration
    for i in range(len(numbers) - 1):
        # Compare adjacent elements
        if numbers[i] > numbers[i + 1]:
            swapped = True  # A swap is needed
            # Swap the elements
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

# Print the sorted list
print(numbers) """
#The above example shows how to check the numbers for their value, and swaps them accordingly.

#The below example, is going to show me how to categorize names alphabetically, and then go back and reverse the list.


#I actually had an error where it would reverse but neither of them were alphabetical, it was
#because I had missed an essential "while swapped:" in the mix
"""
names = ["Bob", "Carol", "Ted", "Alice", "Anna"]

swapped = True

for i in range(0, len(names)):
    names[i] = names[i].lower()
while swapped:
    swapped = False
    for i in range(len(names) - 1):
        if names[i] > names[i + 1]:
            if names[i] > names[i + 1]:
                swapped = True
                names[i], names[i + 1] = names[i + 1], names[i]


print(names)

names.reverse()

print(names)
"""
#assignment
"""
Accept five names from the user.
Store these names in a list.
Sort the list using the Bubble Sort algorithm. 
Finally, reverse the sorted list using a Python list method. 
"""


custom_names = []
names = ["first", "second", "third", "fourth", "fifth"]

for x in names:
    my_names = input(f"Please give the {x} name ")
    custom_names.append(my_names)
    #print(custom_names) FINALLY GOT IT TO WORK SOMEWHAT

swapped = True
for i in range(0, len(custom_names)):
    
    custom_names[i] = custom_names[i].lower()
while swapped:
    swapped = False
    for i in range (len(custom_names) - 1):
        if custom_names[i] > custom_names[i + 1]:
            swapped = True #a swap is needed
            custom_names[i], custom_names[i + 1] = custom_names[i + 1], custom_names[i]

print(f"The names in alphabetical order are, {custom_names}")

custom_names.reverse()

print(f"The names in reverse alphabetical order are, {custom_names}")
