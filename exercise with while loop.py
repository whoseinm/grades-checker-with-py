buy={}
while True:
    name=input("Malın adını daxil edin")
    cost=int(input("Malın qiymətini daxil edin"))
    buy[name]=cost
    answer=input("Başqa alış olacaq? (bəli/xeyr)")
    if answer=="xeyr":
        break
print("Alışın cəmi =",sum(buy.values()))
print("Malların adı və qiyməti:")
print(buy)
