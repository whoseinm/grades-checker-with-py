buy = {4 : "Taksi", 14 : "Ərzaq mağazası", 9 : "Hədiyyə", 11 : "Kino", 10 : "Taksi", 15 : "Kitab mağazası"}
normal_percent = 0.07
plus_percent = 0.25
cashback = 0
price = buy.keys()
for i in price:
    if buy[i] == "Taksi":
        cashback = cashback + i * plus_percent
    else:
        cashback = cashback + i * normal_percent
print("Keşbek " + str(cashback))