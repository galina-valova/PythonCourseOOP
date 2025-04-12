from hash_table import HashTable

table = HashTable(4)
table.insert("a", 3)
table.insert("b", 4)
table.insert(-2, "c")
table.insert(-1, "q")
table.insert(123, "qwerty")
print("deleted value =", table.pop(-1))
print("Table size =", len(table))
print("Table:", table)
