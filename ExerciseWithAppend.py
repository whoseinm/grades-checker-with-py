date_friends = ['Əsmər 24 mart','Valeh 5 aprel','Əsmər 24 mart','Ziya 18 aprel','Polad 11 may','Heydər 22 may']
date_family = ['Günay 14 fevral','Murad 11 mart','Murad 11 mart','Nazim 15 aprel', 'Nazim 15 aprel','Səma 24 aprel']
a=[]
for i in range(2):
    b=input()
    a.append(b)
del date_friends[0]
del date_family[1]
del date_family[2]
b=date_friends+date_family+a
print(b)