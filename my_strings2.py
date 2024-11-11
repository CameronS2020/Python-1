def main():
    # Example string
    example_string = "Hello, Python programmers!"
    # TODO: Iterate through the string and print each character
    for char in example_string:
        print(char) #prints
    print("Iterating through the string:")
    # TODO: Find and print the character with the minimum ASCII value in the string

    print("\nCharacter with the minimum ASCII value:", min(example_string))
    # TODO: Find and print the character with the maximum ASCII value in the string
    print("\nCharacter with the maximum ASCII value:", max(example_string))
    # TODO: Find and print the index of the first occurrence of 'o' in the string
    print("\nIndex of 'o':", example_string.index("o"))
    # TODO: Convert the string into a list of characters and print the list
    list_of_chars = list(example_string)
    print("\nConverting string to a list of characters:", list_of_chars)
    # TODO: Count and print the number of occurrences of 'o' in the string
    print("\nCount of 'o' in the string:", example_string.count("o"))
main()
#These kinds of examples are great ways to explain strings to me, I've learned alot more in these than the random assignment practice to be honest!