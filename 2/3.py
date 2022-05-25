letter = input("Буква:")
# у а е о э я и ю ё
arr = ["у", "а", "е", "о", "э", "я", "и", "ю", "ё"]

if letter in arr:
    print("Гласная")
else:
    print("Согласная")
