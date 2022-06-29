from chaininghashtable import ChainingHashTable
from datetime import datetime, timedelta


class Truck:
    def __init__(self):
        self.packages = []
        self.route = []
        self.start_time = None
        self.current_time = None
        self.finish_time = None
        self.speed = 18    # 18 mph = 0.3 miles/minute

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

hash_table = ChainingHashTable()
hash_table.load_package_data('data/packages.csv')

# Create truck objects
truck1 = Truck()
truck2 = Truck()
truck3 = Truck()

# Get list of packages assigned to each truck
truck1_packages = hash_table.get_package_list(1)
truck2_packages = hash_table.get_package_list(2)
truck3_packages = hash_table.get_package_list(3)

# Insert packages into each truck
for package in truck1_packages:
    truck1.insert(package)

for package in truck2_packages:
    if package.notes == "delay_905":
        package.status = "DELAYED"
    truck2.insert(package)

for package in truck3_packages:
    truck3.insert(package)

if __name__ == "__main__":
    print("Truck 1 Packages:")
    print(truck1)

    print("Truck 2 Packages:")
    print(truck2)

    print("Truck 3 Packages:")
    print(truck3)

    truck1.start_time = datetime(2022, 6, 29, 8, 0)
    truck2.start_time = datetime(2022, 6, 29, 9, 5)
    truck3.start_time = datetime(2022, 6, 29, 10, 0)
    print(truck1.start_time.strftime("%H:%M"))
