"""CP1406-practical 6: car simulator"""
from car import Car

def main():
    print("Let's drive!")
    car_name = input("Enter your car name: ")
    car = Car(car_name,100)
    print('{}, fuel={}, odo={}'.format(car.name, car.fuel, car.odometer))
    choice = show_menu()
    while choice != 'q':
        if choice =='d':
            distance = input('How many km do you wish to drive? ')
            while True:
                if check_valid_input(distance)== False:
                    distance = input('How many km do you wish to drive? ')
                else:
                    break
            distance = float(distance)
            distance= car.drive(distance)
            if car.fuel == 0:
                print('The car drove {}km and ran out of fuel'.format(distance))
            else:
                print("the car drove {}".format(distance))
            print('{}, fuel={}, odo={}'.format(car.name, car.fuel, car.odometer))
            choice = show_menu()
        else:
            fuel_amount = input('How many units of fuel do you want to add to the car? ')
            while True:
                if check_valid_input(fuel_amount)== False:
                    fuel_amount = input('How many units of fuel do you want to add to the car? ')
                else:
                    break
            fuel_amount = float(fuel_amount)
            car.add_fuel(fuel_amount)
            print('added {} units of fuel'.format(fuel_amount))
            print('{}, fuel={}, odo={}'.format(car.name, car.fuel, car.odometer))
            choice = show_menu()
    print("Good bye {}'s driver.".format(car.name))

def show_menu():
    '''show menu'''
    choice =input('''Menu:
d) drive
r) refuel
q) quit 
''')
    choice = choice.lower()
    while choice not in ['d','r','q']:
        choice = input('''Menu:
d) drive
r) refuel
q) quit
''')
        choice = choice.lower()
    return choice

def check_valid_input(number):
    """check whether input is alpha or less than 0"""
    if number.isalpha()==True:
        return False
    else:
        number=float(number)
        if number <0:
            return False
        else:
            return True

if __name__ == '__main__':
    main()