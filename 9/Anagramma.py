def splitWord(s):
    result = []
    for letter in s:
        result.append(letter)
    return result
# print(splitWord("ЯАСВ"))
def anagramma(s1,s2):
    if len(s1) != len(s2):
        return False
    s1 = s1.lower()
    s2 = s2.lower()
    arr1 = splitWord(s1)
    arr1.sort()
    arr2 = splitWord(s2)
    arr2.sort()
    s1 = "".join(arr1)
    s2 = "".join(arr2)
    return s1 == s2
print(anagramma("«Ну что… Генуя и Лукка стали не больше, как поместьями фамилии Бонапарте». Император Наполеон управлял миром и был главным врагом человечества. И пришло время вторгнуться в Россию, которую возглавлял Александр1.Итак, малыш, Болконские и Ростовы были двумя русскими семьями, которых объединили любовь и война.Князь Андрей Болконский отправился на войну, потому что устал от своей жены. А тем временем его друг граф Пьер Безухов получил большое наследство. Андрей служил в армии полководца Кутузова. Они воевали с французами, но все время проигрывали.Когда Андрей вернулся с войны, у его жены начались роды, и она умерла. Но ребенок выжил. И через некоторое время Андрей познакомился с девушкой по имени Наташа Ростова. Он полюбил ее, но должен был соблюдать траур, так что вернулся на войну.А между тем Наташа познакомилась с Анатолем Курагиным, знаменитым ловеласом. Но она все равно стала с ним встречаться. Однако, прежде чем она успела предать Андрея, ее посадили под замок.Позднее, в сражении при Аустерлице*, Андрей был тяжело ранен. Находясь при смерти, он узнал, что сотворил Анатоль, но простил его за флирт с Наташей, потому что умирал.Когда Наполеон вошел в Москву, город был покинут, и тот начал мародерствовать. Пьер Безухов хотел покончить с Наполеоном, но его арестовали и подвергли пыткам.В конце концов, Андрей и Наташа помирились, но Андрей умер. А когда Пьера освободили, он стал навещать Наташу в память о своем друге, потом они полюбили друг друга и, конечно, поженились.Через некоторое время Наполеон сошел с ума и проиграл войну. Россия вернулась к нормальной жизни, и после такой страшной войны все закончилось миром.","ЯАСВ"))
