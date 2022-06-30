from chaininghashtable import pack_hash_table
from datetime import datetime, timedelta


class Truck:
    def __init__(self):
        self.packages = []
        self.route = []
        self.start_time = None
        self.current_time = None
        self.finish_time = None
        self.speed = 18    # 18 mph = 0.3 miles/minute
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


if __name__ == "__main__":
    load_trucks(pack_hash_table.get_all_packages())
    print(f"Truck 1 has {truck1.package_count} packages:")
    print(truck1)

    print(f"Truck 2 has {truck2.package_count} packages:")
    print(truck2)

    print(f"Truck 3 has {truck3.package_count} packages:")
    print(truck3)

    truck1.start_time = datetime(2022, 6, 29, 8, 0)
    truck2.start_time = datetime(2022, 6, 29, 9, 5)
    truck3.start_time = datetime(2022, 6, 29, 10, 0)
    print(truck1.start_time.strftime("%H:%M"))

    print(truck1.packages[0])
    print()
    truck1.packages[0].status = 'DELIVERED AT 09:37:00'
    # print(truck1.packages[0])
    # for package in pack_hash_table.get_package_list(1):
    #     if package.package_id == 1:
    #         print(package)
    pack_hash_table.print_all_packages()