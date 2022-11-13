# made my self but cannot understand the memory error

class Student:
    # blue print of the class: anything i add here i need to add in the input function "get_student" too.
    
    def __init__(self, name, house,):
        self.name = name
        self.house = house

    # defined within the class (indent)
    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name:")
    house = input("House:")
    # rememeber to return class vairables instead of  defined variable
    return Student(name, house)

# remeber to always call main() and if__name__== "__main__": 
if __name__ == "__main__":
    main()
