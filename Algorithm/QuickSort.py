def quickSort(arr, start, end, updateDisplay):

    if start < end:
        pivot = partition(arr, start, end, updateDisplay)

        quickSort(arr, start, pivot - 1, updateDisplay)
        quickSort(arr, pivot + 1, end, updateDisplay)


def partition(arr, start, end, updateDisplay):

    pivot = arr[end]
    i = start - 1

    for j in range(start, end):

        updateDisplay(j, end)

        if arr[j] < pivot:

            i = i + 1

            updateDisplay(i, j, True)

            arr[i], arr[j] = arr[j], arr[i]

            updateDisplay(i, j, True)

    updateDisplay(i + 1, end, True)

    arr[i + 1], arr[end] = arr[end], arr[i + 1]

    updateDisplay(i + 1, end, True)

    return i + 1