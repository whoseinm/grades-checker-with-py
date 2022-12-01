a = [5, 7, 11, 2, 6, 8]
print('Cari toplanılan pul: pleyer, telefon, giroskuter, it, kompüter, 3d-printer')
print(a)
manat = int(input("Toplanılan pulları neçə manat artırmaq lazımdır?"))
for i in range(6):
    a[i]=a[i] + manat
print('Yenilənmiş toplanılan pul siyahısı:')
print(a)