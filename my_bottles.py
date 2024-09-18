"""
Write the program "99 Bottles of Beer on the Wall" using a while loop.
 Be mindful to change the word 'bottles' to 'bottle' when you are down to the last one. 
You need to do the full 99 bottles the sample shows the last 3 verses.
"""
#does it start at 100 or 99? I remember it as 99

count = 99
while count > 0:
    print(count, "bottles of beer on the wall,")
    print(count, "bottles of beer!")
    count -= 1 #inrement decrease
    print("Take one down, pass it around")
    print(count, "bottles of beer on the wall! \n")
    if count == 2:
        print(count, "bottles of beer on the wall!")
        print(count, "Bottles of beer!")
        print("Take 1 down, pass it around")
        count -= 1
        print(count, "Bottle of beer on the wall!")
        
    
    
    if count == 1:
        print(count, "bottle of beer on the wall")
        print(count, "bottle of beer!")
        print("take one down and pass it around")
        count -= 1
        print(count, "Bottles of beer on the wall!")
