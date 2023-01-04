buy = [1400, 210, 430, 150, 90]
percent = 0.1
cashback = 0
for i in range(len(buy)):
   cashback = cashback + buy[i] * percent
print("Keşbek " + str(cashback))