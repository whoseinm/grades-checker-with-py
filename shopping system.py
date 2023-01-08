item = int(input("Malın sayını daxil edin"))
percent = 0.03
cashback = 0
for i in range(item):
    name = input("Malın adını daxil edin")
    price = int(input("Malın qiymətini daxil edin"))
    cashback = cashback + price * percent 

print("Alışların ümumi dəyəri", price)
print("Keşbek",cashback)