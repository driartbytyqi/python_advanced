from adult import Adult
from child import Child


def main():
    print("===== BMI Calculator =====")

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))

    # Create object based on age
    if age >= 18:
        person = Adult(name, age, weight, height)
    else:
        person = Child(name, age, weight, height)

    # Display information
    person.print_info()


if __name__ == "__main__":
    main()