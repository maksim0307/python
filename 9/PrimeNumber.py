def primeNumber(number):
    flag = False
    if number > 1:
        for i in range(2,number):
            if number % i == 0:
                flag = True
                break
        if flag == True:
            print("число",number,"не простое")
        else: print("число",number,"простое")
for i in range(1,100000000000):
    primeNumber(i)































