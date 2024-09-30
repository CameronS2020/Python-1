#Homework
"""
 Select a Song: Choose a song that is well-known and suitable for a classroom setting. Avoid any song with inappropriate or offensive content.

Identify Variables: Determine at least 8 different variables that the user will provide to customize the song. These could include names, adjectives, nouns, places, etc.

Write the Function:

Define a function named custom_song that takes at least 8 parameters corresponding to the variables you've identified.
Use f-strings to incorporate these parameters into the song's lyrics.
Ensure the function prints the customized song lyrics.
Collect User Input:

Write code to collect user input for each of the 8 variables.
Use clear and descriptive prompts to guide the user.
Call the Function:

Call the custom_song function with the user inputs as named arguments.
Ensure the order of arguments matches the parameters in your function definition
"""

#Song I selected for the mad libs assignment was "Polka dot tail" By ween

def song(animal1, noun1, body_part1, animal2, noun2, place, food, body_part2):
    print("\n\n")
    print(f"Did you ever seen a {animal1} with a polka dot tail")
    print(f"Did you ever seen a {noun1} with eight fingers on his hand")
    print(f"Did you have to dry your {body_part1} when you saw that{animal2} fly")
    print("oh no, tell me it ain't so")
    print()
    print(f"Have you ever tried to shrink, like a {noun2} in the sink")
    print(f"Have you ever tried to see what lies hidden in the {place}")
    print(f"Have you ever made a {food} and squished it in your {body_part2}")
    print("Oh no, tell me it ain't so")

input_animal1 = input("Enter an animal, please ")
input_noun1 = input("Enter a noun, please ")
input_body_part1 = input("Enter a body part please! (Keep it appropriate) ")
input_animal2 = input("Enter another animal please ")
input_noun2 = input("Enter another noun please ")
input_place = input("Enter a place please ")
input_food = input("Enter a food please ")
input_body_part2 = input("Enter another body part please! (Still keep it appropriate) ")

song(animal1=input_animal1, noun1=input_noun1, body_part1=input_body_part1, animal2=input_animal2, noun2=input_noun2,
place=input_place, food=input_food, body_part2=input_body_part2)