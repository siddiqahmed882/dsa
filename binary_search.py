def binarySearch(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (high + low) // 2
        if target == array[mid]:
            return True
        elif target > array[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False


nums = []
for i in range(0, 100, 2):
    nums.append(i)

print(binarySearch(nums, 50))
