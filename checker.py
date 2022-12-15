a = [5, 1, 3, 4, 2, 6, 9, 3, 2, 5, 4]
print('Basketbol üzrə məşqlərin nəticələri azalan sıra ilə:')
a.sort(reverse = True)
print(a)
p = a[0] - a[len(a)-1]
print('Proqres bərabərdir:')
print(p)