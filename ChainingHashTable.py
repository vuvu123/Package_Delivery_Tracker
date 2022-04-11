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
        bucket = hash(package) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = package
                return True

        # if not, insert the item to the end of the bucket list
        key_value = [key, package]
        bucket_list.append(key_value)
        return True

    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for key_value in bucket_list:
            if key_value[0] == key:
                return key_value[1] # value
        return None

    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for key_value in bucket_list:
            if key_value[0] == key:
                bucket_list.remove([key_value[0], key_value[1]])


