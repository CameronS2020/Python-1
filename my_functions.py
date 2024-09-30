#practice
"""
#function definition
def greet(name):
    print("Hello, " + name + "!")
    #Calling the function
greet("monty")
#Works, but only if greet monty isn't within the function line
"""


"""
    #practice
def months(years):
    #calculate how many months old you are (Rounded to years)
    months = 12 * years
    print(f"You are {months} months old!")

years = int(input("How many years old are you?"))
months(years)
"""





"""
#parameters.
def add_numbers(number1, number2):
    #number 1 and number 2 are parameters
    return number1 + number2
#pass through default order.
total = add_numbers(5, 7)
print(total)
#override default order.
total = add_numbers(number2 = 12, number1 = 7)
print(total)
"""

"""
    Global variables should not change while the program is running
    Global "variables" are technically constants.
"""
"""
BAG_CHARGE = .10

def bag_cost(num_bags):
    cost = num_bags * BAG_CHARGE
    print(f"Cost for bags is: {cost:.2f}$")
bag_cost(7)
"""
"""
# Global variable
number = 10


def multiply(number):
    # The parameter 'number' shadows the global variable 'number'
    return number * 2


# Calling the function
result = multiply(5)

print("Result:", result)
print("Global number:", number)
"""

#homework
#Defining square by it's side. needs () even if they are empty
def square(side):
    area = side * side
    print(f"The area of a square is {area} square units! ")
square(7)

#Defining a circle by it's radius
def circle(radius):
    area = 3.14 * radius * radius
    print(f"The radius of the circle is {area} units! ")
circle(12)