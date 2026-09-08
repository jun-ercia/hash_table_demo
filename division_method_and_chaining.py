# ============================================================
# HASH TABLE IMPLEMENTATION
# Prepared by: Jun Y. Ercia
# Hashing Method: Division Method
# Collision-Resolution Method: Separate Chaining
# Hash Function: h(k) = k mod N
# ============================================================

class HashTable:
    def __init__(self, size):
        # Create a hash table containing empty buckets
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        # Division Method
        return key % self.size

    def insert(self, key):
        # Compute the table index
        index = self.hash_function(key)

        # Insert the key into the bucket
        self.table[index].append(key)

    def search(self, key):
        # Compute the table index
        index = self.hash_function(key)

        # Search for the key inside the bucket
        if key in self.table[index]:
            return True

        return False

    def delete(self, key):
        # Compute the table index
        index = self.hash_function(key)

        # Remove the key if it exists
        if key in self.table[index]:
            self.table[index].remove(key)
            return True

        return False

    def display(self):
        # Display the contents of the hash table
        for index in range(self.size):
            print(index, "->", end=" ")

            for key in self.table[index]:
                print(key, "->", end=" ")

            print("None")


# Create a hash table with 10 slots
hash_table = HashTable(10)

# Insert keys
keys = [25, 37, 45, 12, 52, 23]

for key in keys:
    hash_table.insert(key)

# Display the hash table
print("HASH TABLE")
hash_table.display()

# Search for a key
print("\nSearch for 45:")
if hash_table.search(45):
    print("45 was found.")
else:
    print("45 was not found.")

# Delete a key
print("\nDelete 25:")
if hash_table.delete(25):
    print("25 was deleted.")
else:
    print("25 was not found.")

# Display the updated hash table
print("\nUPDATED HASH TABLE")
hash_table.display()
