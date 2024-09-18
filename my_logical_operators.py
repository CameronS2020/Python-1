"""
User Input: Start by asking the user to input two distinct integers. 
Logical Operators: Implement six different logical comparisons using the input integers. Include two examples for each of the following operators:
and
or
not
Display Results: For each comparison, print both the logical statement and its result.
Guidelines for Logical Comparisons:
Ensure that your comparisons are meaningful and not too obvious (e.g., avoid comparisons like num1 == num1).
Try to use comparisons that could yield different results based on user input.
Sample Output: Here's an example of what your program's output might look like:
"""

#Taking in peoples input politely, and converting it to integers (Since we don't need to get into decimals.)
a = int(input("Could you please give me a number for a?"))
b = int(input("Could you please give me a number for b as well?"))
#Prints both neatly on seperate lines.
print("a is", a, "\nand b is", b)
#beginning of the functions, going down the list, skipping over elifs, and using elses to simplify coding.
if b > 0 and a > 0:
    print("Both numbers are above 0 = True.")
else:
    print("both numbers are above 0 = False.")
#TODO test each line seperately for both conditions.
if b > 100 and a > 100:
    print("Both numbers are greater than 100 = True.")
else: 
    print("Both numbers are greater than 100 = False.")

if a % 2==0 or b % 2==0:
    print("Either number is even? True.")
else:
    print("Either number is even? False.")

if a < 100 or b < 100:
    print("Either number is less than 100? True.")
else:
    print("Either number is less than 100? False.")
#testing the super specific numbers like 101, and 0 worked perfectly.
if a is not b:
    print("a is not equal to b. True.")
else:
    print("a is not equal to b. False.")
#It detected when both numbers were the same
if a is not 0:
    print("a is not 0. True")
else:
    print("a is not 0. False.")
#a was in fact detected as 0.