"""def main():
    my_tuple = (1, 2, 3)
    for item in my_tuple:
        print(item)
    print("the tuple has", len(my_tuple), "items")

main()
"""
#simple function, just to call to each class with text dictating them as individual classes. then call the number of classes.
def main(): 
    programming_classes = ("Intro to python", "Advanced python", "Database Essentials", "Web Development Basics", "Data Structures in Python", "Web Design Fundamentals.")
    for item in programming_classes:
        print("The following class is underneath the programming mcc umbrella:", item)
    print("The number of classes linked to programming at mcc is", len(programming_classes))

main()