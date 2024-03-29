from chaininghashtable import pack_hash_table
from nearest_neighbor import nn_sort, get_distance
from datetime import datetime, timedelta
from math import ceil

TRUCK_SPEED = 18
TRUCK1_START = datetime.strptime("08:00:00", "%H:%M:%S")
TRUCK2_START = datetime.strptime("09:05:00", "%H:%M:%S")
TRUCK3_START = datetime.strptime("10:30:00", "%H:%M:%S")
ADDRESS_CHANGE_TIME = datetime.strptime("10:20:00", "%H:%M:%S")
TIME_FORMAT = "%H:%M:%S"


# Truck class holds information about the truck
class Truck:
    def __init__(self, truck_id=1):
        self.truck_id = truck_id
        self.packages = []
        self.route = []
        self.current_time = None
        self.package_count = 0

    # Inserts package into truck's route and packages lists - O(1)
    def insert(self, package):
        self.packages.append(package)
        self.route.append(package.address)

    # Removes package from truck's route and packages lists - O(1)
    def remove(self, package):
        self.packages.remove(package)
        self.route.remove(package.address)

    # Updates current time by adding minutes based on the distance traveled - O(1)
    def add_travel_time(self, distance):
        minutes = ceil((distance / TRUCK_SPEED) * 60)
        self.current_time += timedelta(minutes=minutes)

    # Returns package object by package ID - O(N)
    def get_package(self, package_id):
        for package in self.packages:
            if package.package_id == package_id:
                return package
        return None


# Create truck objects
truck1 = Truck(1)
truck2 = Truck(2)
truck3 = Truck(3)


# Insert packages into each truck - O(N)
def load_trucks(all_packages):
    for package in all_packages:
        if package.truck == 1:
            truck1.insert(package)
            truck1.package_count += 1
        elif package.truck == 2:
            if package.notes == "delay_905":
                package.status = "EN_ROUTE"
            truck2.insert(package)
            truck2.package_count += 1
        elif package.truck == 3:
            truck3.insert(package)
            truck3.package_count += 1


# Calculates and returns total mileage for route - O(N)
def miles_driven(route):
    miles = 0
    for i in range(0, len(route) - 1):
        miles = miles + get_distance(route[i], route[i + 1])
    return miles


# Calculates total miles driven for all trucks and returns string text for mileage report - O(1)
def total_miles_all_trucks():
    truck1_miles = miles_driven(truck1.route)
    truck2_miles = miles_driven(truck2.route)
    truck3_miles = miles_driven(truck3.route)
    return f"Truck 1 miles driven: {truck1_miles}\n" \
           f"Truck 2 miles driven: {truck2_miles}\n" \
           f"Truck 3 miles driven: {truck3_miles}\n" \
           f"Total miles driven: {truck1_miles + truck2_miles + truck3_miles}"


# Sets all packages on truck to "EN ROUTE" - O(N)
def update_status_en_route(truck):
    for package in truck.packages:
        package.status = "EN ROUTE"


# Delivers truck packages. - O(N^2)
# Keeps track of time and updates package status as packages get delivered.
def deliver_truck_packages(truck):
    # Reruns nearest neighbor algorithm for truck 3 after changing package 9 address/zip code
    if truck.truck_id == 3 and truck.current_time >= ADDRESS_CHANGE_TIME:
        pack_9 = truck.get_package(9)
        pack_9.address = "410 S State St"
        pack_9.zip_code = "84111"
        truck.route.remove("300 State St")
        truck.route.append("410 S State St")
        truck.route = nn_sort(truck.route)

    update_status_en_route(truck)
    for i in range(0, len(truck.route) - 1):
        distance = get_distance(truck.route[i], truck.route[i + 1])
        truck.add_travel_time(distance)
        delivery_time = truck.current_time
        delivery_status = "DELIVERED => "
        for package in truck.packages:
            if package.address == truck.route[i + 1]:
                package.status = delivery_status
                package.time_delivered = delivery_time


# Gets individual package status at any given time - O(1)
def get_package_status(package_id, time=TRUCK1_START):
    package = pack_hash_table.search(package_id)
    if package is None:
        print("Package ID not found.")
        return

    if time < ADDRESS_CHANGE_TIME and package.package_id == 9:
        package.address = "300 State St"
        package.zip_code = "84103"
    elif package.package_id == 9:
        package.address = "410 S State St"
        package.zip_code = "84111"

    if package.truck == 1:
        start_time = TRUCK1_START
    elif package.truck == 2:
        start_time = TRUCK2_START
    elif package.truck == 3:
        start_time = TRUCK3_START

    if start_time < time < package.time_delivered:
        package.status = "EN ROUTE"
    elif time <= start_time:
        package.status = "AT THE HUB"
    else:
        package.status = "DELIVERED => "
    print(package)


# Gets all package statuses at any given time - O(N)
def get_all_package_status(time=TRUCK1_START):
    for package in pack_hash_table.get_all_packages():
        get_package_status(package.package_id, time)


# Simulates package delivery - O(1)
def delivery_simulation():
    # Load trucks with packages
    load_trucks(pack_hash_table.get_all_packages())

    # Initialize truck start times
    truck1.current_time = TRUCK1_START
    truck2.current_time = TRUCK2_START
    truck3.current_time = TRUCK3_START

    # Use nearest neighbor algorithm to sort truck routes
    truck1.route = nn_sort(truck1.route)
    truck2.route = nn_sort(truck2.route)
    truck3.route = nn_sort(truck3.route)

    # Deliver trucks
    deliver_truck_packages(truck1)
    deliver_truck_packages(truck2)
    deliver_truck_packages(truck3)

