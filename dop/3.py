# око
# мадам
def palindrom(s):
    s=s.lower()
    s1=""
    for i in s:
        if i !=" ":
            s1 += i
    print(s1)
    return s==s[::-1]
s = input("введи слово  :  ")
if palindrom(s):
    print("єто палиндром")
else: print("не палиндром")


