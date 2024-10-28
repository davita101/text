def func(x):
    res = sorted([char for char in x.split()])
    res2= ''
    for words in x:
       if not words.isdigit():
           res2+=words
    return sorted(res2.split())
print(func('is2 Thi1s T4est 3a'))
print(func("4 of Fo1r people g3ood th5e the2"))