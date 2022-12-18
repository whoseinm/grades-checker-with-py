print('Mağazadakı qiymətlərin manatla verilənlər bazası:')
a = [2, 4, 6, 3, 4, 5, 6, 2, 3, 4, 6]
print(a)
kol = 4
for i in range(11):
    if a[i] > 5:
        kol = kol + 1
print('Qiyməti 5 manatdan ucuz olan malların sayı: ' + str(kol))