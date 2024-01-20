from hash_table import HashTable

H = HashTable(2)

print('H = ', H.table)

for pair in [("apple", 10), ("orange", 20), ("banana", 30), ("melon", 40)]:
    print(f'insert({pair[0]}, {pair[1]}) = ', H.insert(pair[0], pair[1]))
    print(f'get({pair[0]}) = ', H.get(pair[0]))


print('H = ', H.table)

print(f'get(watermelon) = ', H.get("watermelon"))

for key in ["banana", "watermelon", "apple"]:
    print(f'delete({key}) = ', H.delete(key))
    print('H = ', H.table)

