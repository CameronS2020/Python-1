def double_penny(days, amount=0.01):
 
    if days == 1:
        return amount
    else: 
        return double_penny(days - 1, amount * 2)
    
 

def main():
     days = int(input("Enter the number of days: "))
     total_amount = double_penny(days)
     print(f"Total amount after {days} days: ${total_amount:,.2f}")

main()