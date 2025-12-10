class Student:
    def __init__(self, name, house):
        # this runs automatically when you do Student(name, house)
        self.name = name
        self.house = house
        print("Creating a new Student object...")
def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    # This calls Student.__init__(...)
    return Student(name,house)

if __name__ == "__main__":
    main()