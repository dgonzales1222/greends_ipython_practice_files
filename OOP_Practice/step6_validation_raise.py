# Raise is a keyword that signals or throws an exception usually put in __init__

class Student:
    def __init__(self, name, house):
        # Validate input using raise to enforce correct values
        # Missing Name
        if not name:
            raise ValueError("Missing or Invalid Name")
        # Invalid House
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House. Go leave Hogwarts.")
        # If name is Lord Voldemort
        if name == "Lord Voldemort":
            raise ValueError("Good Heavens, evacuate everyone!") #hahaha
        
        self.name = name
        self.house = house
    def __str__(self):
        # How the object should look when printed
        return f"Welcome to Hogwarts {self.name} of House {self.house}!"
               
def main():
    student = get_student()
    print("Verifying Student...")
    print(student) # now uses __str__

def get_student():
    name = input("Name: ")
    house = input("House: ")
    # This calls Student.__init__(...)
    return Student(name,house)

if __name__ == "__main__":
    main()