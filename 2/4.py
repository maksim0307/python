# 30 Апрель, Сентябрь Ноябрь, Июнь
# 31 - 29 Февраль, Декабрь

month = input("Месяц:")
month = month.lower()
if month == "Июнь" or month == "Апрель" or month == "Сентябрь" or month == "Ноябрь":
    print("30 Дней")
elif month == "Февраль":
    print("28 - 29 дней")
else:
    print("31 день")
