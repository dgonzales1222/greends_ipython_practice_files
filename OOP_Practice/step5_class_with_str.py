class Student:
    def __init__(self, name, house):
        # this runs automatically when you do Student(name, house)
        self.name = name
        self.house = house
    def __str__(self):
        # How the object should look when printed
        return f"Student(name={self.name}, house={self.house})"
               
def main():
    student = get_student()
    print(student) # now uses __str__

def get_student():
    name = input("Name: ")
    house = input("House: ")
    # This calls Student.__init__(...)
    return Student(name,house)

if __name__ == "__main__":
    main()