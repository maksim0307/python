# def multi(a,b,c):
#     return a*b*c
# m = multi(3,8,1)
# print(m)
# def day(n):
#     days = ["вс","пн","вт","ср","чт","пт","сб"]
#     if n >=0 and n <= 6:
#         print(days[n])
#     else:
#         print("не выдумывай!!")
# day(3)
# day(6)
# 10! 1*2*3*4*5*6*7*8*9*10
def fuctorial(number):
    if number == 0 or number == 1:
        return 1
    return fuctorial(number-1)*number
print(fuctorial(998))

