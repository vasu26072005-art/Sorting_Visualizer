def bubbleSort(arr, updateDisplay):

    n = len(arr)   # size of array

    for i in range(n):
        for j in range(0, n-i-1):
            updateDisplay(j, j+1)   # updates display during sorting of barss
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                updateDisplay(j, j+1) 