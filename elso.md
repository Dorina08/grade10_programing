
# Prog. óra 2023.09.11

## címsor 2

### címsor 3

- first
- second
- third

1. first
2. second
3. third

1. hi
1. :3
1. something else


```python
nemjo = True

while nemjo: #addig fut amíg "nemjo" nem false
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
```