import time

start_time = time.time()

filename1 = 'names/names_1.txt'
filename2 = 'names/names_2.txt'

f = open(filename1, 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open(filename2, 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

duplicates = []
hash_table = {}

for name in names_1:
    hash_table[name] = ""

for name in names_2:
    if name in hash_table:
        duplicates.append(name)

print(len(names_1))
print(len(hash_table.keys()))

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
