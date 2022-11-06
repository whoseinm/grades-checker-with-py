answer = input("Daha bir iştirakçı daxil edilsin?")
while answer=="Bəli" or answer=="bəli":
    name = input("Ad daxil edin")
    surname = input("Soyad daxil edin")
    sport = input("İdman növünü daxil edin")
    trainer = input("Məşqçini daxil edin")
    print("Soyad Ad: " + name + " " + surname + ". İdman növü: " + sport + ". Məşğul olduğu məşqçi: " + trainer)
    answer = input("Daha bir iştirakçı daxil edilsin?")
    print("Verilənlər bazası dolduruldu")