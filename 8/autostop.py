stancions1 = [0,400,401,500,600,800] # 2 остановки
#                    1       2
stancions2 = [0,300,410,670,800,1200] # 3 остановки
#                1       2   3
fuel = 400
def minStops(arr):
    res = 0
    start = 0
    stop = 1
    if arr[stop]-arr[start]>fuel:
        return 0
    while start < stop and stop < len(arr):
        if arr[stop] -arr[start] <= fuel:
            stop = stop+1
        else:
            start = stop - 1
            res = res + 1
    return res
print(minStops(stancions1))
print(minStops(stancions2))








