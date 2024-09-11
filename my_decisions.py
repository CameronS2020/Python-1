"""
Ask the user for their age.
Check to see if the user is old enough to drive.
Check to see if the user can vote.
Check to see if the user can legally buy alcohol.
Check to see if the user is eligible for a senior discount (65).
Print all the results on the screen.
"""

age = input("Hello, What is your age? (In years only please.) ")
#Once again transferring input into integer. insanely integral if not impertenant in this instance
age = int(age)
#Creating the if statements. I find that started at the lowest option and working your way up allows you to form future lines looking at previous ones!
if age >= 16:
    print("You can drive, but only with a license or adult supervision, you can not vote yet, you cannot legally buy alcohol, and you are NOT eligable for a senior discount!")
elif age >= 18:
    print("You can drive with a license, you can vote if registered, however you cannot legally purchase alcohol, nor do you qualify for the seniors discount")
elif age >= 21: 
    print("You can drive (With a license) you can vote (If registered) You can legally buy alocohol, BUT you do NOT qualify for the seniors discount (I know you're so old.)")
elif age >= 65:
    print("You can drive, you can vote, you can buy alcohol, and you even qualify for the seniors discount, welcome in old timer!")
else:
    print("You can't do anything just yet, enjoy being young, little baby man. ")
    #Been in a bubbly mood today, other days i've written humorous things and deleted them, wanted to see if I could get a laugh, lemme know if any of these got you!
