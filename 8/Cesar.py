def cesar():
    alphabet_EU = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_RU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФЦШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФЦШЩЪЫЬЭЮЯ"

    shift = int(input("Смещение : "))
    message = input("Сообщение для шифровки : ").upper()
    result = ""
    lang = input("Выбери те язык RU / EU").upper()

    if lang == "RU":
        for b in message:
            index = alphabet_RU.find(b)
            new_index = index + shift
            if b in alphabet_RU:
                result += alphabet_RU[new_index]
    else:
        for b in message:
            index = alphabet_EU.find(b)
            new_index = index + shift
            if b in alphabet_EU:
                result += alphabet_EU[new_index]

    print(result)

def decode():
    alphabet_EU = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_RU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФЦШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    shift = int(input("Смещение : "))
    message = input("Сообщение для шифровки : ").upper()
    result = ""
    lang = input("Выбери те язык RU / EU").upper()

    if lang == "RU":
        for b in message:
            index = alphabet_RU.find(b)
            new_index = index - shift
            if b in alphabet_RU:
                result += alphabet_RU[new_index]
    else:
        for b in message:
            index = alphabet_EU.find(b)
            new_index = index - shift
            if b in alphabet_EU:
                result += alphabet_EU[new_index]

    print(result)



cesar()
decode()
