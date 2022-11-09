answer = input("Ev tapşırığı daxil edilsin?")
while answer == "bəli":
    text = input("Sualın cavabını daxil edin")
    print("Mətn:",str(text))
    print("Simvolların sayı: " +str(len(text))+".")
    answer = input("Ev tapşırığı daxil edilsin?")