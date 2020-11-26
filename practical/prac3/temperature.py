MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input().upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = cel_to_fah(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit : "))
            celsius = fah_to_cel(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input().upper()
    print("Thank you.")


def fah_to_cel(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def cel_to_fah(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
