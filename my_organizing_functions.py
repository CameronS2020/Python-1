#struggled for a bit of this, but function defines how the penny is doubled
def double_penny(days, amount=0.01):
 
    if days == 1:
        return amount
    else: 
        return double_penny(days - 1, amount * 2)
    
 
#The doubling penny function doesn't have to be called at the base level, it can be called only from another function if needed, like here to apply the equation in the main function.
def main():
     days = int(input("Enter the number of days: "))
     total_amount = double_penny(days)
     print(f"Total amount after {days} days: ${total_amount:,.2f}")

main()
