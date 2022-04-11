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

myHash.insert(packages[1][0], packages[1][1])
myHash.insert(packages[9][0], packages[9][1])

myHash.search(1)
myHash.search(12)   # None
myHash.search(10)

print(myHash.table)