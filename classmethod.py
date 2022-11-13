class Student:
    #intitalizes the contents of an object (attribute)
    def __init__(self, name, house):
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name:")
    house = input("House:")
    student = Student
    return student
    

if __name__ == "__main__":
    main()
            