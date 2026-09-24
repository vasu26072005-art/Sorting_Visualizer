def selectionSort(arr, updateDisplay):

    n = len(arr)

    for i in range(n):
        minIdx = i
        for j in range(i+1, n):
            updateDisplay(j, minIdx)
            if arr[j] < arr[minIdx]:
                minIdx = j

        if minIdx != i:
            arr[i], arr[minIdx] = arr[minIdx], arr[i]
            updateDisplay(i, minIdx)        