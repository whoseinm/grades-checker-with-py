a = [3, 4, 2, 6, 5, 3, 4, 7, 8, 8, 3, 5, 3, 4, 2, 5, 4, 6, 2, 3]
kol = 0
i = 0
while i < 20:
    if a[i] > 6:
        kol = kol + 1
    i = i + 1
print(kol)