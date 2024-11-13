#Practice
"""# Class definition
class Student:
    # Class variable
    school_name = "McHenry County College"

    def __init__(self, first_name, last_name, student_id, grade_level="Freshman"):
        # Instance variables
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_id = student_id
        self.__grade_level = grade_level

    # Getter and Setter for first_name
    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name
        
    def get_student_id(self):
        return self.__student_id
    
    def get_grade_level(self):
        return self.__grade_level

    def set_first_name(self, value):
        self.__first_name = value
    
    def set_last_name(self, value):
        self.__last_name = value

    def set_student_id(self, value):
        self.__student_id = value
    
    def set_grade_level(self, value):
        self.__grade_level = value

    # Method to print student details
    def print_student_details(self):
        print("Student Details:", vars(self))
    
    # Method to print basic info about the student
    def print_info(self):
        print(self.__first_name + " " + self.__last_name)
        print(self.__student_id)
        print(self.__grade_level)

# Main function to demonstrate usage of the Student class
def main():
    # Creating an instance of Student
    ducktor_quacks = Student("Meri", "Quacksalot", '009234', "Super Senior")
    print("\n\n\n")
    print(ducktor_quacks.get_first_name())
    ducktor_quacks.print_student_details()
    ducktor_quacks.print_info()

    print("\n\n\n")
    ducktor_quacks.set_grade_level("Ducktorate")
    ducktor_quacks.print_info()

# Calling the main function
main()
"""

vet_name = "All Paws Vet"
pet_type = "Dog"

#Assignment

class Pet:
    #class variables

    #created "pet breed", gave it a base class, and allows each different "pet" to recieve their own breed in later code.

    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_breed="Doberman"):
        #instance variables.
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name

    #getter and setters

    def get_owner_first_name(self):
        return self.__owner_first_name

    def get_owner_last_name(self):
        return self.__owner_last_name

    def get_pet_id(self):
        return self.__pet_id

    def get_pet_name(self):
        return self.__pet_name

    def get_pet_breed(self):
        return self.__pet_breed

    def set_owner_first_name(self, value):
        self.__owner_first_name = value

    def set_owner_last_name(self, value):
        self.__owner_last_name = value

    def set_pet_id(self, value):
        self.__pet_id = value

    def set_pet_name(self, value):
        self.__pet_name = value

    def set_pet_breed(self, value):
        self.__pet_breed = value
        #set a LOT of things, but it's all important. especially pet_breed since i almost didn't get or set it.

    #method to print pet details
    def print_pet_details(self):
        print("Pet Details: ", vars(self))

    #method to print basic info about the pet
    def print_info(self):
        print(self.__owner_first_name + " " + self.__owner_last_name)
        print(self.__pet_id)
        print(self.__pet_name)
        print(self.__pet_breed)

#main function to actually give a result.

def main():
    #creating an instance of a pet
    pet_1 = Pet("Owner: Luis", "Sera", "Pet_id: 752", "Princess")
    print("\n")
    print(pet_1.get_owner_first_name())
    pet_1.print_pet_details()
    pet_1.print_info

    print("\n")
    pet_1.set_pet_breed("Shiba Inu")
    pet_1.print_info()
    print("Vet clinic: ", vet_name,)
    print("Pet_type: ", pet_type)
    print(hasattr(pet_1, "_Pet__owner_first_name")) 

    #Second instance of a pet
    pet_2 = Pet("Owner: Blowey", "Joeseph", "Pet_id: 223", "Pet_name: Carrot top")
    print("\n")
    print(pet_2.get_owner_first_name())
    pet_2.print_pet_details()
    pet_2.print_info

    print("\n")
    pet_2.set_pet_breed("Pet_breed: Welsh Corgi")
    pet_2.print_info()
    print("Vet clinic: ", vet_name,)
    print("Pet_type: ", pet_type)
    print(hasattr(pet_2, "_Pet__pet_middle_name"))
    #Third and final instance of a pet
    pet_3 = Pet("Owner: Moriah", "Carey", "Pet_id: 001", "Pet_name: Christmas")
    print("\n")
    print(pet_3.get_owner_last_name())
    pet_3.print_pet_details()
    pet_3.print_info

    print("\n")
    pet_3.set_pet_breed("Pet_breed: Chihuahua")
    pet_3.print_info()
    print("Vet clinic:", vet_name,)
    print("Pet_type:", pet_type)
    print(hasattr(pet_3, "_Pet__pet_id"))
#calling the main function
main()