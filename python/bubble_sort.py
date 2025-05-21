def bubble_sort(arr: list) -> list:
    '''
    type arr: List[int]
    return type: List[int]
    '''
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

arr = bubble_sort([7, 3, 9, 12, 11])
print(arr)


