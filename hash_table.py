# Creates a hashmap class for each package to easily look up the information associated with a key
class Hashmap:
    # Constructs the object with 64 "buckets" to reduce the number of collisions
    # Time Complexity O(N)
    # Space Complexity O(1)
    def __init__(self):
        self.size = 64
        self.map = [None] * self.size

    # Creates the hashed value that will be inserted into the Hashmap object. The hash is the primary package key
    # multiplied by a prime number (13) to reduce the number of unique keys
    # Time Complexity O(1)
    # Space Complexity O(1)
    def _get_hash(self, key):
        init_hash = int(key) * 13

        return init_hash % self.size

    # The hash function uses the package ID as a key and multiplies it by a prime number
    # to reduce the number of collision after the modular division
    # Time Complexity O(N)
    # Space Complexity O(1)
    def insert(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        # if the len of the items in the map is larger than the number of buckets, doubles the number of buckets
        if len(self.map) > self.size:
            self.size = self.size * 2

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    # Returns the package information given the key
    # Time Complexity O(N)
    # Space Complexity O(1)
    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    # Removes the package information from the Hashmap given the key
    # Time Complexity O(N)
    # Space Complexity O(1)
    def remove(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

# Citation for code that was used
# (Joe James, 2016)
