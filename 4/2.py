# for

# s = "ПриВэТЬ"
s = input("введите символы : ")

# for letter in s:
#     print(letter)

# letter1 = "a" letter2 = "b"
print(s)
big_en = 0
small_en = 0
small_rus = 0
big_rus = 0
for letter in s:
    if letter >= "а" and letter <= "я":
        small_en += 1
    elif letter >= "А" and letter <= "Я":
        big_en += 1
    elif letter >= "а" and letter <= "я":
        small_rus += 1
    elif letter >= "А" and letter <= "Я":
        big_rus += 1
print(f"Small en = {small_en} and Big en = {big_en}")
print(f"Small rus = {small_en} and Big rus = {big_en}")


