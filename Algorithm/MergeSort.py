def mergeSort(arr, start, end, updateDisplay):
    if start < end:
        mid = (start + end) // 2

        mergeSort(arr, start, mid, updateDisplay)
        mergeSort(arr, mid + 1, end, updateDisplay)

        merge(arr, start, mid, end, updateDisplay)


def merge(arr, start, mid, end, updateDisplay):

    leftArray = arr[start:mid + 1]
    rightArray = arr[mid + 1:end + 1]

    i = 0
    j = 0
    k = start

    while i < len(leftArray) and j < len(rightArray):

        updateDisplay(k, k, True)

        if leftArray[i] <= rightArray[j]:
            arr[k] = leftArray[i]
            i = i + 1
        else:
            arr[k] = rightArray[j]
            j = j + 1

        k = k + 1

    while i < len(leftArray):

        updateDisplay(k, k, True)

        arr[k] = leftArray[i]
        i = i + 1
        k = k + 1

    while j < len(rightArray):

        updateDisplay(k, k, True)

        arr[k] = rightArray[j]
        j = j + 1
        k = k + 1

    updateDisplay(-1, -1)