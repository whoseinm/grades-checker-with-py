color = ['aqua 0 255 255', 'black 0 0 0', 'blue 0 0 255', 'fuchsia 255 0 255', 'gray 128 128 128', 'green 0 128 0', 'lime 0 255 0', 'red 255 0 0', 'white 255 255 255', 'yellow 255 255 0']
kol = 0
for i in range(len(color)):
    if color[i].count('255') > 0:
        print(color[i])
        kol = kol + 1
print("Cəmi",kol,"belə element var.")