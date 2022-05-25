array = [1,2,3,5,11,22,50,77]
def sum1(arr):
    s = 0
    for n in arr:
        s += n
    return s
# print(sum1(array))
def sum2(arr):
    s = 0
    i = 0
    while i < len(arr):
        s += arr[i]
        i += 1
    return s
print("Summa =",sum2(array))















