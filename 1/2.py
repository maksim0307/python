import random
number = random.randint(1,10000)
print(number)
user = int( input("Угадай число от 1 до 10000    "))
print("Ваше числоооооооооооооооооооо?   ")
count = 0
while True:
    count += 1

    if number == user:
        print("ЦЫГАНИН ТЕЛЕПАТ!!!")
    elif user > number:
        print("МЕНЬШЕ")
        user = int( input("Угадай число от 1 до 100"))
    elif user < number:
        print("БОЛЬШЕ")
        user = int( input("Угадай число от 1 до 100"))

