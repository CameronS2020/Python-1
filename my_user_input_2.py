"""
Create a Python application that allows users to input their total budget and the amount spent in various categories. 
The program will then calculate and display what percentage of the total budget each category represents.
"""

#input based variables for future equations
budget = float(input("how much do you have to spend each month? "))
housing = float(input("How much do you spend on rent each month? "))
utilities = float(input("How much are you spending on utilities each month? "))
groceries = float(input("How much are you spending on food and drinks each month? "))
transportation = float(input("how much are you spending to get around each month? "))
health_care = float(input("Health care is important, how much is your monthly rate? "))
personal_care = float(input("we all have to take care of ourselves, how much do you splurge on self care? "))
clothing = float(input("it's nice to stay fresh, how much do you spend on clothes each month? "))
debt = float(input("Some of us are paying off debts, how much do you have to make up for each month? "))
#Making the percentage variables.
#TODO clean this mess (it at leats works.)
total_spending = housing + utilities + groceries + transportation + health_care + personal_care + clothing + debt
net_total = budget - total_spending
print(f"Your mothly spending adds up toa total of {total_spending:.2f}")
print(f"This is how much you're coming out of the month with! {net_total:.2f}")
print(f"This is how much of your budget is spent on housing! {housing / budget * 100:.2f}%")
print(f"This is how much of your budget is spent on utilities! {utilities / budget * 100:.2f}%")
print(f"This is how much of your budget is spent on groceries! {groceries / budget * 100:.2f}%")
print(f"This is how much of your budget is spent on transportation! {transportation / budget * 100:.2f}%")
print(f"This is how much of your budget is spent on health care each month! {health_care / budget * 100:.2f}%")
print(f"This is how much of your budget is spent on personal care each month! {personal_care / budget * 100:.2f}%")
print(f"This is how much of your budget is spent on clothing each month! {clothing / budget * 100:.2f}%")
print(f"This is how much of your budget is spent on debt each month! {debt / budget * 100:.2f}%")
print(f"And this is how much of your budget is left over for whatever you want! {net_total / budget *100:.2f}%")
"""
It might seem a bit repetetive but it is extremely simplified and normalized so that people are reminded
that each payment is monthly, and that they are different things. I kept away from flattery or flair
to keep function over form for the user.
"""