#example of a return statement in a python function

"""
def add_numbers(number1, number2):
    total = number1 + number2
    return total

#using the function
result = add_numbers(5, 3)
print("The sum is:", result)
"""

#The function tells you that there are 2 numbers, and they are to be added together, to return the total
#Calling the function, but storing the values down below, outside of the function

# Return the divisor and remainder
"""
def division(num1, num2):
    whole = num1 // num2
    remainder = num1 % num2
    return whole, remainder

whole, remainder = division(12, 7)
print(f"The answer is {whole} with a remainder of {remainder}.")
"""
#it works! impressive that we can have it track and understand the remainder.

#assignment
"""
    Define the function calculate_interest with the appropriate parameters.
Inside the function, apply the formula to calculate the simple interest.
Ensure that the function returns the calculated interest and stores it in a variable named result. 
Print the variable, in a user-friendly string, formatted. 
print(f"The simple interest for a principal amount of ${principal_amount:,.2f} \
                at an interest rate of {interest_rate}% over a period of \
                {investment_time} years is: ${calculated_interest:,.2f}")

the \ is a symbol you can use to split a string over multiple lines

The {principal_amount:,.2f} format specifier formats the principal amount as a floating-point number with two decimal places, and includes commas as thousand separators.
The {calculated_interest:,.2f} does the same for the calculated interest.
Test your function with different values to ensure it works correctly.
"""


def calculate_interest():
    principal = int(input("What is the initial amount of money? "))
    rate = int(input("What is your yearly rate (use whole numbers, not decimals.) "))
    time = int(input("How many years are you going to be keeping the money invested? (please put a number only.) "))
    print(f"The base principal is {principal} with a rate of {rate / 100}% over {time} years")
    simple_interest = (principal * rate * time) / 100
    print(f"Your money gained after {time} years will be {simple_interest:.2f}$ and your total will be {principal + simple_interest:.2f}$")
calculate_interest()