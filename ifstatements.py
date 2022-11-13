# Prints student without __str__


class Student:
    def __init__(self, name, house, upper):
        # Defensive coding if statements always above the class attributes
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]: 
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        

    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    print(student)



def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()