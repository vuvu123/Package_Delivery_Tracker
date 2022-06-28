import csv
from package import Package


class ChainingHashTable:

    # Constructor with optional initial capacity parameter
    # Assigns all buckets with an empty list
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table.
    def insert(self, key, package):
        # get the bucket list where this item will go
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        for item in bucket_list:
            if item[0] == key:
                item[1] = package
                return True

        # if not, insert the item to the end of the bucket list
        item = [key, package]
        bucket_list.append(item)
        return True

    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for item in bucket_list:
            if item[0] == key:
                return item[1]  # value
        return None

    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for item in bucket_list:
            if item[0] == key:
                bucket_list.remove([item[0], item[1]])

    def print_packages(self):
        for bucket in self.table:
            for package in bucket:
                print(package[1])

    def get_package_list(self, truck_num):
        # Returns list of package objects assigned to truck
        packages = []
        for bucket in self.table:
            for package in bucket:
                if int(package[1].truck) == truck_num:
                    packages.append(package[1])
        return packages

    def load_package_data(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                package = Package(int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                self.insert(int(row[0]), package)


hash_table = ChainingHashTable()
hash_table.load_package_data('data/packages.csv')
# hash_table.print_packages()
packages = hash_table.get_package_list(2)
# for package in packages:
#     print(package)
# for package in sorted(packages, key=lambda p: p.package_id):
#     print(package)
