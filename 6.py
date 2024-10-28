def func(x):
    copy_wor = x[0].lower()+x[1:]
    copy_wor = "".join(i for i in copy_wor if i not in " ")
    
    res = ""
    for char in copy_wor:
        if char == char.upper() and char.isalpha():
            res += "_"+char.lower() 
        else:
            res+= char
    return res
            
print(func("TestController"))
print(func("MoviesAndBooks"))
print(func("App7    Test"))
print(func("1"))