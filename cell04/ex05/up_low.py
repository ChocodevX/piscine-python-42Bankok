x = input()
for i in x:
    if i.isupper():
        print(i.lower(), end="")
    else:
        print(i.upper(), end="")