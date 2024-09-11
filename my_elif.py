"""
Accept a numeric grade from the user and display a letter grade. The  grading scale is 
 90 - 100: A, 80-89: B, 70-79:C, 60-69:D, Below 60: F
Check to see if the number given is between 0 and 100.
"""

grade = input("What percent out of 100 did you get on the test? ")
#changing grade to an integer
grade = int(grade)
#Decided to add an A+ for those special students who go above and beyond 100%
s = str("A+")
a = str("A")
b = str("B")
c = str("C")
d = str("D")
f = str("F")
#now that my responses are made, I decide to write out simple parameters describing each grade! (Avoiding = signs since it ruined me.)
grade_letter = 0
if grade < 60: 
    grade_letter = f
elif grade < 70:
    grade_letter = d
elif grade < 80:
    grade_letter = c
elif grade < 90:
    grade_letter = b
elif grade <= 100:
        grade_letter = a
else:
    grade_letter = s

#This assignment was fun because it was the mix of Simplicity and my own struggles that makes coding so fun to me.

print ("Your score of", grade, "out of 100, results in a grade of", grade_letter, ".")
#Fun fact, putting in negative numbers is still registered as an F, and not an S, glad I checked!
#TODO change the negative from an F to a "Did not submit"
