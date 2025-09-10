def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # Shift elements of arr[0..i-1] that are greater than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place key at after the element just smaller than it
        arr[j + 1] = key

    print("Sorted array:", arr)


# Example usage
arr = [64, 25, 12, 22, 11]
print("Original array:", arr)
insertion_sort(arr)
