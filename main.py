"""
    Demonstrate the use of the calculator package
"""

#changed to pull fromt he new folder instead of the modules folder.
from my_math_operations import my_calculator
from my_math_operations import my_geometry

def main():
    result = my_calculator.add(5, 3)
    print("addition result:", result)

    result = my_calculator.subtract(10, 4)
    print("Subtraction result:", result)

    result = my_geometry.rectangle(10, 4)
    print("The area of a rectangle with sides of 10 and 4 inch lengths is:", result)

    result = my_geometry.triangle(8, 9)
    print("The area of a triangle with a base of 8 and a height of 9 is:", result)

    result = my_geometry.circle(20)
    print(f"The area of a circle with a radius of 20 is: {result:.2f}")


main()
