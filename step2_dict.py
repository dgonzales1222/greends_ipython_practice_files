def main():
    student = get_student()
    print(student)
    print(f"{student['name']} from {student['house']}")
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house":house}
if __name__ == "__main__": # __name__ Only run the main() function if this file is executed directly, NOT when it is imported
    main()