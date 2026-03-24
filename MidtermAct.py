my_list = []

for i in range(1, 10):
    my_list.append(i)

print("Original list:", my_list)
print("Length of list:", len(my_list))

y = 0

for x in range(len(my_list)):
    if y < len(my_list):
        if my_list[x] == my_list[y] and x != y:
            del my_list[y]
        else:
            y = y + 1
    else:
        break

print("The list with unique elements only.")
print(my_list)