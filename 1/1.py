import pyautogui
# login = input("Login?  ")
# password = input("Password?  ")
#
# if login == "admin" and password == "root":
#     print("Hello, you are Admin")
# else:
#     print("Hello, thanks for choosing PyThon")
his = int(input("Histori : "))
mat = int(input("Matematika : "))
inf = int(input("Informatika : "))
sr = (his+mat+inf) / 3
if sr <= 3:
    print("Двоечник")
elif sr >3 and sr < 4:
    print("Троечник")
elif sr >=4 and sr <5:
    print("Хохохохохохохорошист")
elif sr == 5:
   print("Дай списать=)")
else:
    print("Двоечник да?")
