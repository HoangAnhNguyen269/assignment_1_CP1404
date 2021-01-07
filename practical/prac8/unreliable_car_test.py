"""
CP1404 Practical
unreliable car test
"""
from unreliable_car import UnreliableCar
def main():
    good_car = UnreliableCar("good car",100,80)
    bad_car = UnreliableCar("bad car",100,10)

    for i in range(10):
        print("try to drive {} km".format(i))
        print("{:10} drove {:2}km".format(good_car.name, good_car.drive(i)))
        print("{:10} drove {:2}km".format(bad_car.name, bad_car.drive(i)))
    print(good_car)
    print(bad_car)

if __name__ == '__main__':
    main()