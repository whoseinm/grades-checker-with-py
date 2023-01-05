buy = {"Ərzaq mağazası" : 140, "Taksi" : 21, "Kinoteatr" : 43, "Şirniyyat mağazası" : 15, "Dəftərxana malları mağazası" : 9}
percent = 0.05
cashback = 0
for k,v in buy.items():
    cashback = cashback + v * percent

print("Keşbek " + str(cashback))