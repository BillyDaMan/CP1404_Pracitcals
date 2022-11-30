from prac_09.unreliable_car import UnreliableCar


def main():
    """Test the unreliable car class"""
    my_unreliable_car = UnreliableCar("WRX STI", 100, 50)
    my_unreliable_car.drive(40)
    print(my_unreliable_car)
    my_reliable_car = UnreliableCar("Toyota Sahara", 100, 99)
    my_reliable_car.drive(100)
    print(my_reliable_car)


main()
