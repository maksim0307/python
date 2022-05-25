import random
def randomPassword(n):
    str = "1234567890qwertyuiopasdfghjkl;'zxcvbnm,.`[]-=!@#$%^&*()(_+_|\=-йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,QWERTYUIOPP{{}ASDFGHJKL:ZZXCVBNM<>?"
    password = ""
    i = 0
    while i <= n:
        password += random.choice(str)
        i += 1
    return password
print(randomPassword(4000000))



























