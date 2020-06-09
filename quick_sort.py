def quick_sort(input_list):

    if len(input_list)<1:
        return []

    else:
        # find pivot
        pivot = input_list.pop() # taking the last element of the list as pivot

        lesser = []
        greater = []

        for item in input_list:
            if item < pivot:
                lesser.append(item)
            else:
                greater.append(item)

        result = quick_sort(lesser) + [pivot] + quick_sort(greater)
        return result


print(quick_sort([10,9,8,3,4, 5,1]))