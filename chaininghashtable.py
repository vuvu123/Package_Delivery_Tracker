import csv
from package import Package


# Chaining hash table data structure holds package data
class ChainingHashTable:

    # Constructor with optional initial capacity parameter - O(N)
    # Assigns all buckets with an empty list
    def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table - O(n)
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

    # Get value from hash table - O(n)
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for item in bucket_list:
            if item[0] == key:
                return item[1]  # value
        return None

    # Remove value from hash table - O(n)
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for item in bucket_list:
            if item[0] == key:
                bucket_list.remove([item[0], item[1]])

    # Helper function. Returns a lot of all packages sorted by ID - O(N^2)
    def get_all_packages(self):
        all_packages = []
        for bucket in self.table:
            for package in bucket:
                all_packages.append(package[1])
        return sorted(all_packages, key=lambda p: p.package_id)  # Sorts package list by ID

    # Loads all package data from file - O(n)
    def load_package_data(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                package = Package(int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7], int(row[8]))
                self.insert(int(row[0]), package)


# Helper function creates ChainingHashTable object, loads data, then returns the object
def create_package_hash_table():
    packages_ht = ChainingHashTable()
    packages_ht.load_package_data('data/packages.csv')
    return packages_ht


# ChainingHashTable object to be used elsewhere
pack_hash_table = create_package_hash_table()

