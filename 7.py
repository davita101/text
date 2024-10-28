def func(x):
    arr = [0,1]
    for i in range(2, x):
        arrList = arr[i-1] + arr[i-2]
        arr.append(arrList)
    return arr
print(func(7))
print(func(5))