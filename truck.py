from chaininghashtable import pack_hash_table
from nearest_neighbor import nn_sort, get_distance
from datetime import datetime, timedelta
from math import ceil

TRUCK_SPEED = 18


class Truck:
    def __init__(self):
        self.packages = []
        self.route = []
        self.current_time = None
        self.package_count = 0

    def insert(self, package):
        """Insert package into truck"""
        self.packages.append(package)
        self.route.append(package.address)

    def remove(self, package):
        """Removes packaging from truck"""
        self.packages.remove(package)
        self.route.remove(package.address)

    def __str__(self):
        items = ""
        for pack in self.packages:
            items += f"{pack}\n"
        return items

    # Updates current time by adding minutes based on the distance traveled
    def add_travel_time(self, distance):
        minutes = ceil((distance / TRUCK_SPEED) * 60)
        self.current_time += timedelta(minutes=minutes)


# Create truck objects
truck1 = Truck()
truck2 = Truck()
truck3 = Truck()


# Insert packages into each truck
def load_trucks(all_packages):
    for package in all_packages:
        if package.truck == 1:
            truck1.insert(package)
            truck1.package_count += 1
        elif package.truck == 2:
            if package.notes == "delay_905":
                package.status = "DELAYED"
            truck2.insert(package)
            truck2.package_count += 1
        elif package.truck == 3:
            truck3.insert(package)
            truck3.package_count += 1


# Calculates and returns total mileage for route
def total_miles(route):
    miles = 0
    for i in range(0, len(route) - 1):
        print(f"{route[i]} -> {route[i+1]} = {get_distance(route[i], route[i+1])} miles")
        miles = miles + get_distance(route[i], route[i + 1])
    print(f"Total Miles: {miles}")
    return miles


# Delivers packages on truck
# Algorithm to deliver
# 1. Loop through nearest neighbor sorted route
# 2. Pop(first address) of route
# 3. Change status of package associated with address
# 4. Keep track of miles
# 5. Keep track of time elapsed (add_travel_time(miles))
def deliver_truck_packages(truck):
    for i in range(0, len(truck.route) - 1):
        distance = get_distance(truck1.route[i], truck1.route[i + 1])
        truck.add_travel_time(distance)
        delivery_time = truck.current_time
        delivery_status = f"DELIVERED AT {delivery_time.strftime('%H:%M:%S')}"



if __name__ == "__main__":
    load_trucks(pack_hash_table.get_all_packages())
    print(f"Truck 1 has {truck1.package_count} packages:")
    print(truck1)

    print(f"Truck 2 has {truck2.package_count} packages:")
    print(truck2)

    print(f"Truck 3 has {truck3.package_count} packages:")
    print(truck3)

    # Initialize start times for trucks
    truck1.current_time = datetime(2022, 6, 29, 8, 0)
    truck2.current_time = datetime(2022, 6, 29, 9, 5)
    truck3.current_time = datetime(2022, 6, 29, 10, 0)

    # print(total_miles(truck1.route))  # Before sorting
    # print()
    # nn_t1_route = nn_sort(truck1.route)
    # print(total_miles(nn_t1_route))

    # Testing add_travel_time function
    truck1.add_travel_time(34)
    print(truck1.current_time)


    # print(truck1.start_time.strftime("%H:%M"))
    #
    # print(truck1.packages[0])
    # print()
    # truck1.packages[0].status = 'DELIVERED AT 09:37:00'
    # pack_hash_table.print_all_packages()
