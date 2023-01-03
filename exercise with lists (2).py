summ=0
while True:
    cost=int(input("Malın qiymətini daxil edin"))
    summ=summ+cost
    answer=input("Başqa alış olacaq? (bəli/xeyr)")
    if answer=="xeyr":
        break
print("Alış məbləği",summ)