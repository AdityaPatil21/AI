nums = [100, 200, 34, 1, 23, 0, 768, 102]

def selectionSort(nums):
    # Iterate over the array
    for i in range(len(nums)):
        min_index = i  # Assume the current element is the minimum

        # Find the minimum element in the unsorted portion of the array
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j

        # Swap the minimum element with the current element
        nums[i], nums[min_index] = nums[min_index], nums[i]

    # Print the sorted array
    print("Sorted array is:", nums)

# Call the selectionSort function with the given array
selectionSort(nums)
#O(n^2)
#O(1)
