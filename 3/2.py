# 30 Апрель, Сентябрь Ноябрь, Июнь
# 31 - 29 Февраль, Декабрь
month = input("Месяц:")
month = month.lower()
# if month == "Июнь" or month == "Апрель" or month == "Сентябрь" or month == "Ноябрь":
#     print("30 Дней")
# elif month == "Февраль":
#     print("28 - 29 дней")
# else:
#     print("31 день")
day30 = ["июнь","апрель","сентябрь","ноябрь"]
day31 = ["май","март","июль","август","декабрь","октябрь"]
day28 = ["февраль"]
if month in day30:
    print("30 дней")
elif month in day31:
    print("31 дней")
elif month in day28:
    print("28-29 дней")
else:
    print("Гуляй васся")


























