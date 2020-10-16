def bubble_sort(list_to_sort):

    while True:

        all_sorted = True

        for i, item in enumerate(list_to_sort):

            if i == len(list_to_sort) - 1:
                if all_sorted:
                    return list_to_sort
            else:
                next_item = list_to_sort[i + 1]
                if item > next_item:
                    all_sorted = False
                    list_to_sort[i], list_to_sort[i+1] = list_to_sort[i+1], list_to_sort[i]


print(bubble_sort([4,3,78,2,0,2, 6098, 234, 23, 53, 1, 5, -2, 5, 9]))
