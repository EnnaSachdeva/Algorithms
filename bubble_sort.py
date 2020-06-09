def bubble_sort(input_list):

    unsorted = True

    while unsorted:
        unsorted = False # this will break the loop

        for i in range(len(input_list)-1):
            if input_list[i] > input_list[i+1]:
                unsorted = True # this will keep the loop going
                temp = input_list[i]
                input_list[i] = input_list[i+1]
                input_list[i+1] = temp

    return input_list


print(bubble_sort([10, 5, 5, 3, 9, 1, 2]))