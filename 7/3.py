n = input
def fizzBuzz(number):
    s = ""
    n = int(number)
    number = int(number)
    for x in range(1,number+1):
        if x % 3 == 0 and x % 5 != 0:
            s += "fizz\n"
        elif x % 5 == 0 and x % 3 != 0:
            s += "buzz\n"
        elif x % 3 == 0 and x % 5 == 0:
            s += "fillBuzz\n"
        else:
            s += str(x)
print(fizzBuzz(n))








