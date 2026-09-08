# ============================================================
# HASH TABLE IMPLEMENTATION
# Prepared by: Jun Y. Ercia
# Hashing Method: Mid-Square Method
# Collision-Resolution Method: Linear Probing
# Hash Function:
#   1. Square the key.
#   2. Take the middle two digits.
#   3. Compute: h(k) = middle_digits mod N
# ============================================================

class HashTable:
    DELETED = "<DELETED>"

    def __init__(self, size):
        # Create an empty hash table
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        # Step 1: Square the key
        square = key ** 2

        # Step 2: Convert the square to four digits
        square_string = str(square).zfill(4)

        # Step 3: Get the middle two digits
        middle_digits = int(square_string[1:3])

        # Step 4: Convert the middle digits into a valid table index
        return middle_digits % self.size

    def insert(self, key):
        # Compute the original index using the Mid-Square Method
        index = self.hash_function(key)
        original_index = index

        while self.table[index] is not None and self.table[index] != self.DELETED:
            # Linear Probing:
            # Move to the next slot when the current slot is occupied
            index = (index + 1) % self.size

            # Stop if the table is full
            if index == original_index:
                print("Hash table is full.")
                return False

        self.table[index] = key
        return True

    def search(self, key):
        # Compute the original index
        index = self.hash_function(key)
        original_index = index

        while self.table[index] is not None:
            if self.table[index] == key:
                return index

            # Continue linear probing
            index = (index + 1) % self.size

            if index == original_index:
                break

        return -1

    def delete(self, key):
        # Search for the key first
        index = self.search(key)

        if index != -1:
            # Mark the slot as deleted
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

# Create a hash table with 10 slots
hash_table = HashTable(10)

# Keys to insert
keys = [10, 11, 12, 20, 21, 22]

# Insert the keys
for key in keys:
    hash_table.insert(key)

# Display the hash table
hash_table.display()

# Search for a key
print("\nSearch for 21:")

index = hash_table.search(21)

if index != -1:
    print("21 was found at index", index)
else:
    print("21 was not found.")

# Delete a key
print("\nDelete 11:")

if hash_table.delete(11):
    print("11 was deleted.")
else:
    print("11 was not found.")

# Display the updated hash table
hash_table.display()
