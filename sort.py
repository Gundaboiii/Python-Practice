def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Input list from the user
numbers = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))

# Calling the bubble_sort function
sorted_numbers = bubble_sort(numbers)

# Printing the sorted list
print("Sorted list is:", sorted_numbers)
