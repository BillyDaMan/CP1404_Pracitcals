from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test the SilverServiceTaxi class"""
    silver_service_taxi = SilverServiceTaxi("1300 CAB", 100, 50)
    silver_service_taxi.drive(40)
    print(silver_service_taxi)
    print(silver_service_taxi.get_fare())


main()
