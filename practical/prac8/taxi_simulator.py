"""
CP1404 Practical
Taxi simulator
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Each time, until they quit:
    The user should be presented with a list of available taxis and get to
    choose one. Then they should say how far they want to drive.
    At the end of each trip, show them the price and add it to their bill."""
    total_bill = 0
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    option = input(">>>").lower()
    while option != 'q':
        if option == 'c':
            print('Taxis available:')
            display_taxis(taxis)
            current_taxi_num = int(input("Choose taxi: "))
            while current_taxi_num not in range(len(taxis)):
                current_taxi_num = int(input("Choose taxi: "))
            current_taxi = taxis[current_taxi_num]
            print("Bill to date: ${:.2f}".format(total_bill))
            print(MENU)
            option = input(">>>").lower()
        elif option == 'd':
            current_taxi.start_fare()
            distance = float(input("Drive how far? "))
            current_taxi.drive(distance)
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, current_taxi.get_fare()))
            total_bill += current_taxi.get_fare()
            print("Bill to date: ${:.2f}".format(total_bill))
            print(MENU)
            option = input(">>>").lower()
        else:
            print("Invalid option")
            print(MENU)
            option = input(">>>").lower()
    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display all taxis"""
    for i in range(len(taxis)):
        print('{} - {}'.format(i, taxis[i]))


main()
