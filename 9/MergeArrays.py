array1 = [5,1,2,4,3735,2,679,487,589,96,44,964,65,5432,742]
array2 = [3,6,2,7,3,7,3,7,5,3,89,47,755,74,8564,84,79,14,78,189,46,0,56,2,6,4,2,6,3,]
result = []
# for i in array1:
#     for j in array2:
#         if i == j:
#             result.append(i)
#             break
array1.sort()
array2.sort()
n = min(len(array1),len(array2))

for i in range(n):
    if array1[i] ==array2[i]:
        result.append(i)

print(result)
























