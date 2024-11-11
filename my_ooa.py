"""
_summary_
       Demonstration of writing and instantiating a class




# Class definition of a student


class Student:  # class names are capitalized
    # You can/should initialize a class with variables
    def __init__(self, first_name, last_name, student_id, year):
        # declaring the private variables. Starting with __ makes them private
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_id = student_id
        self.__year = year

    # method to get student's info as a formattes string
    def get_info(self):
        return f"{self.__first_name} {self.__last_name}, ID: {self.__student_id}, Year: {self.__year}"


def main():
    student_1 = Student("Meri", "Kasprak", "123456", "Super Senior")
    print(student_1.get_info())
    print(student_1.get_first_name(), student_1.get_last_name())
    student_1.set_last_name("Engel")
    print(student_1.get_info())

    student_2 = Student("Fred", "Flinstsont", "234566", "Freshman")
    print(student_2.get_info())


main()
"""

#above was the in class example, below is my assignment.

class person: #just an ordinary joeseph
    def __init__(self, name, address, age, phone): #initialized with variables.
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    def get_info(self): 
        return (f"name: {self.__name}, home: {self.__address}, age: {self.__age}, phone number: {self.__phone}")


def main():
    person_1 = person("Henry Mundis", "2012 Elmers street", "22 years and 3 days old", "101-232-8948")
    print(person_1.get_info())

    person_2 = person("Agatha Mundis", "180 acrewood avenue", "82 years and 2 years old", "180-555-cash-back-now")
    print(person_2.get_info())

    person_3 = person("Marge Mundis", "the fog", "35 years old", "222-222-2223")
    print(person_2.get_info())

main()