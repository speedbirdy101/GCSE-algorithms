names = ["keadle", "william", "juan", "tibinia", "motvee", "lenud", "aarish", "hp", "gog", "cuba"]

# Binary search
left_index = 0
right_index = len(names) - 1
found = False

# Must be sorted for binary to work
names.sort()
print(names)

while not found:
    mid_point = (left_index + right_index) // 2

    name = names[mid_point]
    if name.lower() == to_find.lower():
        found = True
        print(f"Found {name} at index {mid_point}")

    if name < to_find:
        left_index = mid_point + 1
    else:
        right_index = mid_point - 1
