def linearSearch(array, target):
    for i in range(len(array)):
        if target == array[i]:
            return True
    return False


def linearSearchOnSortedList(array, target):
    for i in range(len(array)):
        if target == array[i]:
            return True
        elif array[i] > target:
            return False


nums = [3, 9, 6, 1, 2]
