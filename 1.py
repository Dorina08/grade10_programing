
#option one
nemjo = True

while nemjo: #addig fut amíg "nr" nem false
    szam_str = input("Szám: ")
    if szam_str.isdecimal():
        nemjo = False
        szam = int(szam_str)


if szam < 3:
    print("A szám kisebb mint 3")
elif szam > 3:
    print("A szám nagyobb mint 3")
else:
    print("A szám = 3")

