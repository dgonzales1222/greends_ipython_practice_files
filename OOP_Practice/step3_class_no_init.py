class Student:
    pass

def main():
    student = Student() # create an object of type student
    print(type(student))
    student.name = input("Name: ")
    student.house = input("House: ")
    print(f"{student.name} from {student.house}")

if __name__ == "__main__":
    main()