

def bankomat(money):
    res = []
    banknotes = [10000,5000, 2000, 1000, 500, 200, 100, 50, 10]

    for b in banknotes:
        while money - b >=0:
            res.append(b)
            money -= b

    return res

print(bankomat(30000000000))
