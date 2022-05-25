import random
array = []
for i in range(1, 50000000000): # i = 1, 2, 3, 4, 5, 6...99
    array.append(random.randint(1,i))
def bubbleSoft(arr):
    for i in range(len(arr)):
        for k in range(len(arr)):
            if arr[i]<arr[k]:
                arr[i],arr[k]=arr[k],arr[i]














print("до сортировки")
print(array)
print("после")
bubbleSoft(array)
print(array)
