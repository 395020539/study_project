old_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
new_list = []

for i in range(0, len(old_list), 10):
    new_list.append(old_list[i:i+10])

print(new_list)