def minimumSwaps(arr):
    i = 0
    swap_count = 0
    while i<len(arr):
        if arr[i] == i+1:
            i += 1
            continue
        else:
            temp = arr[i]
            k = arr[i]
            arr[i] = arr[k-1]
            arr[k-1] = temp
            swap_count += 1

    return swap_count