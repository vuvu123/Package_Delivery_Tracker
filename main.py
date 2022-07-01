# Kenny Vu | ID: 001222943

from truck import *


def ui():
    delivery_simulation()
    user_input = None
    while user_input != 0:
        print("Welcome to WGUPS package tracking system!")
        print("\t1 => Print all packages at a specified time.")
        print("\t2 => Lookup an individual package at a specified time.")
        print("\t3 => Truck mileage report.")
        print("\t0 => Exit program.")
        print()
        user_input = int(input("Please select an option from the menu: "))
        print()
        if user_input == 0:
            print("Exiting..")
            return

        if user_input == 1:
            lookup_time = input("Please enter a time. (HH:MM:SS) format and 24-hr time: ")
            if len(lookup_time) != 8:
                print("Please enter a valid time format (HH:MM:SS).\n")
                continue
            lookup_time = datetime.strptime(lookup_time, TIME_FORMAT)
            print()
            get_all_package_status(lookup_time)
            print()

        if user_input == 2:
            lookup_time = input("Please enter a time. (HH:MM:SS) format and 24-hr time: ")
            if len(lookup_time) != 8:
                print("Please enter a valid time format (HH:MM:SS).\n")
                continue
            lookup_time = datetime.strptime(lookup_time, TIME_FORMAT)
            try:
                lookup_pack_id = int(input("Please enter package id number: "))
            except ValueError:
                print("Please enter a number.\n")
                continue
            get_package_status(lookup_pack_id, lookup_time)
            print()

        if user_input == 3:
            print("------TRUCK MILEAGE REPORT------")
            print(total_miles_all_trucks())
            print("--------------------------------")
            print()


ui()
