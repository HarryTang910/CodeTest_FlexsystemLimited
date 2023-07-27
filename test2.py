def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Flag to check if any swap occurred in this pass
        swapped = False

        # Last i elements are already in place, so we don't need to compare them again
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap the elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Set the flag to True to indicate a swap occurred
                swapped = True

        # If no two elements were swapped in the inner loop, the array is already sorted
        if not swapped:
            break

# Example usage:
if __name__ == "__main__":
    # Test the bubble sort function with a sample list
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", sample_list)

    bubble_sort(sample_list)

    print("Sorted list:", sample_list)