# ============================================================
# HASH TABLE IMPLEMENTATION
# Prepared by: Jun Y. Ercia
# Hashing Method: Folding Method
# Collision-Resolution Method: Quadratic Probing
#
# Folding Method:
#   1. Divide the key into groups of 2 digits.
#   2. Add the groups.
#   3. Compute: h(k) = sum of groups mod N
#
# Quadratic Probing:
#   h_i(k) = (h(k) + i^2) mod N
#   where i = 0, 1, 2, 3, ...
# ============================================================


class HashTable:
    DELETED = "<DELETED>"

    def __init__(self, size):
        # Create an empty hash table
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        # Convert the key to a string
        key_string = str(key)

        # Divide the key into groups of 2 digits
        groups = []

        for i in range(0, len(key_string), 2):
            groups.append(int(key_string[i:i + 2]))

        # Add all groups
        total = sum(groups)

        # Convert the total into a valid table index
        return total % self.size

    def insert(self, key):
        # Compute the original index using the Folding Method
        original_index = self.hash_function(key)

        # Quadratic Probing
        for i in range(self.size):
            index = (original_index + i ** 2) % self.size

            if self.table[index] is None or self.table[index] == self.DELETED:
                self.table[index] = key
                return True

        print("Unable to insert", key)
        return False

    def search(self, key):
        # Compute the original index
        original_index = self.hash_function(key)

        # Follow the same quadratic probing sequence
        for i in range(self.size):
            index = (original_index + i ** 2) % self.size

            if self.table[index] is None:
                return -1

            if self.table[index] == key:
                return index

        return -1

    def delete(self, key):
        # Locate the key
        index = self.search(key)

        if index != -1:
            # Mark the position as deleted
            self.table[index] = self.DELETED
            return True

        return False

    def display(self):
        print("\nHASH TABLE")
        print("--------------------")

        for index in range(self.size):
            if self.table[index] is None:
                print(index, "-> Empty")

            elif self.table[index] == self.DELETED:
                print(index, "-> Deleted")

            else:
                print(index, "->", self.table[index])


# ============================================================
# MAIN PROGRAM
# ============================================================

# A prime table size is suitable for this example
hash_table = HashTable(11)

# Keys to insert
keys = [1234, 2323, 3412, 2541, 3612, 4703]

# Insert all keys
for key in keys:
    hash_table.insert(key)

# Display the hash table
hash_table.display()

# Search for a key
print("\nSearch for 3412:")

index = hash_table.search(3412)

if index != -1:
    print("3412 was found at index", index)
else:
    print("3412 was not found.")

# Delete a key
print("\nDelete 2323:")

if hash_table.delete(2323):
    print("2323 was deleted.")
else:
    print("2323 was not found.")

# Display the updated hash table
hash_table.display()
