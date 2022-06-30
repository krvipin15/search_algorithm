# Recursive Binary Search Algorithm


def recursive_binary_search(lst, target):
    if len(lst) == 0:
        return False
    else:
        midpoint = len(lst) // 2
        if lst[midpoint] == target:
            return True
        else:
            if lst[midpoint] < target:
                return recursive_binary_search(lst[midpoint+1:], target)
            else:
                return recursive_binary_search(lst[:midpoint], target)


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target is not in the list")


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = recursive_binary_search(num, 9)
verify(result)
