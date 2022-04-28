from ChainingHashTable import ChainingHashTable

packages = [
    [0, "Package 0"],
    [1, "Package 1"],
    [2, "Package 2"],
    [3, "Package 3"],
    [4, "Package 4"],
    [5, "Package 5"],
    [6, "Package 6"],
    [7, "Package 7"],
    [8, "Package 8"],
    [9, "Package 9"],
    [10, "Package 10"],
]

myHash = ChainingHashTable()

# Insert packages
myHash.insert(packages[1][0], packages[1][1])
myHash.insert(packages[10][0], packages[10][1])
print(myHash.table)
print()

print("Searching...")
print(myHash.search(1))
print(myHash.search(12))   # None
print(myHash.search(10))
print()

print("Updating...")
myHash.insert(10, "Package 10 - EDITED")
print(myHash.table)

print("Removing...")
myHash.remove(10)
print(myHash.table)
myHash.remove(1)
print(myHash.table)
