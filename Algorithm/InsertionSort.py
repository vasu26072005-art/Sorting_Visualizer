def insertionSort(arr, updateDisplay):

    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i-1

        while j >= 0 and arr[j] > key:

            updateDisplay(j, j+1, True)

            arr[j+1] = arr[j]

            updateDisplay(j, j+1, True)

            j = j-1

        arr[j+1] = key
        updateDisplay(j+1, i)