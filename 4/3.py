s = input("Введие коментарий : ")
# split()
lst = s.strip().split(" ")
# print(lst)
lst_new = []
for x in lst:
    if x != "":
        lst_new.append(x)
print(len(lst_new))










