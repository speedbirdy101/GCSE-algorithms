# Bubble Sort
unsorted_list = ["Josh", "Aarish", "Alfred", "Will", "Lenud", "Harry", "Kobe"]


def bubble_sort(to_sort):
    swapped = True
    while swapped:
        swapped = False

        for item_index in range(0, len(to_sort) - 1):
            if to_sort[item_index] > to_sort[item_index + 1]:
                temp = to_sort[item_index]
                to_sort[item_index] = to_sort[item_index + 1]
                to_sort[item_index + 1] = temp

                swapped = True

    return to_sort

print(bubble_sort(unsorted_list))
