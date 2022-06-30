# Linear Search Algorithm


def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target is not in the list")


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linear_search(num, 9)
verify(result)
