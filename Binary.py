def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = list(map(int, input("Enter sorted array (space-separated): ").split()))
target = int(input("Enter the element to search: "))
result = binary_search(arr, target)
print(f"Element found at index {result}" if result != -1 else "Element not found")
