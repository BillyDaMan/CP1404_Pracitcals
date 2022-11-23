from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)choose taxi, d)rive"


def main():
    """Choose and drive a taxi, produces the cost of the trip"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    total_bill = 0
    current_taxi = None
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "C":
            choose_taxi(taxis, current_taxi)
        elif menu_choice == "D":
            drive_taxi(current_taxi, total_bill)
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        menu_choice = input(">>> ").upper()
    print("Have a nice day >:)")


def choose_taxi(taxis, current_taxi):
    """Displays available taxis and chooses one"""
    print("Taxis available")
    display_taxis(taxis)
    taxi_choice = int(input("Choose taxi: "))
    try:
        current_taxi = taxis[taxi_choice]
    except IndexError:
        print("Invalid taxi choice")
    return current_taxi


def display_taxis(taxis):
    """Displays available taxis in a numbered list"""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def drive_taxi(current_taxi, total_bill):
    """Drive a distance and return the price to the total bill"""
    if current_taxi:
        current_taxi.start_fare()
        distance_to_drive = float(input("Drive how far?: "))
        current_taxi.drive(distance_to_drive)
        trip_cost = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
        total_bill += trip_cost
    else:
        print("You need to choose a taxi before you can drive")
    return total_bill


main()
