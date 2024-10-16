"""
#Practicing try and except functions
#main function that allows the process to run.
def main():
    try:
        result = 10 / 0
        #The equation understands zeridivisionerror, and calls to the print, only when it happens.
    except ZeroDivisionError:
        print("\nCannot divide by zero!")
    finally:
        print("\nExecution Completed.\n")
        #Using blank lines to divide the learning with python code text from the actual execution (it upsets me when they are close.)
main()
"""
#This code is the starting code
#currently, the problems I've found with this code, is no main function, which I've added,
#As well as a problem with calling the input to the squared number line. I don't think the non int input can be turned into an int by typing int(number)
#The only other problem I see from the get go, is that the input isn't being triggered, meaning I need to rethink the order. which I'll do below.
"""
    def square_number():
        number = input("Enter a number to square:  ")
        squared_number = int(number) ** 2
        print(f"The square of {number} is {squared_number}.")

square_number()

"""

#This is some experimentation, learned a few things from it!
"""
#After trying it again, I realized that my call to the square_number() was in the wrong indentation, and now fixed,
#With an added main function, now works perfectly and displayed and calculates an input to it's squared number.
#Perhaps adding a :.2f to the print function so that it properly displays any possible decimals someone might use.
#Was wrong about the int input thing, it works perfectly fine written out like this, which is good to know.
#Changed the input to a float input, and changed int to float in squared_number, can now calculate squares of decimal numbers!
def main():

    def square_number():
        number = float(input("Enter a number to square:  "))
        squared_number = float(number) ** 2
        print(f"The square of {number:.2f} is {squared_number:.2f}.")

    square_number()
main()
"""
#This main function is to house the entire process.
def main():
    #This function is to take an input, times it by itself, and print the result.
    def square_number():
        number = input("Enter a number to square:  ")
        squared_number = int(number) ** 2
        print(f"The square of {number} is {squared_number}.")
        try: #made a process that tries to take your squared number result, double it, and display is in a user friendly manner.
            ruin = squared_number / int(input(f"Choose a number to divide {squared_number} by. "))
            print(f"Your squared number was {squared_number} and divided it into {ruin}")
        except ZeroDivisionError:
            #too long dont read, had a silly error, fixed it. 
            """
            #Something I really want to do, is if someone inputs a float instead of an int (decimals specifically) Is that it scolds you.
            #For some unknown to god reason, I get a ValueError and it doesn't print out bruh, it just tells me the 3 lines that are upset.
            #The error is happening outside of the try block, which is why the except doesn't catch it, I need to find a new error to cause inside of my try.
            #Getting a constant ValueError when I input a float instead of an int, but whenever I apply my except it does nothing and doesn't work.
            """
            #Made the error possible if the users second input is zero.
            print("\nDid you know you can't divide by zero, please try again! \n")
        else:
            print("Equation successful!")
        finally: 
            print("The equation is done running! \n")
        #it finally works now :>
    square_number()
main()