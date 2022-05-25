import random

def randomPassword(n):
    str = "1234567890qazwsxedcrfvtgbhnujmik,ol.p;['/]/*-+!@#$%^&*()"

    password = ""
    i = 0
    while i <= n:
        password = password + random.choice(str)
        i = i + 1

    return password

print(randomPassword(999999))
