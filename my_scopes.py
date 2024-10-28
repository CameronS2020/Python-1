#Practice
"""
# sales tax calculator to demonstrate scope

# Global variable declaration
global TAX_RATE
TAX_RATE = 0.07  # Set the global tax rate to 7%

# Function to calculate tax based on the price
def calculate_tax(price):
    # 'tax' is a local variable inside this function.
    # It uses the global variable 'TAX_RATE' to calculate the tax.
    tax = price * TAX_RATE
    return tax  # Returns the calculated tax value.

# Function to calculate the total price (price + tax)
def calculate_total(price):
    # 'total' is a local variable in this function.
    # It calls 'calculate_tax' to compute the tax and adds it to the original price.
    total = price + calculate_tax(price)
    return total  # Returns the total price after adding the tax.

# Main part of the program

# Input from user, converted to float (decimal number)
price = float(input("Enter a price: "))

# Calls 'calculate_total' function and formats the output to 2 decimal places
# The formatted string is displayed to the user
print(f"The total price is ${calculate_total(price):,.2f}")

# Displays the tax rate by converting it to a percentage and formatting to 2 decimal places
print(f"The tax rate is {(TAX_RATE * 100):,.2f}%")
"""
#conversion variables are global (Make them in all caps.)
global POUND
global INCHES
POUND = 0.453592
INCHES = 0.0254



def my_input():
    #Input marks for both global variables.
    weight = float(input("Please enter your weight in pounds: "))
    height = float(input("Please enter your height in inches: "))
    #First function changing pounds to kilograms and classing them as kilograms. printed
    return weight, height



def calculate_weight(weight):
    kilograms = weight * POUND
    print(f"You weigh {kilograms:.2f} kilograms!")
    return kilograms

    #Second function, changing inches height to meters, and classing them as meters. printed
def calculate_height(height):
    meters = height * INCHES
    print(f"You are {meters:.2f} meters tall!")
    return meters


    #Using an equation to convert height and weight into body mass index, not classifying them yet.
def calculate_bmi(kilograms, meters):
    
    bmi = kilograms / (meters * meters)
    print(f"Your bmi is {bmi:.2f}%")
    return bmi



def main():
    weight, height = my_input()
    
    
    kg = calculate_weight(weight)
    m = calculate_height(height)
    body_mass_index = calculate_bmi(kg, m)
    print(f"Your body mass index is {body_mass_index:.2f}%")

main()