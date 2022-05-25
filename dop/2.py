import os
# file = open("test.txt","w")
# file.write("minecraft")
# os.remove("test.txt", "3.py")
os.chdir("..")
print(os.getcwd())
for dirpath,dirnames,filenames in os.walk("."):
    for dirname in dirnames:
        print("каталог:",os.path.join(dirpath,dirname))
    for filename in filenames:
        print("файл:",os.path.join(dirpath,filename))

