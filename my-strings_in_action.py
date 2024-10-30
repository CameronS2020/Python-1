
# print("Apple".lower() == "apple".lower())
# num_str = "10"
# print(int(num_str) + 5)
# fruits = ["Orange", "apple", "Banana"]
# print(sorted(fruits))
# fruits.sort()
# print(fruits)

# age = input("Enter your age: ")
# age_num = int(age)
# print("you are " + str(age_num) + " years old.")


def main():
    games = 0 #games is defined to stop it at ten.
    titles=[]
    while games != 10:

        title = input("Please put in the title of your favorite games, one at a time. ")
        title = title.title()
        titles.append(title)
        games += 1 #Successfully adding each time the loop passes.
        print(titles)
        if games == 10:
            print("That was 10 games!")
            alpha_titles = sorted(titles)
            print(alpha_titles)
            print("your 10 favorite games are:")
            for elem in alpha_titles:
                print(elem)
            break
        
        #trying to figure out how to raise the number of titles each time an input is give


main()