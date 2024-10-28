def func(x):
    res = ""
    for char in x:
        if char.isalnum():
            res += char.lower()
    return res == res[::-1]


print(func("A man a plan a canal Panama"))
print(func("A man a plan a canal Paname "))