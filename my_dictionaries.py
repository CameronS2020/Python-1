
"""
looked up code for uppercase: https://chatgpt.com/share/671fe57c-3b88-800b-9319-80fd7af67205
"""


NATO_ALPHABET = {"A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo", "F": "Foxtrot", "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliett", "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar", "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango", "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray", "Y": "Yankee", "Z": "Zulu"}
       

def main():
    user_input = input("Please, put in your favorite word! ")
    # convert user_input to upper case
    word = user_input.upper()
   #make sure that the letter is repeated after Nato Alphabet
    for letter in word:
        print(NATO_ALPHABET[letter])
    
    

main()