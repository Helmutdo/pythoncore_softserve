palabra = "HackerRank"
palabra_modificada = ""
for i in palabra:
    if i.isupper():
        i = i.lower()
    elif i.islower():
        i = i.upper()
    elif i == " ":
        i = " "
    palabra_modificada += i
print(palabra_modificada)