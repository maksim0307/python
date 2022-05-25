array = ["GSGO","DOOM","HILF-LIFE"]
print(len(array[2]),array[2],array[1:2],array[::-1] )
array[0] = "S.T.A.L.K.E.R"
array.append("DOTA")
array1 = [n for n in array if len(n) == 4]
print(array1)
cities = ("е","с","я")
#cities[0] = "а"
print(len(cities),cities[0],cities[-1])
products = {"хлеб","помидор","уголь","Pyton"}
products.add("лаваш")
print(products)
gg = [6,8,2,3,4,1,3]
sum_gg = sum(gg)
sum_uniq = sum(set(gg))
print(sum_gg,sum_uniq,sum_gg-sum_uniq)
str = "gig1"
# print(str == str[::-1])
#или
def palindrom(s):
    if s == s[::-1]:
        print("палиндром")
    else:
        print("не палиндром")

marks = {
    "math":3,
    "inglish":5,
    "his":1,
    "Rassion":3
}
print(marks)

