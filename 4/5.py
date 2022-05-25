# login > 3 and < 15
# password > 5 and < 11111
login = input("Login :")
password = input("password :")
if len(login) >= 3 and len(login) <= 15:
    print("login ok")
else:
    print("Login start 3 to 15")
if len(password) >= 5 and len(login) <= 111 and not password.isdigit()and not password.isalpha():
    print("password ok")
else: print("retype password")























