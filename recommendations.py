like = int(input("Paylaşıma qoyulan bəyənmələrin sayını daxil edin"))
comment = int(input("Paylaşıma yazılan şərhlərin sayını daxil edin"))
if like < 50 or comment < 5:
    print("Paylaşım aktual deyil. Mövzu pis seçilib və ya mətn pis yazılıb")
else:
    if like >= 100 and comment >= 50:
        print("Paylaşım 100% tövsiyələrə düşəcək. Yeni abunəçiləri gözləyin")
    else:
        print("Paylaşım 50% ehtimalla tövsiyələrə düşəcək")