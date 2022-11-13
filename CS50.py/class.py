# creating a class defined with ... (no method)
class Student:
    ...

def main():
    # student vairable contains the get_student() function. We give the function the ability below (attributes)?
    student = get_student()
    # "." used instead of [list] to use class
    print(f"{student.name} from {student.house}")

# to use the class I have to change this set of code. No longer using dict data type, we will use class.
def get_student():
    name = input("Name:")
    house = input("House:")
    student = Student
    return student
    

if __name__ == "__main__":
    main()
            