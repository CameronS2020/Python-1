"""
Your program should iterate through the numbers 1 to 300. For each number, 
it should check if the number is divisible by 7.
A number is divisible by 7 if the remainder is 0 when the number is divided by 7. 
This can be checked using the modulus operator (%) in Python.
Write your Python script in a file named divisible_by_7.py, 
upload the link to GitHub and submit it through Canvas.
Ensure your code is well-commented, explaining the logic you've used.
"""

for i in range(0, 300):
    if i % 7==0:
        print(i, "\n")