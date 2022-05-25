import random

array = []

for i in range(10):
    array.append(random.randint(0, i))


# print(array)
# [0, 1, 1, 2, 3, 4]

def binarySearch(arr, n):
    arr.sort()
    start = 0
    end = len(arr) - 1
    step = 0

    while start <= end:
        step += 1
        mid = (start + end) // 2
        if n == arr[mid]:
            return (mid, f"step = {step}")

        if n < arr[mid]:
            end = mid - 1

        else:
            start = mid + 1

    return -1

array.sort()
print(array)
print(binarySearch(array, 6))
